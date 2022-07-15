from unittest import result

def zero(n):
    count = 0

    for i in range(n):
        if n[i] != 0:
            n[count] = n[i]
            count+=1
    while count < n:
        n[count] = 0
        count += 1








