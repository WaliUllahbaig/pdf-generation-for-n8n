"""
HTML to PDF Converter API
A production-grade REST API for converting HTML strings to PDF files.

This module provides a Flask-based API that:
- Converts HTML strings to PDF using WeasyPrint
- Handles comprehensive error management and logging
- Includes health checks for Docker/orchestration
- Returns proper HTTP status codes and error messages
"""

import io
import logging
import traceback
from typing import Tuple, Dict, Any
from functools import wraps
import sys

from flask import Flask, request, send_file, jsonify
from flasgger import Swagger
from weasyprint import HTML, CSS
from weasyprint.css import get_all_computed_styles
from weasyprint.css.targets import TargetCollector


# ============================================================================
# LOGGING CONFIGURATION
# ============================================================================

def setup_logging() -> logging.Logger:
    """
    Configure logging for production environment.
    Logs to both console and provides structured output.
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    
    # Formatter with timestamp, level, and message
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    console_handler.setFormatter(formatter)
    
    logger.addHandler(console_handler)
    return logger


logger = setup_logging()


# ============================================================================
# FLASK APP INITIALIZATION
# ============================================================================

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# Set maximum request size to 50MB to handle large HTML strings
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024

# Initialize Swagger for interactive API documentation
swagger = Swagger(app, template={
    "swagger": "2.0",
    "info": {
        "title": "HTML to PDF Converter API",
        "version": "1.0.0",
        "description": "Convert HTML strings to PDF files with comprehensive error handling",
        "contact": {
            "name": "API Support"
        }
    },
    "host": "localhost:5001",
    "basePath": "/",
    "schemes": ["http"],
    "consumes": ["application/json"],
    "produces": ["application/pdf", "application/json"]
})


# ============================================================================
# ERROR HANDLERS & DECORATORS
# ============================================================================

class PDFGenerationError(Exception):
    """Custom exception for PDF generation failures."""
    pass


class ValidationError(Exception):
    """Custom exception for request validation failures."""
    pass


def validate_request_content_type(f):
    """Decorator to validate that request is JSON."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not request.is_json:
            logger.warning(f"Invalid Content-Type received: {request.content_type}")
            return jsonify({
                "error": "Invalid Content-Type",
                "message": "Request must have Content-Type: application/json",
                "received": request.content_type
            }), 400
        return f(*args, **kwargs)
    return decorated_function


