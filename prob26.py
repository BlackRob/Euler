def schlong_division(x):
    i = 0
    j = 1
    rem = 1
    dividend = x
    unifrac = 0.0
    remainders =[]
    while (True):
        step = rem*10//dividend
        #print(step)
        rem = rem*10 - step*dividend
        #print(rem)
        unifrac += step/(10**j)
        #print(x,unifrac)
        
        #print('*'*20)
        
        if rem in remainders:
            #print(unifrac,', recurring cycle for ',x,' is ',i, 'digits')
            return i
            
        remainders.append(rem)
        if rem == 0.0:
            #print(unifrac,', 1 /',x,"doesn't repeat")
            return i
        j += 1
        i += 1
        

x = 0
y = 0
yi = 0

for i in range(2,1000):
    x = schlong_division(i)
    if x > y:
        y = x
        yi = i

print(yi,y)
    