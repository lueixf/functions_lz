a = float(input('введите число'))

def even(a):
    if (a % 2 == 0):
        print('число', a , 'чётное')
    else:
        print('число', a , 'нечётное')

    return(a)

print(even(a))