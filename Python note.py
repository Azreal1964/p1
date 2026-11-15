# class t1(object):
#     def __init__(self):
#         print("1")
#     def __new__(cls, *args, **kwargs):
#         print("2")
#         print(cls)
#         res = super().__new__(cls) #父类方法扩展
#         return res
# t=t1()
# print(t)
import time
# class Pp(object):
#     def __new__(cls, *args, **kwargs):
#         print(1)
#         print(super().__new__(cls))
#         return super().__new__(cls)
#     def __init__(self,n):
#         self.n=n
#         print(self.n)
# p=Pp('bb')
# print(p)

# class a(object):
#     pass
# A1=a()
# print(A1)
# A2=a()
# print(A2)


# class sl():
#     cc=None
#     def __new__(cls, *args, **kwargs):
#         print(1)
#         if cls.cc==None:
#             cls.cc=super().__new__(cls)
#         return cls.cc
#     def __init__(self):
#         print(2)
# s=sl()
# print(s)
# s1=sl()
# print(s1)

# from text2 import te as t2
# from text2 import te as t3
# print(t2,id(t2))
# print(t3,id(t3))

# f =open('zzz.ipynb')
# print(f.name)
# print(f.mode)
# print(f.closed)
# f.close()
# print(f.closed)
# f = open('zzz.ipynb',encoding='utf-8')
# print(f.read(-1))
# f.close()

# file = open('text02.txt','w+',encoding='utf-8')
# # print(file.write('zzzzz'))
# # file.close()
# file.write('鸟厚杰')
# print(file.read())
# file.close()

# f = open('text02.txt','a+',encoding='utf-8')
# print(f.read())
# f.write("\nsamao hhh")
# f.close()

# #文件定位操作：tell() seek()
# f = open('text02.txt','w+')
# f.write("niaohoujeisb")
# pos = f.tell()
# print(pos)
# f.seek(0,0)  #移动到起始位置
# pos2 = f.tell()
# print(pos2)
# f.read(pos)

# #with open 作用：代码执行完，系统会自动调用f.close（），可以省略文件关闭步骤
# with open('text02.txt','w')as f:
#     f.write("hhh  niaohoujie")
# print(f.closed)

# with open('text02.txt','w',encoding='utf-8') as f:
#     f.write("nhj")

# with open('text02.txt',encoding='utf-8') as f:
#     print(f.read())

# #图片复制‘rb’
# #1.读取图片 2.写入图片
# with open(r"C:\Users\Azreal\Pictures\16.jpg",'rb') as file:
#     im = file.read()
#     print(im)
# #将读取到的文件写入当前文件
# with open(r"C:\Users\Azreal\Pictures\16.jpg",'wb') as f:
#     f.write(im)
#
# import os
# os.rename('旧名字','新名字')#重命名
# os.remove('')#删除文件
# os.mkdir('')#创建文件夹
# os.rmdir('')#删除文件夹
# print(os.getcwd())#获取当前路径
# print(os.listdir())#获取目录列表
# print(os.listdir('../'))#获取上一级列表

#迭代器Iterable:依次从对象中把一个个元素取出来 类型:str list tuple dict set等
#条件：实现了__iter__()方法  方法返回了迭代器对象
#for循环原理：通过__iter__()获取可迭代对象的迭代器  然后调用__next__()方法获取下一个值给临时变量
#判断方法 isinstance():判断一个对象是否是可迭代对象或者是一个已知的数据类型
#1.导入模块
from collections.abc import Iterable
# isinstance(对象，类型)
# print(isinstance('123',str))#（int,dict）))

#迭代器(Iterator)：是一个可以记录遍历位置的对象，在上次停留的位置继续做一些事情
#iter（）：获取可迭代对象的迭代器
#next（）：一个个取元素，取完元素后会触发一个异常
# li = [1,2,3,4,5]
# #1.创建迭代器对象
# li2=iter(li)
# #2.获取下一条数据
# print(next(li2))
# print(next(li2))
# print(next(li2))
# print(next(li2))
# print(next(li2))
# #取完元素后会触发StopIterration异常
# print(next(li2))

#步骤：iter()调用对象的__iter__(),并将其返回结果返回
#2.next()掉用对象__next(),一个个取元素
#3.所有元素都取完了，__next__()将引发异常

