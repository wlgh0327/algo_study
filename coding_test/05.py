import sys
sys.setrecursionlimit(100000)
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
DEBUG = True
MAX_INT = 1e6

def mprint(args, debug=DEBUG) :
	if debug is True :
		print(args)
	return


def mprint_arr(arr, length, debug=DEBUG) :
	if debug is True :
		print('=========')
		for i in range(length) :
			print(arr[i])
		print('=========')
	return

def get_input() :
	user_input = input()
	N = int(user_input)
	
	
	input_arr = []
	for j in range(N) :
		arr = []
		user_input = input()
		inputs = user_input.split(' ')
		for i in range(2) :
			arr.append(int(inputs[i]))
		input_arr.append(arr)
	
	
	return N, input_arr


if __name__ == '__main__' :
	
	length, input_arr = get_input()
	
	mprint('length : {}'.format(length))
	mprint_arr(input_arr, length)
	