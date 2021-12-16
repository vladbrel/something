#1.Напишите программу, которая находит среднее арифметическое всех чисел, записанных в файле в
#столбик, и выводит результат в другой файл.
# with open('text.txt') as file:
#     s=0
#     k=0
#     for i in file:
#         try:
#             i=int(i)
#         except:
#             continue
#         s+=i
#         k+=1
#     s=s/k
# print(s)
# s=str(s)
# with open('t.txt', 'w') as file:
#     file.write(s)

#2. Напишите программу, которая находит минимальное и максимальное среди чётных положительных чисел,
# записанных в файле, и выводит результат в другой файл. Учтите, что таких чисел может вообще не быть.
# with open('text.txt') as file:
#     min= int(7) #любое положительное нечетное число
#     max = int(1)
#     for i in file:
#
#         try:
#             i=int(i)
#         except:
#             continue
#         if i>1 and i%2==0:
#             x=i
#             n=i
#             if x>max:
#                 max=x
#             if n<min:
#                 min=n
#     if max==1:
#         max=None
#     if min==7:
#         min=None
#
#     print(min, max)
#     min=str(min)
#     max=str(max)
# with open('min-max.txt', 'w') as file:
#     file.write(min+'\n')
#     file.write(max)

# 3. В файле в столбик записаны целые числа, сколько их –неизвестно. Напишите программу, которая определяет
# длину самой длинной цепочки идущих подряд одинаковых чисел и выводит результат в другой файл.
# with open('3.txt') as f:
#     c=1
#     max_c=1
#     j=1000000
#     for i in f:
#         if i==j:
#             c+=1
#             if max_c<c:
#                 max_c=c
#
#         else:
#             c=1
#         j = i
# print(max_c)
# with open('3_1.txt', 'w') as file:
#     file.write(str(max_c))

#4. В файле записаны в столбик целые числа. Вывести в другой текстовый файл те же числа,
#отсортированные в порядке возрастания.
# with open('3.txt') as f:
#     a=[]
#     for i in f:
#         i=int(i)
#         a.append(i)
#         a.sort()
# print(a)
# with open('4.txt', 'w') as f:
#     for i in a:
#         f.write(str(i)+'\n')

#5. В файле записано данные о собаках: в каждой строчке кличка собаки, ее возраст и порода:
# Мухтар 4 немецкая овчарка Вывести в другой файл сведения о собаках, которым меньше 5 лет.
# with open('dogs.txt') as f:
#     a=[]
#     for i in f:
#         if i.count('0')==1 or i.count('1')==1 or i.count('2')==1 or i.count('3')==1 or i.count('4')==1 :
#             a.append(i)
# i=1
# with open('young_dogs.txt','w') as f:
#     for i in a:
#         f.write(i)


#6 Создать текстовый файл, предварительно убедиться, что файла с таким именем не существует, записать в него построчно данные,
# которые вводит пользователь. Окончанием ввода служит слово "конец".
# import os.path
# g='E:\Projects\Projects_stormnet\my_first_project\hjj.txt'
# h=os.path.isfile(g)
# if h:
#     print('файл существует)))')
# else:
#     with open('hjj.txt','a') as f:
#         while True:
#             a=input('введи данные')
#             if a=='конец':
#                 break
#             else:
#                 f.write(a+'\n')
#     f.close()

# 7. Посчитать количество строк в файле, количество слов и цифр в каждой строке.
# with open ('7.txt') as f:
#     strings=0
#     for i in f:
#         strings+=1
#         nums=0
#         words=0
#         word=''
#         for k, j in enumerate(i):
#             if j.isdigit():
#                 nums += 1
#             elif j.isalpha():
#                 word += j
#             elif not j.isdigit() and not j.isalpha():
#                 word += ','
#             print(nums)
#         arr1 = word.split(',')
#         print(arr1)
#         for i in arr1:
#             if len(i) > 0:
#                 words += 1
#         print(words)
# print(word)
# print(strings)

#8. Найти в файле строки, содержащие  значения "33".
# with open('8.txt') as f:
#     for i in f:
#         if i.find('33')!=-1:
#             print(i)

#9. Написать функцию, которая будет искать определенные значения в файле, удалять их,
# и записывать результат обратно в файл.

# def removing(a,b,s):
#     arr = []
#     with open(a) as f:
#         for i in f:
#
#             arr.append(i)
#     print(arr)
#     arr2=[]
#     for i in arr:
#         if i.count(s)!=0:
#             j=0
#             arr1=[]
#             stri = ''
#             while len(arr2)<(len(i)-len(s)*i.count(s)):
#                 h=i.index(s)
#                 if h==0:
#                     j=len(s)
#                     if i.count(s)>1:
#                         h=i.index(s,j)
#                 arr1.append(i[j:h])
#                 j=h+len(s)
#
#                 for k in arr1:
#                     stri=stri+k
#                 arr2.append(stri)
#         else:
#             arr2.append(i)
#     print(arr2)
#     with open(b,'w') as f:
#         for i in arr2:
#             f.write(i)
# removing('9.txt','9_1.txt', 'rt')
#если нужная(удалаяемая подстрока является отдельной строкой в первом файле,
# то легко решить. Я попытался решить так, что удалаяемая подстрока может быть лишь
# частью строки, но не получилось, мозгов не хватает дорешать:(

#10. Прочитать данные из файла в словарь, ключ - первое слово в строке, значение
# - список из оставшихся слов, удалить все символы '\n'.
# d={}
# with open('10.txt') as f:
#     for i in f:
#         words = 1
#         for y,j in enumerate(i):
#             if j==' ':
#                 first_word=i[0:i.index(' ')]
#                 words+=1
#         print(first_word)
#         print(words)
#         d[first_word]=words-1
#     print(d)

#11. Написать функцию, которая будет читать файл, удалять из каждой строки два
# любых символа, идущих подряд.  строка - 'awwlghhgicooe', результат - 'alice'
# def st(s):
#     with open(s) as f:
#         s1=''
#         for k in f:
#
#             for i,j in enumerate(k):
#                 if i==0:
#                     if  k[i]==k[i+1]:
#                         continue
#                     else:
#                         n=i
#                         s1=s1+k[n:n+1]
#                 elif i+1<len(k):
#                     if k[i]==k[i-1] :
#                         continue
#                     else:
#                         n=i
#                         s1=s1+k[n:n+1]
#                 else:
#                     if j!=s[i-1]:
#                         s1=s1+j
#             print(s1)
#
# st('11.txt')