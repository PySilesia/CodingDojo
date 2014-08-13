#!/usr/bin/env python
# encoding: utf-8
"""
test_ocr.py

Tests source file for OCR Coding Dojo
"""

from nose.tools import *
from ocr import *

def test_none():
    res = ocrnum(None)
    assert_equals(res, None)
    
def test_is_str():
    res = ocrnum(69)
    assert_equals(res, "Err")
    
def test_not_12_lines():
    res = ocrnum('')
    assert_equals(res, "Err")
    
def test_ge_27x3_chars_in_line():
    res = ocrnum(('_' * 28*3 + '\n' ) * 11 + ('_' * 28*3))
    assert_equals(res, [["Err", "Err", "Err", "Err"], "Err"])

def test_le_27_chars_in_line():
    res = ocrnum(('_' * 7 + '\n') * 11 + ('_' * 7))    
    assert_equals(res, [["Err", "Err", "Err", "Err"], "Err"])
    
def test_valid_chars_in_line():
    res = ocrnum(('_' * 10 + '\n') * 11 + ('a' * 10))   
    assert_equals(res, [["Err", "Err", "Err", "Err"], "Err"])

def test_27x2():
    row = [
    ' _ '*27, 
    ' _|'*27, 
    '|_ '*27
    ]		
    res = ocrow(row)
    assert_equals(res, '2' * 27)

def test_27x8():
    row = [
    ' _ '*27, 
    '|_|'*27, 
    '|_|'*27
    ]		
    res = ocrow(row)
    assert_equals(res, '8' * 27)
    
def test_27x6():
    row = [
    ' _ '*27, 
    '|_ '*27, 
    '|_|'*27
    ]		
    res = ocrow(row)
    assert_equals(res, '6' * 27)

def test_27x9():
    row = [
    ' _ '*27, 
    '|_|'*27, 
    ' _|'*27
    ]		
    res = ocrow(row)
    assert_equals(res, '9' * 27)

def test_27x5():
    row = [
    ' _ '*27, 
    '|_ '*27, 
    ' _|'*27
    ]		
    res = ocrow(row)
    assert_equals(res, '5' * 27)

def test_27x3():
    row = [
    ' _ '*27, 
    ' _|'*27, 
    ' _|'*27
    ]		
    res = ocrow(row)
    assert_equals(res, '3' * 27)
    
def test_27x0():
    row = [
    ' _ '*27, 
    '| |'*27, 
    '|_|'*27
    ]		
    res = ocrow(row)
    assert_equals(res, '0' * 27)
    
def test_27x4():
    row = [
    '   '*27, 
    '|_|'*27, 
    '  |'*27
    ]		
    res = ocrow(row)
    assert_equals(res, '4' * 27)

def test_27x7():
    row = [
    '_ '*27, 
    ' |'*27, 
    ' |'*27
    ]		
    res = ocrow(row)
    assert_equals(res, '7' * 27)

def test_27x1():
    row = [
    '|'*27, 
    '|'*27, 
    '|'*27
    ]		
    res = ocrow(row)
    assert_equals(res, '1' * 27)
