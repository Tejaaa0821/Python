
m= int(input("Enter the 1st num: "))
n= int(input("Enter the 2nd num: "))
for j in range(m, n+1 ):
    if j > 1:
        for i in range(2, j):
            if j% i == 0:
                break
        else:
            print(j)

    