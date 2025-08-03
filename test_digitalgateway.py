# test_digitalgateway.py
"""
Tests for DigitalGateway module.
"""

import unittest
from digitalgateway import DigitalGateway

class TestDigitalGateway(unittest.TestCase):
    """Test cases for DigitalGateway class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DigitalGateway()
        self.assertIsInstance(instance, DigitalGateway)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DigitalGateway()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
