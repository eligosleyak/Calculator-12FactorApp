"""
Test configuration file for the Calculator API.
This file sets up the Python path to ensure tests can import the application modules correctly.
"""

import os
import sys

# Add the project root directory to Python path
# This ensures that the app package can be imported during testing
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
