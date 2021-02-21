# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def char2integer(char) :
	if char == 'A' :
		return 10
	elif char == 'B' :
		return 11
	elif char == 'C' :
		return 12
	elif char == 'D' :
		return 13
	elif char == 'E' :
		return 14
	elif char == 'F' :
		return 15
	elif char == 'G' :
		return 16
	elif char == 'H' :
		return 17
	elif char == 'I' :
		return 18
	elif char == 'J' :
		return 19
	elif char == 'K' :
		return 20
	elif char == 'L' :
		return 21
	elif char == 'M' :
		return 22
	elif char == 'N' :
		return 23
	elif char == 'O' :
		return 24
	elif char == 'P' :
		return 25
	elif char == 'Q' :
		return 26
	elif char == 'R' :
		return 27
	elif char == 'S' :
		return 28
	elif char == 'T' :
		return 29
	elif char == 'U' :
		return 30
	elif char == 'V' :
		return 31
	elif char == 'W' :
		return 32
	elif char == 'X' :
		return 33
	elif char == 'Y' :
		return 34
	elif char == 'Z' :
		return 35	
	else :
		return int(char)

def integer2char(number) :
	if number == 10 :
		return 'A'
	elif number == 11 :
		return 'B'
	elif number == 12 :
		return 'C'
	elif number == 13 :
		return 'D'
	elif number == 14 :
		return 'E'
	elif number == 15 :
		return 'F'
	elif number == 16 :
		return 'G'
	elif number == 17 :
		return 'H'
	elif number == 18 :
		return 'I'
	elif number == 19 :
		return 'J'
	elif number == 20 :
		return 'K'
	elif number == 21 :
		return 'L'
	elif number == 22 :
		return 'M'
	elif number == 23 :
		return 'N'
	elif number == 24 :
		return 'O'
	elif number == 25 :
		return 'P'
	elif number == 26 :
		return 'Q'
	elif number == 27 :
		return 'R'
	elif number == 28 :
		return 'S'
	elif number == 29 :
		return 'T'
	elif number == 30 :
		return 'U'
	elif number == 31 :
		return 'V'
	elif number == 32 :
		return 'W'
	elif number == 33 :
		return 'X'
	elif number == 34 :
		return 'Y'
	elif number == 35 :
		return 'Z'
	else :
		return str(number)


def is_negative(string) :
	first = string[0]
	if first == '-' :
		return True
	else :
		return False

def str2int(dec, data) :
	data_length = len(data)
	data_arr = []
	for i in range(len(data)) :
		d = char2integer(data[i])
		d *= dec ** (data_length - 1 - i)
		data_arr.append(d)

	return data_arr

def multiply(dat1, dat2) :
	a = 0
	b = 0
	mul = 0
	for j in range(len(dat2)-1, -1, -1) :
		d2 = int(dat2[j])
		for i in range(len(dat1)) :
			d1 = int(dat1[i])
			mul += d1 * d2
		
		a += mul
		mul = 0
	
	return a

def convert(n, dec) :
	T = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	q, r = divmod(n, dec)
	if q == 0 :
		return T[r]
	else :
		return convert(q, dec) + T[r]


length = int(input())

input_arr = []
negative_arr = []
for i in range(length) :
	inputs = input()
	split_inputs = inputs.split(' ')
	a = is_negative(split_inputs[1])
	b = is_negative(split_inputs[2])
	
	if a is True :
		split_inputs[1] = split_inputs[1][1:]
	if b is True :
		split_inputs[2] = split_inputs[2][1:]
		
	input_arr.append(split_inputs)
	negative_arr.append([a, b])


for i in range(len(input_arr)) :
	data = input_arr[i]
	neg1 = negative_arr[i][0]
	neg2 = negative_arr[i][1]
	dec = int(data[0])
	data[0] = dec
	
	dat1 = str2int(dec, data[1])
	dat2 = str2int(dec, data[2])

	res = multiply(dat1, dat2)
	final = convert(res, dec)
	
	if res != 0 :
		if neg1 is True and neg2 is False :
			final = '-' + final
		if neg1 is False and neg2 is True :
			final = '-' + final
	
	print(final)
