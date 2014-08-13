#!/usr/bin/env python
# encoding: utf-8
"""
ocr.py

Solution source file for OCR Coding Dojo

    _  _     _  _  _  _  _
  | _| _||_||_ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _| 
    _  _     _  _  _  _  _
  | _| _||_||_ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _| 
    _  _     _  _  _  _  _
  | _| _||_||_ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _| 
    _  _     _  _  _  _  _  _
  | _| _||_||_ |_   ||_||_|| |
  ||_  _|  | _||_|  ||_| _||_|

Input:
  * 4 rows with number of 27 digits to OCR                           
  * None -> None
  * Invalid string or else -> "Err"

Output:
  [[str_number1,str_number2,str_number3,str_number4],status]
    
   status:
   "OK"
   "Part"
   "Err"
Example:   
[["123456789","123456789","123456789","123456789"],"OK"]    
[["123456789","123456789","Err","123456789"],"Part"]    
[["Err","Err","Err","Err"],"Err"]    
"""

numbers = [
	[
	' _ ',
	' _|',
	'|_ '
	],
	[
	' _ ',
	'|_|',
	'|_|'
	],
	[
	' _ ',
	'|_ ',
	'|_|'
	],
	[
	' _ ',
	'|_|',
	' _|'
	],
	[
	' _ ',
	'|_ ',
	' _|'
	],
	[
	' _ ',
	' _|',
	' _|'
	],
	[
	' _ ',
	'| |',
	'|_|'
	],
	[
	'   ',
	'|_|',
	'  |'
	],
	[
	'_ ',
	' |',
	' |'
	],	
	[
	'|',
	'|',
	'|'
	]
]



import re


def ocrnum(scan):
	if scan is None:
		return None
	if not isinstance(scan, str):
		return "Err"
		
	lines = scan.split('\n')
	if len(lines) != 12:
		return "Err"
		
	result = [[], ""]
		
	for line in lines:
		if len(line) > 27 * 3:
			result[0] = ["Err" for i in range(4)]
			result[1] = "Err"
			return result
		elif len(line) < 27:
			result[0] = ["Err" for i in range(4)]
			result[1] = "Err"
			return result
		if not re.match(line, "_ \|"):
			result[0] = ["Err" for i in range(4)]
			result[1] = "Err"
			return result
			
def ocrow(row):
	nums = ''
	offset = len(row[0])
	
	i = 0
	while i < offset:
		digit = [
			row[0][i: i + 3],
			row[1][i: i + 3],
			row[2][i: i + 3]
		]
		if digit == numbers[0]:
			nums += '2'
			i += 3
		elif digit == numbers[1]:
			nums += '8'
			i += 3
		elif digit == numbers[2]:
			nums += '6'
			i += 3
		elif digit == numbers[3]:
			nums += '9'
			i += 3
		elif digit == numbers[4]:
			nums += '5'
			i += 3
		elif digit == numbers[5]:
			nums += '3'
			i += 3
		elif digit == numbers[6]:
			nums += '0'
			i += 3
		elif digit == numbers[7]:
			nums += '4'
			i += 3
		else:
			digit = [
			row[0][i: i + 2],
			row[1][i: i + 2],
			row[2][i: i + 2]
			]
			if digit == numbers[8]:
				nums+="7"
				i+=2
			else:
				digit = [
				row[0][i: i + 1],
				row[1][i: i + 1],
				row[2][i: i + 1]
				]
				if digit == numbers[9]:
					nums+="1"
					i+=1
				else:
					return "Err"
	return nums