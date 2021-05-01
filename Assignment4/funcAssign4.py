# Abbie Dyck
# 110046150

def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


print("The number of sequences is:", fib(int(10)))
