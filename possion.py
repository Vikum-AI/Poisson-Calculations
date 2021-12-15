import math

data = []
count = 0
x = 4
mean = 2.1

# Values to place in equation
def input(): 
    x  = int(input("Enter x value: "))
    mean = float(input("Enter lambda value: "))


# P(X=x)
def equals(): 
    ans = (math.exp(-mean) * mean**x) / math.factorial(x)
    print("P( X =" , x , ") = ", ans)


# P(X<x)

for i in range(x): 
    # ans = (math.exp(-mean) * mean**i) / math.factorial(i)
    ans = (math.exp(-mean) * mean**i) / math.factorial(i)
    print(i)
    data.append(ans)
    

print(data)
    