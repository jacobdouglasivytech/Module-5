# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 10:39:24 2023

@author: jacob
"""

import unittest
class TestSum(unittest.TestCase):
    
    def test_sum(self):
        self.assertEqual(sum([1,2,3]), 6, "Should be 6")
        
    def test_sum_tuple(self):
        self.assertEqual(sum((1,2,2)), 6, "Should be 6")
        
if __name__ == "__main__":
    unittest.main()
    