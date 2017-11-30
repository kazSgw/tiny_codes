def getFaceAmount(lst): # lst must be a STRING list
    amount = 0
    
    for i in range(10):
        child_lst = [x for x in lst if str(i)==x[0] ]
        if not child_lst:
            continue
        elif len(child_lst[0]) == 2:
            amount += 1
        else:
            amount += getFaceAmount( [ x[1:] for x in child_lst ] )

    return amount + 1
        