def handle_exceptions(f):
    """Decorator for comprehensive exception handling."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except ValidationError as e:
            logger.warning(f"Validation error: {str(e)}")
            return jsonify({
                "error": "Validation Error",
                "details": str(e)
            }), 400
        except PDFGenerationError as e:
            logger.error(f"PDF generation error: {str(e)}")
            return jsonify({
                "error": "PDF generation failed",
                "details": str(e)
            }), 500
        except MemoryError as e:
            logger.error(f"Memory error during PDF generation: {str(e)}")
            return jsonify({
                "error": "PDF generation failed",
                "details": "Insufficient memory to process PDF",
                "code": "MEMORY_ERROR"
            }), 500
        except Exception as e:
            error_traceback = traceback.format_exc()
            logger.error(f"Unexpected error: {str(e)}\n{error_traceback}")
            return jsonify({
                "error": "Internal server error",
                "details": "An unexpected error occurred while processing your request",
                "code": "INTERNAL_ERROR"
            }), 500
    return decorated_function


# ============================================================================
# REQUEST VALIDATION
# ============================================================================

def validate_html_input(data: Dict[str, Any]) -> str:
    """
    Validate and sanitize the HTML input from request.
    
    Args:
        data: The JSON request body
        
    Returns:
        The validated HTML string
        
    Raises:
        ValidationError: If validation fails
    """
    if not isinstance(data, dict):
        raise ValidationError("Request body must be a JSON object")
    
    if "html" not in data:
        raise ValidationError("Required field 'html' is missing from request body")
    
    html_content = data.get("html")
    
    if not isinstance(html_content, str):
        raise ValidationError("Field 'html' must be a string")
    
    if not html_content.strip():
        raise ValidationError("Field 'html' cannot be empty")
    
    if len(html_content) > 10 * 1024 * 1024:  # 10MB limit
        raise ValidationError("HTML content exceeds maximum size (10MB)")
    
    return html_content.strip()


# ============================================================================
# PDF GENERATION
# ============================================================================

def generate_pdf_from_html(html_content: str) -> bytes:
    """
    Convert HTML string to PDF bytes.
    
    Includes error handling for:
    - Invalid HTML
    - Missing fonts
    - Rendering errors
    - Memory issues
    
    Args:
        html_content: The HTML string to convert
        
    Returns:
        PDF content as bytes
        
    Raises:
        PDFGenerationError: If PDF generation fails
    """
    try:
        logger.info(f"Generating PDF from HTML (size: {len(html_content)} bytes)")
        
        # Create BytesIO buffer for PDF output
        pdf_buffer = io.BytesIO()
        
        # Parse and render HTML to PDF
        try:
            html_object = HTML(string=html_content)
        except Exception as e:
            raise PDFGenerationError(f"Invalid HTML structure: {str(e)}")
        
        try:
            # Write PDF to buffer
            html_object.write_pdf(pdf_buffer)
        except Exception as e:
            raise PDFGenerationError(f"Failed to render HTML to PDF: {str(e)}")
        
        # Get the PDF bytes
        pdf_buffer.seek(0)
        pdf_bytes = pdf_buffer.getvalue()
        
        if not pdf_bytes:
            raise PDFGenerationError("PDF generation produced empty output")
        
        logger.info(f"Successfully generated PDF (size: {len(pdf_bytes)} bytes)")
        return pdf_bytes
        
    except PDFGenerationError:
        raise
    except MemoryError as e:
        logger.error(f"Memory error during PDF generation: {str(e)}")
        raise PDFGenerationError("Insufficient memory to generate PDF")
    except Exception as e:
        logger.error(f"Unexpected error during PDF generation: {str(e)}")
        raise PDFGenerationError(f"Unexpected error: {str(e)}")


# ============================================================================
# API ROUTES
# ============================================================================

@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint for Docker and Kubernetes orchestration.
    ---
    tags:
      - System
    responses:
      200:
        description: Service is healthy
        schema:
          type: object
          properties:
            status:
              type: string
              example: "ok"
            service:
              type: string
              example: "html-to-pdf-api"
            version:
              type: string
              example: "1.0.0"
    """
    logger.debug("Health check requested")
    return jsonify({
        "status": "ok",
        "service": "html-to-pdf-api",
        "version": "1.0.0"
    }), 200


@app.route('/html-to-pdf', methods=['POST'])
@validate_request_content_type
@handle_exceptions
def convert_html_to_pdf():
    """
    Convert HTML string to PDF file.
    ---
    tags:
      - PDF Conversion
    consumes:
      - application/json
    produces:
      - application/pdf
    parameters:
      - in: body
        name: body
        description: HTML string to convert to PDF
        required: true
        schema:
          type: object
          required:
            - html
          properties:
            html:
              type: string
              example: "<html><body><h1>Hello World</h1><p>This is a test PDF</p></body></html>"
              description: Full HTML string to convert to PDF (max 10MB)
    responses:
      200:
        description: Successfully generated PDF file
        content:
          application/pdf:
            schema:
              type: string
              format: binary
      400:
        description: Invalid request (missing or invalid html field)
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Validation Error"
            details:
              type: string
              example: "Required field 'html' is missing from request body"
      413:
        description: Payload too large
        schema:
          type: object
          properties:
            error:
              type: string
      500:
        description: PDF generation failed
        schema:
          type: object
          properties:
            error:
              type: string
              example: "PDF generation failed"
            details:
              type: string
    """
    logger.info("HTML to PDF conversion request received")
    
    # Get and validate request data
    request_data = request.get_json()
    html_content = validate_html_input(request_data)
    
    logger.debug(f"Validated HTML content (length: {len(html_content)} characters)")
    
    # Generate PDF
    pdf_bytes = generate_pdf_from_html(html_content)
    
    # Create BytesIO object for sending file
    pdf_file = io.BytesIO(pdf_bytes)
    pdf_file.seek(0)
    
    logger.info("Sending PDF file to client")
    
    # Return PDF as downloadable file
    return send_file(
        pdf_file,
        mimetype='application/pdf',
        as_attachment=True,
        download_name='report.pdf'
    )


