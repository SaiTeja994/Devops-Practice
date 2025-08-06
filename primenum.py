#write a python code for prime numbers between 1 t0 100
for i in range(1,101):
    flag = 0
    for j in range(2, i):
        if(i % j == 0):
            flag = 1
            break
        if(flag == 0):
            print(i)
            