import numpy  as py


def coins (x , A , n):
	if n==0:
		return 1
	if n<0:
		return 0
	if A<=0 and n >=1:
		return 0

	j=coins (x , A-1 , n)
	print("j=",j ," a=", A ," n=",n)
	print("__________")
	k=coins (x ,A, n-x[A-1])	
	print("k=",k ," a=", A ," n=",n)
	print("----------")
	return  j+k ;
	#return j;

arr = [1,2,5]
a = len(arr)
print ("-->",coins(arr, a,5))