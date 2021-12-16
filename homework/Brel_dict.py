user = {
    'k':1,
    2: 2,
    'name': 3,
    'login': 4,
    'parents': {'mother': [5,{'k':6},'7',[{'a':8}]],
                'father': '9'},
    'g':('10',{'p':11})
}
def f(r):
    arr=[]
    for i in r.values():
        if type(i)!=dict:
            if type(i)!=tuple and type(i)!=list and type(i)!=dict:
                arr.append(i)
            else:
                for k in i:
                    if type(k) != dict:
                        arr.append(k)
                    else:
                        for l in k.values():
                            arr.append(l)

        else:
            for j in i.values():
                if type(j) != dict:
                    if type(j) != tuple and type(j) != list:
                        arr.append(j)
                    else:
                        for k in j:
                            if type(k)!=dict and type(k)!=list and type(k)!= tuple:
                                arr.append(k)
                            elif type(k)==tuple or type(k)==list:
                                for m in k:
                                    if type(m)==dict:
                                        for n in m.values():
                                            arr.append(n)
                                    else:
                                        arr.append(m)
                            else:
                                for l in k.values():
                                    arr.append(l)
    print(arr)
f(user)
