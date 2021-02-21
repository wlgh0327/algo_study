# DFS
import sys
sys.setrecursionlimit(100000)

max_int = 100000

DEBUG = False

def mprint(args, debug_flag=DEBUG) :
	if DEBUG is True :
		print(args)
	return

length = int(input())


cost_map = []
for i in range(length) :
	cost_arr = []
	for j in range(length) :
		cost_arr.append(max_int)
	cost_map.append(cost_arr)



def get_input() :	
	input_arr = []
	for i in range(length) :
		user_input = input()

		arr = []
		for j in range(length) :
			arr.append(int(user_input[j]))

		input_arr.append(arr)
	return input_arr

def print_full_map(arr, size) :
	mprint('========')
	for i in range(size) :
		mprint(arr[i])
	mprint('========')
	return

print_full_map(cost_map, length)

minimum_cost = max_int

def sol(arr, size, row, col, cost) :

	if row < 0 or row >= size or col < 0 or col >= size :
		return
	
	if row == size - 1 and col == size - 1 :
		mprint('final cost : {}'.format(cost))
		global minimum_cost
		minimum_cost = min(minimum_cost, cost)
		return

	if cost_map[row][col] <= cost :
		return
	
	mprint('row {} col {} val {}'.format(row, col, arr[row][col]))
	
	cost += arr[row][col]
	mprint('cost : {}'.format(cost))
	
	cost_map[row][col] = cost
	#input()
	
	sol(arr, size, row-1, col, cost)
	sol(arr, size, row, col-1, cost)
	sol(arr, size, row+1, col, cost)
	sol(arr, size, row, col+1, cost)
	return


if __name__ == '__main__' :
	input_arr = get_input()
#	mprint(input_arr)
	print_full_map(input_arr, length)
	
	sol(input_arr, length, 0, 0, 0)
	
	print(minimum_cost)
	
	