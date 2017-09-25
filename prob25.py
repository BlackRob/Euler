def fib(x,y):
    return x + y

x = 1
y = 1
next = 0
index = 2

while True:
    next = fib(x,y)
    index += 1
    if  len(str(next)) == 1000:
        print(index)
        #print(next)
        break
    x = y
    y = next