def decomposer(n): 
    p = [0] * n      
    k = 0         
    p[k] = n     
                
    while True:         
            print(p) 
  
            rem_val = 0
            while k >= 0 and p[k] == 1: 
                rem_val += p[k] 
                k -= 1
  
            if k < 0: 
                #print() 
                return
  
            p[k] -= 1
            rem_val += 1
  
            while rem_val > p[k]: 
                p[k + 1] = p[k] 
                rem_val = rem_val - p[k] 
                k += 1
  
            p[k + 1] = rem_val 
            k += 1

num=5
print( str(num) + ' . . . ') 
decomposer(num)             