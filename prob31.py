#1 from 1p (1)
#2 from 2 1p or 1 2p (2)
#3 from 2p1p or 3 1p (2)
#4 from 2p2p, 2p1p1p, 4 1p (3)
#5 from 5, 5 1p, or 6 comb of 2,3 (4)
#10 from 10, 2 5, 
#22
#211
#1111

#5
#11111
#2111
#221

#10
#55
#5221
#52111
#511111
#22111111
#2111111111
#11111111111

def replace(coins,x):
    global n
    global combos
    print(coins)
    if x == 200:
        while 200 in coins:
            coins.remove(200)
            coins.append(100)
            coins.append(100)
            n += 1
            while 100 in coins:
                replace(coins,100)
    if x == 100:
        while 100 in coins:
            coins.remove(100)
            coins.append(50)
            coins.append(50)
            n += 1
            while 50 in coins:
                replace(coins,50)
    if x == 50:
        while 50 in coins:
            coins.remove(50)
            coins.appens(20)
            coins.append(20)
            coins.append(10)
            n += 1
            while 20 in coins:
                replace(coins,20)
            while 10 in coins:
                replace(coins,10)
    if x == 20:
        while 20 in coins:
            coins.remove(20)
            coins.appens(10)
            coins.append(10)
            n += 1
            while 10 in coins:
                replace(coins,10)
    if x == 10:
        while 10 in coins:
            coins.remove(10)
            coins.appens(5)
            coins.append(5)
            n += 1
            while 5 in coins:
                replace(coins,5)
    if x == 50:
        while 50 in coins:
            coins.remove(50)
            coins.appens(20)
            coins.append(20)
            coins.append(10)
            n += 1
            while 20 in coins:
                replace(coins,20)
            while 10 in coins:
                replace(coins,10)
            
#        replace(20)
#        replace(20)
#        replace(10)
#    if coin == 20:
#        #n -= 1
#        replace(10)
#        replace(10)
#    if coin == 10:
#        replace(5)
#        replace(5)
#    if coin == 5:
#        n += 4


n = 0   # number of coin combinations; to start, a single 200p coin
coins = [200]
cc = {200:'a',100:'b',50:'c',20:'d',10:'e',5:'f',2:'g',1:'h'}
combos = []
replace(coins,200)
print(200,n)
