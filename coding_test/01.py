import numpy as np
import os
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def get_input() :
	length = int(input())
#	if length < 6 or length > 80000 :
#		assert()
		
	input_arr = []
	for i in range(length) :
		dat = int(input())
#		if(dat < 1 or dat > 1000000000) :
#			assert()
		input_arr.append(dat)
	
	return length, input_arr


if __name__ == '__main__' :
	length, input_arr = get_input()
	
	dat = input_arr[0]
		
	sum_data = 0

	stack = []
	stack2 = []
	
	sum_v = 0
	
	dat = input_arr[0]
	k = 0
	count = 0
	sums = 0

	sp = 0
	for i in range(length) :
		while sp > 0 : 
			if input_arr[i] < stack2[-1] :
				break
			else :
				stack2.pop()
				sp = sp - 1
		sums += sp
		stack2.append(input_arr[i])
		print(sums, stack2)
		sp = sp + 1
#		print(i, stack2)
#		sp = len(stack2) - 1
	print(sums)
'''	
	for i in range(length-1) :
		dat = input_arr[i]
		count = 0
		k = i+1
		while k<length :
			if dat <= input_arr[k] :
				break
			else :
				count = count + 1
				k = k + 1
#				if k == length :
#					break

		sum_data = sum_data + count

	print(sum_data)
'''