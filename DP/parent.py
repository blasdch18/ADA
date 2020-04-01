
res = {}

def recurser(s, index, leftcounter, rightcounter, leftremover, rightremover, express): 

		if index == len(s):
			if leftremover == 0 and rightremover == 0:
				answer = "".join(express)
				res[answer] = 1
		else:
			if(s[index] == '(' and leftremover>0) or (s[index] == ')' and rightremover>0):
				recurser(s, index+1, leftcounter,rightcounter, 
					     leftremover - (s[index] == '('), rightremover - (s[index] ==')'), 
					     express)

			express.append(s[index])
			if s[index] != '(' and s[index] != ')':

				recurser(s, index+1, leftcounter, rightcounter, 
					     leftremover, rightremover, 
					     express)

			elif s[index] == '(':

				recurser(s, index + 1, leftcounter + 1, rightcounter,
					     leftremover, rightremover,
					     express)

			elif s[index] == ')' and leftcounter > rightcounter:
				
				recurser(s, index+1, leftcounter, rightcounter+1,
						 leftremover, rightremover, 
						 express)

			express.pop()
def remover(s):
	left = 0
	right = 0
	
	for i in s: # misplaced left and right parentheses

		if i =='(':
			left+=1
		elif i ==')':
			right+=1 if left == 0 else right

			left -=1 if left > 0 else left

	recurser(s,0,0,0,left, right, [])
	return list(res.keys())


exp = "())"

print(remover(exp))