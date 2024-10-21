def fact(a):
    f = 1  # Initialize f to 1 for factorial calculation
    for i in range(1, a + 1):
        f = f * i
    return f

def spl(n):
    s = 0
    k = n
    while n != 0:
        a = n % 10
        s = s + fact(a)
        n = n // 10
    if k == s:
        print("Special number")
    else:
        print("Not special number")

n = int(input("Enter number: "))
spl(n)