@app.route('/info', methods=['GET'])
def get_info():
    """
    Get API information and capabilities.
    ---
    tags:
      - System
    responses:
      200:
        description: API metadata and capabilities
        schema:
          type: object
          properties:
            name:
              type: string
              example: "HTML to PDF Converter API"
            version:
              type: string
              example: "1.0.0"
            description:
              type: string
            endpoints:
              type: object
            max_payload_size_mb:
              type: integer
              example: 50
            max_html_size_mb:
              type: integer
              example: 10
            pdf_library:
              type: string
              example: "WeasyPrint"
            production_ready:
              type: boolean
              example: true
    """
    return jsonify({
        "name": "HTML to PDF Converter API",
        "version": "1.0.0",
        "description": "Converts HTML strings to PDF files",
        "endpoints": {
            "POST /html-to-pdf": "Convert HTML to PDF",
            "GET /health": "Health check",
            "GET /info": "API information",
            "GET /apidocs": "Interactive API documentation (Swagger UI)"
        },
        "max_payload_size_mb": 50,
        "max_html_size_mb": 10,
        "pdf_library": "WeasyPrint",
        "production_ready": True
    }), 200


# ============================================================================
# ERROR HANDLERS
# ============================================================================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 Not Found errors."""
    logger.warning(f"Route not found: {request.method} {request.path}")
    return jsonify({
        "error": "Not Found",
        "message": f"The requested endpoint '{request.path}' does not exist",
        "available_endpoints": ["/html-to-pdf", "/health", "/info"]
    }), 404


@app.errorhandler(405)
def method_not_allowed(error):
    """Handle 405 Method Not Allowed errors."""
    logger.warning(f"Invalid method: {request.method} {request.path}")
    return jsonify({
        "error": "Method Not Allowed",
        "message": f"Method {request.method} is not allowed for this endpoint"
    }), 405


@app.errorhandler(413)
def request_entity_too_large(error):
    """Handle 413 Payload Too Large errors."""
    logger.warning(f"Request payload too large: {request.content_length} bytes")
    return jsonify({
        "error": "Payload Too Large",
        "message": "Request payload exceeds maximum allowed size (50MB)",
        "max_size_bytes": app.config['MAX_CONTENT_LENGTH']
    }), 413


@app.errorhandler(500)
def internal_server_error(error):
    """Handle 500 Internal Server Error."""
    logger.error(f"Internal server error: {str(error)}")
    return jsonify({
        "error": "Internal Server Error",
        "message": "An unexpected error occurred on the server"
    }), 500


# ============================================================================
# BEFORE/AFTER REQUEST HOOKS
# ============================================================================

@app.before_request
def log_request():
    """Log incoming requests."""
    logger.debug(f"Incoming request: {request.method} {request.path}")


@app.after_request
def log_response(response):
    """Log outgoing responses."""
    logger.debug(f"Response: {response.status_code} - {request.method} {request.path}")
    return response


# ============================================================================
# APPLICATION ENTRY POINT
# ============================================================================

if __name__ == '__main__':
    logger.info("=" * 80)
    logger.info("Starting HTML to PDF Converter API")
    logger.info("=" * 80)
    logger.info(f"Server running on http://0.0.0.0:5001")
    logger.info(f"Health check: GET http://localhost:5001/health")
    logger.info(f"API info: GET http://localhost:5001/info")
    logger.info(f"Convert HTML: POST http://localhost:5001/html-to-pdf")
    logger.info("=" * 80)
    
    # Run Flask app
    app.run(
        host='0.0.0.0',
        port=5001,
        debug=False,
        use_reloader=False
    )
