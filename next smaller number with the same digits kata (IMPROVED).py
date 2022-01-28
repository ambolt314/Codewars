def next_smaller(n):
    
    if n < 10:
        return -1
    if type(n) is not int:
        return -1
    
    
    left = [int(d) for d in str(n)] # unsorted half
    right = [] # sorted half
    
    digits = len(left)

    # Split number into sorted and unsorted halves
    right.append(left.pop())
    while(left[-1] <= right[-1]):
        right.append(left[-1])
        left.pop()
        
        # number is its lowest value
        if len(left) == 0:
            return -1
    
    tmpL = left[-1]
    
    # Find the greatest number strictly less than tmpL
    tmpR = tmpL
    indexR = 0
    
    right.sort(reverse=True)
    
    for i in range(len(right)):
        if right[i] < tmpR:
            tmpR = right[i]
            indexR = i
            break
        else:
            continue
    
    # Swap tmpL and tmpR
    left[-1] = tmpR
    right[indexR] = tmpL
    
    # reverse sort right
    right.sort(reverse=True)
        
    # generate a number from the arrays
    output_array = []
    
    for item in left:
        output_array.append(item)
    for item in right:
        output_array.append(item)
        
    output = int("".join(map(str, output_array)))
    
    # numbers with leading zeros have unequal digits to the starting number
    if len(str(output)) != len(str(n)):
        return -1
    
    return output
        