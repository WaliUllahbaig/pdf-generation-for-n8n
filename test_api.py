#!/usr/bin/env python3
"""
Test script for HTML to PDF Converter API
This script tests all endpoints and various scenarios
"""

import requests
import json
import os
import time
from typing import Tuple, Dict, Any
import sys


class Colors:
    """ANSI color codes for terminal output"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Configuration
API_URL = "http://localhost:5001"
TEST_OUTPUT_DIR = "test_output"


def print_header(text: str):
    """Print a formatted header"""
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'='*80}")
    print(f"  {text}")
    print(f"{'='*80}{Colors.ENDC}\n")


def print_success(text: str):
    """Print success message"""
    print(f"{Colors.OKGREEN}✓ {text}{Colors.ENDC}")


def print_error(text: str):
    """Print error message"""
    print(f"{Colors.FAIL}✗ {text}{Colors.ENDC}")


def print_info(text: str):
    """Print info message"""
    print(f"{Colors.OKCYAN}ℹ {text}{Colors.ENDC}")


def print_warning(text: str):
    """Print warning message"""
    print(f"{Colors.WARNING}⚠ {text}{Colors.ENDC}")


def create_output_dir():
    """Create output directory for test PDFs"""
    if not os.path.exists(TEST_OUTPUT_DIR):
        os.makedirs(TEST_OUTPUT_DIR)
        print_info(f"Created output directory: {TEST_OUTPUT_DIR}")


def check_server_health() -> bool:
    """Check if the server is running"""
    try:
        response = requests.get(f"{API_URL}/health", timeout=5)
        return response.status_code == 200
    except requests.ConnectionError:
        return False
    except Exception:
        return False


def test_health_endpoint() -> bool:
    """Test the /health endpoint"""
    print_header("TEST 1: Health Check Endpoint")
    
    try:
        response = requests.get(f"{API_URL}/health", timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            print_success(f"Health check passed")
            print_info(f"Response: {json.dumps(data, indent=2)}")
            return True
        else:
            print_error(f"Unexpected status code: {response.status_code}")
            return False
    except Exception as e:
        print_error(f"Health check failed: {str(e)}")
        return False


def test_info_endpoint() -> bool:
    """Test the /info endpoint"""
    print_header("TEST 2: API Info Endpoint")
    
    try:
        response = requests.get(f"{API_URL}/info", timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            print_success(f"Info endpoint accessible")
            print_info(f"API Name: {data.get('name')}")
            print_info(f"Version: {data.get('version')}")
            print_info(f"Production Ready: {data.get('production_ready')}")
            return True
        else:
            print_error(f"Unexpected status code: {response.status_code}")
            return False
    except Exception as e:
        print_error(f"Info endpoint failed: {str(e)}")
        return False


def test_simple_html() -> bool:
    """Test simple HTML conversion"""
    print_header("TEST 3: Simple HTML Conversion")
    
    html = "<html><body><h1>Test Report</h1><p>Hello World</p></body></html>"
    
    try:
        response = requests.post(
            f"{API_URL}/html-to-pdf",
            json={"html": html},
            timeout=10
        )
        
        if response.status_code == 200:
            if response.headers.get('content-type') == 'application/pdf':
                pdf_data = response.content
                output_file = os.path.join(TEST_OUTPUT_DIR, "test_simple.pdf")
                with open(output_file, 'wb') as f:
                    f.write(pdf_data)
                print_success(f"PDF generated successfully ({len(pdf_data)} bytes)")
                print_info(f"Saved to: {output_file}")
                return True
            else:
                print_error(f"Wrong content type: {response.headers.get('content-type')}")
                return False
        else:
            print_error(f"Status code: {response.status_code}")
            print_error(f"Response: {response.text}")
            return False
    except Exception as e:
        print_error(f"Test failed: {str(e)}")
        return False


def test_html_with_styling() -> bool:
    """Test HTML with CSS styling"""
    print_header("TEST 4: HTML with CSS Styling")
    
    html = """
    <html>
    <head>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; background-color: #f5f5f5; }
            h1 { color: #333; border-bottom: 2px solid #007bff; padding-bottom: 10px; }
            p { line-height: 1.6; color: #666; }
            .highlight { background-color: yellow; padding: 5px; }
        </style>
    </head>
    <body>
        <h1>Styled Report</h1>
        <p>This PDF has <span class="highlight">CSS styling</span> applied!</p>
        <p>It demonstrates how WeasyPrint renders HTML with styles.</p>
    </body>
    </html>
    """
    
    try:
        response = requests.post(
            f"{API_URL}/html-to-pdf",
            json={"html": html},
            timeout=10
        )
        
        if response.status_code == 200:
            pdf_data = response.content
            output_file = os.path.join(TEST_OUTPUT_DIR, "test_styled.pdf")
            with open(output_file, 'wb') as f:
                f.write(pdf_data)
            print_success(f"Styled PDF generated ({len(pdf_data)} bytes)")
            print_info(f"Saved to: {output_file}")
            return True
        else:
            print_error(f"Status code: {response.status_code}")
            return False
    except Exception as e:
        print_error(f"Test failed: {str(e)}")
        return False


def test_html_with_table() -> bool:
    """Test HTML with table"""
    print_header("TEST 5: HTML with Table")
    
    html = """
    <html>
    <head>
        <style>
            table { border-collapse: collapse; width: 100%; }
            th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
            th { background-color: #4CAF50; color: white; }
            tr:nth-child(even) { background-color: #f9f9f9; }
        </style>
    </head>
    <body>
        <h1>Sales Report</h1>
        <table>
            <tr>
                <th>Month</th>
                <th>Sales</th>
                <th>Growth</th>
            </tr>
            <tr>
                <td>January</td>
                <td>$10,000</td>
                <td>+5%</td>
            </tr>
            <tr>
                <td>February</td>
                <td>$12,500</td>
                <td>+25%</td>
            </tr>
            <tr>
                <td>March</td>
                <td>$15,000</td>
                <td>+20%</td>
            </tr>
        </table>
    </body>
    </html>
    """
    
    try:
        response = requests.post(
            f"{API_URL}/html-to-pdf",
            json={"html": html},
            timeout=10
        )
        
        if response.status_code == 200:
            pdf_data = response.content
            output_file = os.path.join(TEST_OUTPUT_DIR, "test_table.pdf")
            with open(output_file, 'wb') as f:
                f.write(pdf_data)
            print_success(f"Table PDF generated ({len(pdf_data)} bytes)")
            print_info(f"Saved to: {output_file}")
            return True
        else:
            print_error(f"Status code: {response.status_code}")
            return False
    except Exception as e:
        print_error(f"Test failed: {str(e)}")
        return False


def test_missing_html_field() -> bool:
    """Test error handling - missing HTML field"""
    print_header("TEST 6: Error Handling - Missing HTML Field")
    
    try:
        response = requests.post(
            f"{API_URL}/html-to-pdf",
            json={},
            timeout=5
        )
        
        if response.status_code == 400:
            data = response.json()
            if "error" in data and "html" in data.get("details", "").lower():
                print_success(f"Correctly rejected empty request (Status: 400)")
                print_info(f"Error message: {data['details']}")
                return True
            else:
                print_error(f"Wrong error message")
                return False
        else:
            print_error(f"Expected 400, got {response.status_code}")
            return False
    except Exception as e:
        print_error(f"Test failed: {str(e)}")
        return False


def test_empty_html() -> bool:
    """Test error handling - empty HTML"""
    print_header("TEST 7: Error Handling - Empty HTML")
    
    try:
        response = requests.post(
            f"{API_URL}/html-to-pdf",
            json={"html": ""},
            timeout=5
        )
        
        if response.status_code == 400:
            data = response.json()
            print_success(f"Correctly rejected empty HTML (Status: 400)")
            print_info(f"Error message: {data['details']}")
            return True
        else:
            print_error(f"Expected 400, got {response.status_code}")
            return False
    except Exception as e:
        print_error(f"Test failed: {str(e)}")
        return False


def test_invalid_content_type() -> bool:
    """Test error handling - invalid Content-Type"""
    print_header("TEST 8: Error Handling - Invalid Content-Type")
    
    try:
        response = requests.post(
            f"{API_URL}/html-to-pdf",
            headers={"Content-Type": "text/plain"},
            data='{"html": "<html></html>"}',
            timeout=5
        )
        
        if response.status_code == 400:
            data = response.json()
            if "Content-Type" in data.get("error", "") or "Content-Type" in str(data):
                print_success(f"Correctly rejected invalid Content-Type (Status: 400)")
                print_info(f"Error: {data['error']}")
                return True
            else:
                print_warning(f"Got 400 but message may not mention Content-Type")
                return True
        else:
            print_error(f"Expected 400, got {response.status_code}")
            return False
    except Exception as e:
        print_error(f"Test failed: {str(e)}")
        return False


def test_invalid_json() -> bool:
    """Test error handling - invalid JSON"""
    print_header("TEST 9: Error Handling - Invalid JSON")
    
    try:
        response = requests.post(
            f"{API_URL}/html-to-pdf",
            headers={"Content-Type": "application/json"},
            data='not valid json',
            timeout=5
        )
        
        if response.status_code == 400:
            print_success(f"Correctly rejected invalid JSON (Status: 400)")
            return True
        else:
            print_error(f"Expected 400, got {response.status_code}")
            return False
    except Exception as e:
        print_error(f"Test failed: {str(e)}")
        return False


def test_nonexistent_route() -> bool:
    """Test error handling - non-existent route"""
    print_header("TEST 10: Error Handling - Non-existent Route")
    
    try:
        response = requests.get(
            f"{API_URL}/nonexistent",
            timeout=5
        )
        
        if response.status_code == 404:
            data = response.json()
            print_success(f"Correctly returned 404 for non-existent route")
            print_info(f"Error: {data.get('error')}")
            return True
        else:
            print_error(f"Expected 404, got {response.status_code}")
            return False
    except Exception as e:
        print_error(f"Test failed: {str(e)}")
        return False


def run_all_tests():
    """Run all tests"""
    print(f"\n{Colors.BOLD}{Colors.HEADER}")
    print("╔" + "="*78 + "╗")
    print("║" + " "*20 + "HTML to PDF Converter API - Test Suite" + " "*20 + "║")
    print("╚" + "="*78 + "╝")
    print(f"{Colors.ENDC}")
    
    # Check server health
    print_info(f"Testing API at: {API_URL}")
    if not check_server_health():
        print_error(f"Cannot connect to {API_URL}")
        print_warning("Make sure the API is running:")
        print_warning("  Local: python app.py")
        print_warning("  Docker: docker-compose up -d")
        sys.exit(1)
    
    print_success("Server is accessible\n")
    
    # Create output directory
    create_output_dir()
    
    # Run tests
    tests = [
        ("Health Check", test_health_endpoint),
        ("API Info", test_info_endpoint),
        ("Simple HTML", test_simple_html),
        ("HTML with Styling", test_html_with_styling),
        ("HTML with Table", test_html_with_table),
        ("Missing HTML Field", test_missing_html_field),
        ("Empty HTML", test_empty_html),
        ("Invalid Content-Type", test_invalid_content_type),
        ("Invalid JSON", test_invalid_json),
        ("Non-existent Route", test_nonexistent_route),
    ]
    
    results = {}
    for test_name, test_func in tests:
        try:
            results[test_name] = test_func()
        except Exception as e:
            print_error(f"Test crashed: {str(e)}")
            results[test_name] = False
    
    # Print summary
    print_header("TEST SUMMARY")
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    for test_name, result in results.items():
        status = f"{Colors.OKGREEN}PASS{Colors.ENDC}" if result else f"{Colors.FAIL}FAIL{Colors.ENDC}"
        print(f"  {status}  {test_name}")
    
    print(f"\n{Colors.BOLD}Results: {passed}/{total} tests passed{Colors.ENDC}\n")
    
    if passed == total:
        print_success("All tests passed! ✓")
        return 0
    else:
        print_error(f"{total - passed} test(s) failed")
        return 1


if __name__ == "__main__":
    exit_code = run_all_tests()
    sys.exit(exit_code)
