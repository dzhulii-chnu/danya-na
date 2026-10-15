import math

def term(k = 1, x = 2.0, a = 3.0):
    return ((-1) ** k) * (x ** (-4 * k)) / ((a ** 4) + math.factorial(k))

def task1():
    x = float(input("input x != 0: "))
    a = float(input("input a != 0: "))
    eps = float(input("input eps > 0: "))
    if x == 0 or a == 0 or eps < 0:
        print("error")
        return 0
    k = 1
    count = 0
    total = 0
    while abs( term(k, x, a) - term(k + 1, x, a)) >= eps:
        total += term(k, x, a)
        k += 1
        count += 1
    print("result :", total)
    print("number of terms :", count)


def element(n = 1 , x = 1.0):
    if n == 0: return x
    cur = element(n - 1, x)
    res = (4/5 * cur + (x/(5 * cur ** 4)))
    return res
def task2():
    n = int(input("input n < 100: "))
    x = float(input("input x != 0: "))
    if n > 100 or x == 0:
        print("error")
        return 0
    print(element(n, x))

def task3():
    text = str(input("input text > "))
    result = set(text.split(', '))
    new = " ".join(result)
    print(new)

def binar(n = 10):
    if n < 2 : return str(n)
    return binar(n // 2) + str(n % 2)

def task4():
    n = int(input("input n > 0: "))
    if n == 0: return 0
    print(binar(n))


def menu():
    n = int(input("input number of task: "))
    while n != 0:
        match n:
            case 1:
                task1()
            case 2:
                task2()
            case 3:
                task3()
            case 4:
                task4()

        n = int(input("input number of task: "))
menu()