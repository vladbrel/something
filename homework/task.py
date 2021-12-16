# s =[int(i) for i in input('введи строку').split(' ')]
# cnt = 0
# n = 0
# s.sort()
# for i in s:
#     while n < len(s)-1 :
#         if s[n] == s[n + 1]:
#             n += 1
#             cnt += 1
#         if cnt > 0:
#             print(s[n], end = ' ')
#         if n > len(s):
#             quit()
#         if s[n] != s[n + 1]:
#             n += 1
#             cnt = 0
# print(len(s))
# prog_for_stepik
# a=input('Введи строку: ')
# print(len(a))
# s=a.split()
# if len(s)==1:
#     print(a)
# else:
#     d=[]
#     for i,j in enumerate(s):
#         if i<len(s)-1:
#             d.append(int(s[i-1])+int(s[i+1]))
#         else:
#             d.append(int(s[i-1])+int(s[0]))
#     print(d)
# print(s)

# d = {'id':1, 'name': 'Bob'}
# print(d.get('name'))
# print(d['name'])
# for i in d:
#     print(d[i])
# print(d.values())

# d={'1':1}
# print(d.get('1'))
# if d.get('2')== None:
#     print('111')
# else:
#     print('222')
