# #方法2：
# li = [1,2,3,4,5]
# li2=li.__iter__()
# print("li2",li2)
# print(li2.__next__())
# print(li2.__next__())
# print(li2.__next__())
# print(li2.__next__())
# print(li2.__next__())

# print(dir(li))

#可迭代对象iterable和迭代器iterator
#凡是可以作用于for循环的都属于可迭代对象
#凡是可以作用于next（）的都是迭代器
# from  collections.abc import Iterable,Iterator
# name = 'niaohoujie'
# print(isinstance(name,Iterable))
# print((isinstance(name,Iterator)))
# name2=iter(name)
# print(isinstance(name2,Iterable))
# print((isinstance(name2,Iterator)))
#总结：可迭代对象可以通过iter（）转换为迭代器对象
#如果一个对象拥有__iter__(),是可迭代对象，如果一个对象拥有__next__()和__iter__()方法，是迭代器对象
#dir():查看对象中的属性和方法
#重点：可迭代对象并不一定是迭代器对象   迭代器对象一定是可迭代对象

#迭代器协议：对象必须提供一个next方法，执行该方法要么就返回迭代中的下一项，要么就引发StopIteration异常
#自定义迭代器类
#两个特性：__iter__()和__next__()
# class Text(object):
#     def __init__(self):
#         self.num = 1
#     def funa(self):
#         print(self.num)
#         self.num += 1
# tt=Text()
# print(tt)
# for i in range(5):
#     tt.funa()
# for i in tt:
#     print(i)

# class MI(object):
#     def __init__(self):
#         self.num = 1
#     def __iter__(self):
#         return self #返回的是当前迭代器类的实例对象
#     def __next__(self):
#         if self.num == 10:
#             raise StopIteration("no")
#         self.num+=1
#         return  self.num
# mi=MI()
# print(mi)
# for i in mi:
#     print(i)
#生成器：generator
#python中一边循环一边计算的机制，叫生成器
#生成器表达式
# for i in range(5):
#     print(i*5)
#列表推导式:
# li = [i*5 for i in range(5)]
# gen = (i*5 for i in range(5)) #改括号就成了生成器表达式
# print(li)
# print(gen)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))#有异常和迭代器一样
#生成器函数
# python 中，使用了yield关键字的函数就称为生成器函数
# yield的作用：
# 1.类似retrun，将指定值或者多个返回值给调用者
# 2.yield语句一吃一次返回一个结果，在每个结果中间，挂起函数，执行next（），再重新从挂起点继续往下执行
# 使函数中断，并保存中断的状态
# li=[]
# def tt():
#     # global  li
#     li = []
#     li.append('a')
#     li.append('b')
#     print('li:',li)
# tt()
# tt()
#生成器函数
# def ggg():
#     print("鸟侯杰")
#     yield 'da' #返回一个‘a’，并暂停函数，在此挂起，下一次从此处回复运行
#     yield 's'
#     yield 'b'
# g=ggg()
# print(g)
# print(next(g))
# print(next(g))
# print(next(g))

# def gen(n):
#     li=[]
#     a=0
#     while a<n:
#         li.append(a)
#         a+=1
#     # for i in range(n):
#     #     li.append(i)
#     print(li)
# gen(2)

# def ddd(n):
#     li=[]
#     a=0
#     while a<n:
#         li.append(a)
#         yield a
#         a+=1
#     print(li)
# print(ddd(7))
# for i in ddd(7):
#     print(i)
# #使用了yield关键字就是生成器函数

# def tt1():
#     yield 1
#     yield 2
#     yield 3
# print(tt1())
# ta = tt1()
# print(next(ta))
# print(next(ta))
# print(next(ta))
# print(next(tt1()))   取值用next，加括号是调用函数，调动一次从头开始，不加括号从对象中取值
# print(next(tt1()))
# print(next(tt1()))

# def funa():
#     yield 'a'
#     yield 'b'
#     yield 'c'
#
# for i in funa():
#     print(i)

