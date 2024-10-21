def palindromeCheck(n):
    m = str(n)
    if m == m[::-1]:
        return True
    else:
        return False

def perfectnumberCheck(n):
    l = []
    for a in range(1, n // 2 + 1):
        if n % a == 0:
            l.append(a)
    if sum(l) == n:
        return True
    else:
        return False

n = int(input("Enter a number: "))

if palindromeCheck(n):
    print("Palindrome")
else:
    print("Not a palindrome")

if perfectnumberCheck(n):
    print("Perfect number")
else:
    print("Not a perfect number")
