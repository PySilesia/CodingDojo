#!/usr/bin/env python
# encoding: utf-8
"""
test_roman.py

Tests source file for Roman Coding Dojo
"""

from nose.tools import *
from roman import a2r

def test_none():
    res = a2r(None)
    assert_equals(res, None)
    
def test_empty_list():
    res = a2r([])
    assert_equals(res, [])

def test_non_list():
    res = a2r("Palid")
    assert_equals(res, None)

def test_negative():
    res = a2r([-1])
    assert_equals(res, ["NaN"])

def test_zero():
    res = a2r([0])
    assert_equals(res, ["NaN"])
    
def test_over_3000():
    res = a2r([3001])
    assert_equals(res, ["NaN"])
    
def test_is_string():
    res = a2r(["whatever"])
    assert_equals(res, ["Err"])
    
def test_1():
    res = a2r([1])
    assert_equals(res, ['I'])
    
def test_1000():
    assert_equals(a2r([1000]), ['M'])
    
def test_500():
    assert_equals(a2r([500]), ['D'])
    
def test_100():
    assert_equals(a2r([100]), ['C'])

def test_50():
    assert_equals(a2r([50]), ['L'])
    
def test_10():
    assert_equals(a2r([10]), ['X'])

def test_5():
    assert_equals(a2r([5]), ['V'])
    
def test_2():
    assert_equals(a2r([2]), ['II'])
    
def test_4():
    assert_equals(a2r([4]), ["IV"])

def test_1800():
    assert_equals(a2r([1800]), ["MDCCC"])