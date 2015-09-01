# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 19:02:54 2015

@author: laurence
"""
import unittest
from ci_test.parens_match import parens_match

def test_pairs_match():
    matching = '[]{}(){({()})}'
    assert parens_match(matching)
    
def test_mismatch():
    dont_match = '[()[]}'
    assert not parens_match(dont_match)

if __name__ == '__main__':
    unittest.main()