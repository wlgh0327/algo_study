# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def find_index(data, target) :
	res = []
	lis = data
	while True :
		try :
			res.append(lis.index(target) + (res[-1]+1 if len(res) != 0 else 0))
			lis = data[res[-1]+1:]
		except :
			break
	return res

def get_used_color(data) :
	used_color = []
	for c_idx in range(1, 10) :
		for i in range(len(data)) :
			index_arr = find_index(data[i], c_idx)
			if index_arr :
				used_color.append(c_idx)
				break
	return used_color

def check_overlap(input_arr, color_arr, use_color_num, color_idx, color_map) :
	color_data = use_color_num[color_idx]
	y_arr = []
	x_arr = []
	for i in range(len(color_arr)) :
		y = color_arr[i][0]
		x = color_arr[i][1]
#		print(input_arr[y][x])
		y_arr.append(y)
		x_arr.append(x)

	y_min = min(y_arr)
	y_max = max(y_arr)
	x_min = min(x_arr)
	x_max = max(x_arr)
#	print(color_arr)
#	print(use_color_num[color_idx], y_min, y_max, x_min, x_max)

	overlap = False
	for j in range(y_min, y_max + 1) :
		for i in range(x_min, x_max + 1) :
			val = input_arr[j][i]
			if val != use_color_num[color_idx] :
				overlap = True
				color_map[val] += 1
	
	return color_map


length = int(input())

input_arr = []
for i in range(length) :
	user_input = input()
	
	arr = []
	for j in range(length) :
		arr.append(int(user_input[j]))
	
	input_arr.append(arr)

use_color = get_used_color(input_arr)

color_map = []
for i in range(10) :
	color_map.append(0)
for used in use_color :
	color_map[used] = 1


color_arr = []

#count = 0
for c in range(len(use_color)) :
	for i in range(len(input_arr)) :
		index_arr = find_index(input_arr[i], use_color[c])
		for j in range(len(index_arr)) :
			color_arr.append([i, index_arr[j]])	
	color_map = check_overlap(input_arr, color_arr, use_color, c, color_map)

	color_arr.clear()
	color_arr = []

count = 0
for cnt in color_map :
	if cnt == 1 :
		count = count + 1

res = count	
#res = len(use_color) - count
print(res)