#三者关系
#可迭代对象：指实现了Python迭代协议，可以通过for循环遍历对象，比如list，dictionary，str。。。迭代器，生成器
#迭代器：可以记住自己遍历设置的对象，直观体现就是可以使用next()函数返回值，迭代器只能往前，不能往后。
#当遍历完毕后，next（）会抛出异常
#生成器：是特殊的迭代器，需要注意迭代器不一定是生成器，他是Python中的通过简便的方法写出迭代器的一种手段
#包含关系：可迭代对象》迭代器》生成器

#线程
#线程之间共享资源（全局变量）

#写入数据
# from  threading import Thread
# import time
# li=[] #全局变量
# def ss():
#     for i in range(5):
#         li.append(i)
#         time.sleep(0.4)
#     print(li)
# #读取数据
# def dd():
#     print(li)
# if __name__ == "__main__":
# #创建子线程
#     t1 = Thread(target=ss)
#     t2 = Thread(target=dd)
# #开启子线程
#     t1.start()
# #阻塞线程  必须放在后面
#     t1.join()  #加了join方法等待t1任务执行结束
#     time.sleep(0.8) #时间匹配同时运行
#     t2.start()
#     t2.join()

# #资源竞争
# from  threading import Thread
# import time
# a=0
# b=1000000
# #循环一次就给全局变量a+1
# def add():
#     for i in range(b):
#         global a
#         a+=1
#     print(a)
# def add2():
#     for i in range(b):
#         global a
#         a+=1
#     print(a)
# # add()
# # add2()
# if __name__ =="__main__":
#     first = Thread(target=add)
#     second = Thread(target=add2)
#     first.start()
#     first.join() #等待第一子线程执行完成以后，代码再继续往下执行，开始执行第二个字线程
#     second.start()

#线程同步
#两种方式：join 和 互斥锁
#互斥锁  acquire() 加锁    release()解锁
#两个方法必须要成对出现，否则容易形成死锁
#死锁：一种等待对方释放锁的情景
# from  threading import Thread,Lock
# import time
# a=0
# b=1000000
# lock = Lock()
# #循环一次就给全局变量a+1
# def add():
#     lock.acquire()
#     for i in range(b):
#         global a
#         a+=1
#     print(a)
#     lock.release()
# def add2():
#     for i in range(b):
#         global a
#         a+=1
#     print(a)
# # add()
# # add2()
# if __name__ =="__main__":
#     first = Thread(target=add)
#     second = Thread(target=add2)
#     first.start()
#     first.join()      #等待第一子线程执行完成以后，代码再继续往下执行，开始执行第二个字线程
#     second.start()
#注意：互斥锁是多个线程一起去抢，抢到锁的锁的线程先执行

#进程介绍
#是操作系统进行资源分配和调度的基本单位，是操作系统结构的基础
#一个正在运行的程序或者软件就是一个进程
#程序跑起来就成了进程
#注意：进程里面可以创建多个进程，
#多个进程也可以完成多个任务
#进程的状态
#就绪状态：运行的条件都已经满足，正在等待CPU执行
#执行状态：CPU正在执行其功能
#等待状态：等待某些条件满足，如一个程序sleep了，此时就处于等待状态
# print("tianiaol") #程序开始，处于执行状态
# s = input("输入鸟侯杰") #光标闪动，等待用户输入，处于等待状态
# print(s) #执行状态
# time.sleep(1) #处于等待状态

#进程的语法结构 multiprocessing模块提供了process类代表进程对象
#process 类参数
#1.target：执行的目标任务名，即子进程要执行的任务
#2.arge: 以元组的形式传参
#3.kwarges：以字典的形式传参
#方法：
#1.start（）：开启子进程
#2.is_alive():判断子进程是否活着，活着返回：Ture，死亡返回：False
#3.join():等待子进程执行结束
#常用的属性
#name：当前进程的别名，默认process-N
#pid： 当前进程的进程编号
# from multiprocessing import Process
# import os
# def s():
#     # os.getpid():获得当前进程编号
#     # os.getppid():获得当前夫进程编号
#     print(f"{os.getppid()}")
#     print("ss")
# def d():
#     print(f"{os.getppid()}")#就是文件的pid
#     print("dd")
# if __name__=="__main__":
#     #创建子进程
#     #修改子进程名第一种方式
#     p1=Process(target=s,name="子进程1")
#     p2=Process(target=d,name="子进程2")
#     p1.start()
#     p2.start()
#     #修改子进程的第二种方式
#     p1.name="子进程11"
#     p2.name="子进程22"
#     #访问name属性
#     print(p1.name)
#     print(p2.name)
#     #查看子进程的进程编号
#     print(p1.pid)
#     print(p2.pid)

