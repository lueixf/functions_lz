def prime (a):
    k = 0
    for i in range(2, a // 2+1):
        if (a % i == 0):
            k = k+1
    if (k <= 0):
        print("Число простое")
    else:
        print("Число не является простым")
    return(k)





a = int(input("Введите число: "))
print(prime(a))

