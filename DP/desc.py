from copy import copy
new_decomposed = []
def recurse_find(decomposed,remaining,valid_numbers):
    #base case
    if remaining == 0:
        return decomposed
    #find all valid subtractions
    else:
        ans = []
        for number in valid_numbers:
            if remaining - number >= 0:
                #copy(decomposed)
                new_decomposed.append(number)
                cand = recurse_find(new_decomposed,remaining- 
                              number,valid_numbers)
                if cand:
                    ans.append(cand)
        if len(ans) > 0:
            return ans
print(recurse_find([],5,[1,2,3,4,5]))