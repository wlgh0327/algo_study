# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

import numpy as np

DEBUG = False
MAX_INT = 1e6

def mprint(args, flag=DEBUG) :
	if flag is True :
		print(args)
	return

def mprint_arr(length, arr, flag=DEBUG) :
	if flag is True :
		for i in range(length) :
			print(arr[i])
	
	return



if __name__ == '__main__' :
	first_input = input()
	inputs = first_input.split(' ')
	factory_num = int(inputs[0])
	road_num = int(inputs[1])
	
	mprint('factory_num : {}, road_num : {}'.format(factory_num, road_num))

	input_arr = []
	
	for i in range(road_num) :
		user_input = input()

		user_ = user_input.split(' ')
		arr_ = []
		for j in range(3) :
			arr_.append(int(user_[j]))
		input_arr.append(arr_)
	mprint_arr(road_num, input_arr)
	
	
	arr = np.zeros((factory_num, factory_num), dtype=np.int32)
	
	for data in input_arr :
		arr[data[0]-1][data[1]-1] = data[2]
		arr[data[1]-1][data[0]-1] = data[2]

	mprint(arr)
	for j in range(factory_num) :
		for i in range(factory_num) :
			if j == i :
				continue
			else :
				if arr[j][i] == 0 :
					arr[j][i] = MAX_INT
					
	mprint_arr(factory_num, arr)
	
	for k in range(factory_num) :
		for s in range(factory_num) :
			for e in range(factory_num) :
				if arr[s][e] > arr[s][k] + arr[k][e] :
					arr[s][e] = arr[s][k] + arr[k][e]

	max_arr = []
	for i in range(factory_num) :
		max_var = max(arr[i])
		max_arr.append(max_var)

	mprint_arr(factory_num, arr)
	
	print(min(max_arr))