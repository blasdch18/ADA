def bagproblem(w, wt, val, n): 
	bag = [[0 for x in range(w + 1)] for x in range(n + 1)] 

	for i in range(n + 1): 
		for w in range(w + 1): 
			if i == 0 or w == 0: 
				bag[i][w] = 0
			elif wt[i-1] <= w: 
				bag[i][w] = max(val[i-1] + bag[i-1][w-wt[i-1]], bag[i-1][w]) 
			else: 
				bag[i][w] = bag[i-1][w] 

	return bag[n][w] 

w = 7
val = [1, 4, 6] 
wt = [1, 6, 8]
n = len(val)
 
print(bagproblem(w, wt, val, n)) 