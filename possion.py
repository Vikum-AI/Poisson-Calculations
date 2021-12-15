import math

data = []
count = 0
# x = 4
# mean = 2.1


# Values to place in equation
x = int(input("Enter x value: "))
mean = float(input("Enter lambda value: "))


# P(X = x)
def equals():
    ans = (math.exp(-mean) * mean**x) / math.factorial(x)
    print("P( X =", x, ") = ", ans)


# P(X < x)
def less_than():
    for i in range(x):
        # ans = (math.exp(-mean) * mean**i) / math.factorial(i)
        ans = (math.exp(-mean) * mean**i) / math.factorial(i)
        data.append(ans)

    for i in range(x):
        total = data[i]

    print('')
    print("P( X <", x, ") = ",  total)
    print('')


def greater_than():
    for i in range(x):
        # ans = (math.exp(-mean) * mean**i) / math.factorial(i)
        ans = (math.exp(-mean) * mean**i) / math.factorial(i)
        data.append(ans)

    for i in range(x):
        total = data[i]

    total = 1 - total

    print('')
    print("P( X <", x, ") = ",  total)
    print('')
