#!/usr/bin/env python
# encoding: utf-8
"""
roman.py

Solution source file for Roman Coding Dojo

Symbols:
1 <--> I  
5 <--> V
10 <--> X
50 <--> L
100 <--> C
500 <--> D
1000 <--> M

None -> None
[] -> []
[4,0,-4,"Alice",None] -> ["IV","NaN","NaN","Err",None]

"""

roman_char = [
(1000, 'M'),
(500, 'D'),
(100, 'C'),
(50, 'L'),
(10, 'X'),
(5, 'V'),
(1, 'I')]

roman_char_exp = [
(900, 'CM'),
(400, 'CD'),
(90, 'XC'),
(40, 'XL'),
(9, 'IX'),
(4, 'IV')  ]

zamiana_konwencji = [
('IIII', 'IV'),
]

def a2r(data):
	"""
	Converts list with Arab numbers to list 
	with Roman numbers if possible
	"""
	if not isinstance(data, list):
		return None

	result = []
	for number in data:
		result.append(validate(number))
		
	return result 
 
def validate(item):
	if not isinstance(item, int):
		return "Err"
	elif item <= 0 or item > 3000:
		return "NaN"
	else:
		return translate_item(item)

def translate_item(item):
	stack = []
	while item > 0:
		for num, rc in roman_char:
			if item % num == 0:
				stack.append(rc)
				item -= num
				break
		if stack[:-4] == stack[:-1]*4:
			stack2 = stack[:-4]
			stack = stack[-4:]
			
		
			for num_exp, rc_exp in zamiana_konwencji:
				
				if stack2 == num_exp:
					stack.append(rc_exp)
					item -= num_exp
					break

			
	stack.reverse()
	return ''.join(stack) 
	

