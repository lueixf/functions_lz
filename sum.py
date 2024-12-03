
def add (num_list):
     res = float(num_list[0])
     for i in range (1,len(num_list)):
        res += float(num_list[i])
    
     return(res)  

a = input('введите числа')
num_list = a.split()
b = add(num_list)
print( 'сумма всех чисел в списке равна ', b)