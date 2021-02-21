import sys
sys.setrecursionlimit(100000)
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
DEBUG = False
MAX_INT = 1e6

def mprint(args, debug=DEBUG) :
	if debug is True :
		print(args)
	return


def mprint_arr(arr, row, col, debug=DEBUG) :
	if debug is True :
		print('=========')
		for i in range(row) :
			print(arr[i])
		print('=========')
	return

def get_input() :
	user_input = input()
	inputs = user_input.split(' ')
	N = int(inputs[0])
	M = int(inputs[1])
	
	mprint('N : {}, M : {}'.format(N, M))
	
	input_arr = []
	for j in range(N) :
		arr = []
		user_input = input()
		inputs = user_input.split(' ')
		for i in range(M) :
			arr.append(int(inputs[i]))
		input_arr.append(arr)
	
	
	return N, M, input_arr

factory_arr = []
def floodfill(arr, cost_arr, row_num, col_num, row, col, count, f_idx) :
	mprint('row : {}, col : {}'.format(row, col))
	mprint('count : {}'.format(count))	
	if row < 0 or row >= row_num or col < 0 or col >= col_num :
		return
	
	if cost_arr[row][col] != MAX_INT :
		return
	
	if arr[row][col] == 1 :
		count = count + 1
		arr[row][col] = 0
		factory_arr.append([f_idx, row, col])
	else :
		return
				

	
	cost_arr[row][col] = 0
	
	floodfill(arr, cost_arr, row_num, col_num, row-1, col, count, f_idx)
	floodfill(arr, cost_arr, row_num, col_num, row+1, col, count, f_idx)
	floodfill(arr, cost_arr, row_num, col_num, row, col-1, count, f_idx)
	floodfill(arr, cost_arr, row_num, col_num, row, col+1, count, f_idx)
	
	return
	
if __name__ == '__main__' :
	row_num, col_num, input_arr = get_input()
	
	cost_map = []
	for i in range(row_num) :
		cost_arr = []
		for j in range(col_num) :
			cost_arr.append(MAX_INT)
		cost_map.append(cost_arr)

	mprint_arr(input_arr, row_num, col_num)
	
	
	factory_arr = []
	
	factory_idx = 0
	idx_list = []
	rr = [-1, 1, 0, 0]
	cc = [-1, 1, 0, 0]
	
	found_value = False
	for k in range(2) :
		for j in range(row_num) :
			for i in range(col_num) :
				if input_arr[j][i] == 1 :
					found_value = True
					floodfill(input_arr, cost_map, row_num, col_num, j, i, 0, k)
					break
			if found_value is True :
				found_value = False
				break
			


	mprint_arr(input_arr, row_num, col_num)
	mprint(factory_arr)
	
	l1_factory = []
	l2_factory = []
	
	for data in factory_arr :
		if data[0] == 0 :
			l1_factory.append(data)
		else :
			l2_factory.append(data)
			
	min_length = MAX_INT
	for l1_dat in l1_factory :
		for l2_dat in l2_factory :
			l1_y = l1_dat[1]
			l1_x = l1_dat[2]
			l2_y = l2_dat[1]
			l2_x = l2_dat[2]
			
			dist = abs(l1_y - l2_y) + abs(l1_x - l2_x) - 1
			if min_length > dist :
				min_length = dist
	print(min_length)
	