# from multiprocessing import Process
# import os
# def eat(name):
#     print(f"{name}chifan")
# def sleep(name):
#     print(f"{name}shuijiao")
# if __name__ == "__main__":
#     p1=Process(target=eat,args=("niaohoujie",))
#     p2=Process(target=sleep,args=("suiniaohoujie",))
#     p1.start()
#     p1.join() #主进程等待子进程执行
#     #写在主进程中判断存活状态的时候需要加入join阻塞一下
#     p2.start()
#     print(p1.is_alive())
#     print(p2.is_alive())
# if __name__ == "__main__":
#防止别人导入文件的时候执行main里面的方法
#防止window系统递归创建子进程

#进程间不共享全局变量


#进程间的通信
# #主要使用Queue（队列）
# q.put(): 放入数据
# q.get(): 取出数据
# q.empty(): 判断队列是否为空
# q.qsize(): 返回当前队列包含的消息数量
# q.full(): 判断队列是否满了

#导入模块 from queue import Queue
#初始化一个队列
# from queue import Queue
# q = Queue(3)  #最多可以接收三条消息，没写或者是负值就代表上限，直到内存尽头
# q.put("niaodaojintou")
# q.put("yyniaodaojintou")
# print(q.full())
# q.put("noniaodaojintou")
# print(q.full())
# print(q.qsize())
# print(q.get()) #获取队列的一条消息，然后将其从队列中移除
# print(q.get())
# print(q.empty())
# print(q.get())
# print(q.empty())
# print(q.qsize())

# from multiprocessing import Process,Queue
# import time
# li = ["xx","bb","hh","zz"]
# def w(q1):
#     for i in range(5):
#         print(i)
#         li.append(i)
#         q1.put(i)
#         time.sleep(0.1)
#     print(li)
# def r(q2):
#     while True:
#         if q2.empty():
#             break
#         else :
#             print(q2.get())
#     print(li)
# if __name__ == "__main__":
#     #创建队列对象
#     q = Queue()
#     p1=Process(target=w,args=(q,))
#     p2=Process(target=r,args=(q,))
#     p1.start()
#     p1.join()
#     p2.start()
#     p2.join()

#线程
#多任务
# import time
# def s():
#     print("ss")
#     time.sleep(0.5)
#     print("sss")
# def d():
#     print("dd")
# s()
# d()

#多线程
#线程：是CPU调度的基本单位，每一个进程至少都会有一个线程，这个线程通常就是我们所说的主线程
#进程：是操作系统进行资源分配的基本单位，每打开一个程序至少有一个进程。
#一个进程默认有一个线程，进程里面可以有多个线程，线程是依附在进程里面的，没有进程就没有线程
#导入模块：import threading
#Thread线程参数
#target：执行的任务名
#args：以元组的形式给任务传参
#kwargs： 以字典的形式给任务传参
# import time
# import threading
# def s(re):
#     print(f"{re}ss")
#     time.sleep(0.5)
#     print("sss")
# def d(ne):
#     print(f"{ne}dd")
#     time.sleep(0.5)
#     print("ddd")
#
# if __name__ == "__main__":
#     #1.创建子进程
#     t1 = threading.Thread(target=s,args=('nhj',))
#     # print(t1)
#     t2 = threading.Thread(target=d,args=('nhj',))#元组形式
#     # 3.守护线程，必须放在start（）前面：主线程执行结束，子线程也会跟着结束。
#     t1.setDaemon(True)
#     t2.setDaemon(True)
#     # 2.开启子线程
#     t1.start()
#     t2.start()
#     #4.阻塞主线程join（）：暂停作用，等子线程执行结束后，主线程才会进行执行，必须放在start后面
#     t1.join()
#     t2.join()
#     #5.获取线程名字
#     print(t1.getName())
#     print(t2.getName())
#     #6.更改线程名字
#     t1.setName("niao1")
#     t2.setName("niao2")
#     print(t1.getName())
#     print(t2.getName())
#     print("niaohjdasb")
# s()
# d()















