# Транспонирование матрицы
#var1
matrix =[[0.5,0,0,0,0],
        [1,0.5,0,0,0],
        [1,1,0.5,0,0],
        [1,1,1,0.5,0],
        [1,1,1,1,0.5]]


# Транспонирование
matrix_t=list(zip(*matrix))
matrix_t_as_list=list(map(list, zip(*matrix)))

#var2
a=[0.5,0,0,0,0]
b=[1,0.5,0,0,0]
c=[1,1,0.5,0,0]
d=[1,1,1,1,0.5]
matrix_t=list(zip(a,b,c,d))
# func(*arg...**)))
print('без звездочки:\n{}'.format(matrix))
print('со звездочкой:')
print(*matrix)
print('*' * 20)


# Вывод матриц
print(matrix)
print(matrix_t)
#print(matrix_t_as_list)

print('*'*20)

for line in matrix_t_as_list:
    print(line)
    for number in line:
        print(number ** 2)

#a=[1, 12.5, 55, 'hello', True, [0,1,5]]
#a.append(999)
#print(a)

a=[1,3,5]
b=[2,4,6]
c=[10,20,30]
result=list(zip(a,b,c))
result_as_list=list(map(list, result))

#print(type(result[0]))

print(result)
print(result_as_list)

#print(help(list))
print(dir(result_as_list))
#********

a=[1,3,5]
b=[2,4,6]
c=[10,20,30]
print a(-2)
a,b,c=d,a,b