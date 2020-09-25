import csv
import sys

def knapSack(W, wt, val, n): 
	K = [[0 for x in range(W + 1)] for x in range(n + 1)] 

	# Build table K[][] in bottom up manner 
	for i in range(n + 1): 
		for w in range(W + 1): 
			if i == 0 or w == 0: 
				K[i][w] = 0
			elif wt[i-1] <= w: 
				K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w]) 
			else: 
				K[i][w] = K[i-1][w] 

	return K[n][W] 

if __name__ == '__main__':
	W = int(sys.argv[1])

	with open('knapsack.csv', 'r', encoding = 'utf-8') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0

		for row in csv_reader:
			if line_count == 0:
				val = [int(item) for item in row]
				line_count += 1
			else:
				wt = [int(item) for item in row]

	n = len(val)
	result = knapSack(W,wt,val,n)
	print(result)
