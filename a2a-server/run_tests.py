#!/usr/bin/env python3
"""
Test Runner for A2A Text Analysis Agent

This script runs the comprehensive test suite for the A2A text analysis agent,
including unit tests, integration tests, and protocol compliance tests.
"""

import os
import sys
import subprocess
from pathlib import Path

# Add the src directory to the Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))


def run_tests(test_type: str = "all", coverage: bool = False, verbose: bool = False):
    """
    Run the test suite.
    
    Args:
        test_type (str): Type of tests to run ("all", "unit", "integration")
        coverage (bool): Whether to run with coverage reporting
        verbose (bool): Whether to run with verbose output
    """
    # Base pytest command
    cmd = ["python", "-m", "pytest"]
    
    # Add coverage if requested
    if coverage:
        cmd.extend(["--cov=src/a2a_text_analysis_agent", "--cov-report=html", "--cov-report=term"])
    
    # Add verbose flag if requested
    if verbose:
        cmd.append("-v")
    
    # Add test path based on type
    if test_type == "unit":
        cmd.append("tests/unit/")
    elif test_type == "integration":
        cmd.append("tests/integration/")
    else:  # all
        cmd.append("tests/")
    
    print(f"Running {test_type} tests...")
    print(f"Command: {' '.join(cmd)}")
    
    # Run the tests
    result = subprocess.run(cmd, cwd=Path(__file__).parent)
    
    if result.returncode == 0:
        print(f"\n✅ {test_type.title()} tests passed!")
    else:
        print(f"\n❌ {test_type.title()} tests failed!")
        sys.exit(1)


def main():
    """Main entry point for the test runner."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Run A2A Text Analysis Agent tests")
    parser.add_argument(
        "--type", 
        choices=["all", "unit", "integration"], 
        default="all",
        help="Type of tests to run"
    )
    parser.add_argument(
        "--coverage", 
        action="store_true",
        help="Run with coverage reporting"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Run with verbose output"
    )
    
    args = parser.parse_args()
    
    print("🧪 A2A Text Analysis Agent Test Suite")
    print("=" * 50)
    
    run_tests(args.type, args.coverage, args.verbose)


if __name__ == "__main__":
    main() 