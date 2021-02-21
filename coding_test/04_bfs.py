# BFS
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

def sol(arr, size) :
	
	queue = []
	
	queue.append((0, 0, 0))
	cost_map[0][0] = 0
	
	rr = [-1, 1, 0, 0]
	cc = [0, 0, -1, 1]
	
	while(len(queue) > 0) :
		cur_row, cur_col, cur_cost = queue.pop(0)
		for i in range(4) :
			next_row = cur_row + rr[i]
			next_col = cur_col + cc[i]
			
			if next_row < 0 or next_row >= size or next_col < 0 or next_col >= size :
				continue
			
			next_cost = cur_cost + arr[next_row][next_col]
			if cost_map[next_row][next_col] > next_cost :
				cost_map[next_row][next_col] = next_cost
				queue.append((next_row, next_col, next_cost))
				mprint('queue : {}'.format(queue))
				mprint('row {} col {}, nrow {}, ncol {}, cost {}, ncost {}'.format(cur_row, cur_col, next_row, next_col, cur_cost, next_cost))
				#input()
	
	return


if __name__ == '__main__' :
	input_arr = get_input()
#	mprint(input_arr)
	print_full_map(input_arr, length)
	
	sol(input_arr, length)
	
	print_full_map(cost_map, length)
	
	print(cost_map[length-1][length-1])
	#print(minimum_cost)
	
	