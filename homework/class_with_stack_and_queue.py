import queue

class Lift():

    def __init__(self, num):
        self.num=num
    def Que(self, num):
        q = queue.Queue()

        for i in range(self.num):
            q.put(i)

        while not q.empty():
            print(q.get(), end=' ')
        print()
    def Stack(self, num):
        st=[]
        for i in range(self.num):
            st.append(i)
        try:
            while True:
                print(st.pop(), end=' ')
        except:
            print()
l=Lift(5)
l.Que()
l.Stack()

