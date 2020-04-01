s='())'

right=0
left=0
for i in s:

		if i =='(':
			left+=1
		elif i ==')':
			right+=1 if left == 0 else right 

			left +=2 if left > 0 else left
		print left ,right
		#print left		
