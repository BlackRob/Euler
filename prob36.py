def palindromic(A,B):
    revA = A[::-1]
    revB = B[::-1]
    if revA == A and revB == B:
        return True
    else:
        return False




sump = 0

for i in range(1000000):
    bi = '{0:b}'.format(i)
    si = str(i)
    if palindromic(si,bi):
        print(si,bi)
        sump += i

print(sump)