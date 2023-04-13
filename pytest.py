# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 10:47:37 2023

@author: jacob
"""

def test_sum():
    assert sum([1,2,3]) == 6, "Should be 6"
    
def test_sum_tuple():
    assert sum((1,2,2)) == 6, "Should be 6"
    
    