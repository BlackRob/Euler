def genOrderedPerms(lcr,perms,p_in): 
    """ generate ordered permutations by splitting 
    lcr = list of characters remaining
    the idea is given a list of characters, the set of all possible
    permutations of those characters can be split into len(lcr) subsets,
    each starting with a particular character, for example, if our characters
    are a,b,c,d, our set of permutations can be split into sets starting with
    a, starting with b, etc.  Each subset can be treated exactly as the 
    original set, except one character has been removed from the lcr.
    If we operate recursively, we can create all permutations in order,
    or even just count them, as in this case where we only care about a 
    particular permutation (the millionth) """
    
    global j    # our counter
    global p    # length of perms list, doesn't change
    
    depth = p - p_in
    
    #if j == 15: # when we have counted this high we are done
    #    print(perms)
    #    return
    
    
    for i in range(p_in):
        llcr = list(lcr)  # list of local characters remaining
        #print('depth = ',str(depth),' i = ',i,' ',p_in,' ',str(len(lcr)))
        perms[depth] = llcr[i]
        del llcr[i] 
        if len(llcr) == 0:
            j += 1
            if j == 1000000:
                print(perms,j)
                break
            return 
        genOrderedPerms(llcr,perms,p_in-1)
        

j       = 0 # generated permutation counter
perms   = [0,0,0,0,0,0,0,0,0,0]
p       = len(perms)
cars = ['0','1','2','3','4','5','6','7','8','9']

genOrderedPerms(cars,perms,p)


print(perms,j)
