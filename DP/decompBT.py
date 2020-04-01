import copy as cp


def degloser(n):
    numbers=[]
    for i in range(1,n+1):
        numbers.append(i)        
    return numbers

def decomposer(decomposed, remaining, valid_numbers):
    #base case
    
    if remaining == 0:
        return decomposed
    #find all valid subtractions
    else:
        ans = []
        for number in valid_numbers:
            if remaining - number >= 0:
                new_decomposed = cp(decomposed)
                new_decomposed.append(number)
                cand = decomposer(new_decomposed,remaining-number,valid_numbers)
                if cand:
                    ans.append(cand)
        if len(ans) > 0:
            return ans
         

nn=5
print(decomposer([],nn,degloser(nn)))