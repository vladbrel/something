#1 Заполнить массив нулями, кроме первого и последнего элементов, которые должны быть равны единице.
import random
leng=int(input('Введи длину списка')) #этот кусок не комментировать, для всех задач актуален
# a=[]
# a.append(1)
# for i in range(leng-2):
#     a.append(0)
# a.append(1)
# print(a)
#
# #2 Заполнить массив нулями и единицами, при этом данные значения чередуются, начиная с нуля.
# b=[]
# i=0
# while i<leng:
#     b.append(0)
#     i+=1
#     if i<leng:
#         b.append(1)
#         i+=1
#     else:
#         break
# print (b)
#
# #3 Заполнить массив последовательными нечетными числами, начиная с единицы.
# c=[]
# i=1
# while i<leng*2:
#     c.append(i)
#     i+=2
# print(c)
#
# #4 Сформировать массив из элементов арифметической прогрессии с заданным первым элементом x и разностью d.
# x=int(input('Введи первый элемент'))
# d=int(input('введи разность'))
# f=[]
# i=0
# while i<leng:
#     f.append(x+d*i)
#     i+=1
# print(f)
#
# #5 Сформировать возрастающий массив из четных чисел.
# e=[]
# i=2
# while i<leng*2:
#     e.append(i)
#     i+=2
# print(e)

#6 Сформировать убывающий массив из чисел, которые делятся на 3.
# z=int(input('введи начальное значение'))
# i=0
# if z%3!=0:
#     z-=1
# elif z%3!=0:
#     z-=1
# g=[]
# while i<leng:
#     g.append(z)
#     z-=3
#     i+=1
# print(g)

#7 Создать массив из n первых чисел Фибоначчи.
# h=[]
# h.append(0)
# h.append(1)
# i=2
# while i<leng:
#     h.append(h[i-2]+h[i-1])
#     i+=1
# print(h)

#8 Заполнить массив заданной длины различными простыми числами. Натуральное число,
# большее единицы, называется простым, если оно делится только на себя и на единицу.
# def IsPrime(num): # до 250 проверяет
#     if (num==2) or (num==3) or (num==5) or (num==7) or (num==11) or (num==13):
#         return True
#     k = 2
#     while k<14:
#         if (num % k)==0:
#             break
#         else: k+=1
#     if k== 14:
#         return True
#     return False
# j=[]
# i=0
# while i<leng:
#     a = random.randint(2, 250)
#     if IsPrime(a):
#         j.append(a)
#         i+=1
# print(j)

#9 Создать массив, каждый элемент которого равен квадрату своего номера.
# a=[i**2 for i in range(1,leng+1)]
# print(a)

#10Создать массив, на четных местах в котором стоят единицы, а на нечетных местах - числа, равные остатку от деления своего номера на 5.
# нумерация с нуля, потому вопрос чётности индекса немного спорен:)
# a=[]
# i=1
# a.append(1)
# while i<leng:
#     if i % 2==0:
#         a.append(1)
#     else:
#         a.append(i % 5)
#     i+=1
# print(a)

# #если нумерация с единицы:
# a=[]
# i=0
# while i<leng:
#     if i % 2:
#         a.append(1)
#     else:
#         a.append(i % 5)
#     i+=1
# print(a)

#11 Создать массив, состоящий из троек подряд идущих одинаковых элементов.
# a=[]
# i=0
# while i<leng:
#     b=chr(random.randint(33,122))
#     a.append(b)
#     i+=1
#     if i<leng:
#         a.append(b)
#         i+=1
#         if i < leng:
#             a.append(b)
#             i += 1
#     else:break
# print(a)

#12 Создать массив, который одинаково читается как слева направо, так и справа налево.
# a=[i for i in range(leng)]
# for i,j in enumerate(a):
#     a[i]=a[-i-1]=chr(random.randint(33,122))
# print(a)

#13 Сформировать массив из случайных чисел, в которых ровно две единицы, стоящие на случайных позициях.
# a=[]
# for i in range(0,leng):
#     a.append(random.randint(0,9))
# print('первоначальный список', a)
# b=a.count(1)
# f=b
# while f>0:
#     a.remove(1)
#     f-=1
# print('удаление единиц',a)
# while a.count(1)<2:
#     c=random.randint(0,leng-b)
#     a.insert(c,1)
#     leng+=1
# print('список с двумя единицами',a)

#14 Заполните массив случайным образом нулями и единицами так, чтобы количество единиц было больше количества нулей.
# a=[]
# for i in range(0,leng):
#     a.append(random.randint(0,1))
# print('рандомный список',a)
# while a.count(0)+1>a.count(1):
#     c=random.randint(0,leng)
#     a.insert(c,1)
#     leng+=1
# print('конечный список',a)

#15 Сформировать массив из случайных целых чисел от 0 до 9 ,
# в котором единиц от 3 до 5 и двоек больше троек.
# a=[]
# for i in range(0,leng):
#     a.append(random.randint(0,9))
# print(a)
# while a.count(3)+1>a.count(2):
#     c=random.randint(0,leng)
#     a.insert(c,2)
#     leng+=1
# print('2>3 список:',a)
# b=a.count(1)
# f=b
# while f>0:
#     a.remove(1)
#     f-=1
# print('удаление единиц',a)
# while a.count(1)<random.randint(3,5):
#     c=random.randint(0,leng-b)
#     a.insert(c,1)
#     leng+=1
# print('список с 3-5 единицами',a)

# 16 Создайте массив, в котором количество отрицательных чисел равно количеству
# положительных и положительные числа расположены на случайных местах в массиве.
# a=[]
# for i in range(0,leng):
#     a.append(random.randint(-10,10))
# print(a)
# otr=0
# pol=0
# for i in a:
#     if i<0:
#         otr+=1
#     elif i>0:
#         pol+=1
# if otr>pol:
#     k=otr-pol
#     while k>0:
#         c = random.randint(0, leng)
#         a.insert(c, random.randint(1,9))
#         k-=1
#         leng+=1
# elif pol > otr:
#     k = pol - otr
#     while k > 0:
#         c = random.randint(0, leng)
#         a.insert(c, random.randint(-9, -1))
#         k -= 1
#         leng+=1
# else:
#     print('Nice random')
# print(a)

#17 Заполните массив случайным образом нулями, единицами и двойками так, чтобы
# первая двойка в массиве встречалась раньше первой единицы, количество единиц
# было в точности равно суммарному количеству нулей и двоек.
# a=[]
# if leng%2==1:
#     leng+=1
# for i in range(0,leng):
#     a.append(random.randint(0,2))
# print(a)
#
# while (a.count(1)!=a.count(0)+a.count(2)):
#
#     c = random.randint(0, leng-1)
#     if a.count(1)<a.count(0)+a.count(2):
#         a.pop(c)
#         a.insert(c,1)
#     else:
#         a[c]=2*random.randint(0, 1)
#
#     if a.count(1)>0:
#         ed=a.index(1)
#         i = ed
#         if a.count(2)>0:
#             if ed<a.index(2):
#                 a.remove(1)
#                 a.insert(ed,2)
#         else:
#             a.remove(1)
#             a.insert(ed, 2)
# print('fff', a)

#18Придумайте правило генерации массива заданной длины. Определите, сгенерирован ли
# данный массив вашим правилом или нет.
a=[i**3+2 for i in range(1,leng+1)if not i%3==0]
print(a)

