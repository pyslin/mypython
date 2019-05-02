#启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：
import time,threading

def loop():
    print('thread %s is running'%threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread%s>>>%s'%(threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s ended'%threading.current_thread().name)

print('thread %s is dunning...'%threading.current_thread().name)
#函数loop，线程名LoopThrea传入，建立 Thread的对象
#我们用LoopThread命名子线程。名字仅仅在打印时用来显示，
# 完全没有其他意义，如果不起名字Python就自动给线程命名为Thread-1，Thread-2…
t = threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)


#，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，
# 而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，
# 因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。

import time, threading

# 假定这是你的银行存款:
balance = 0

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
"""
balance = balance + n
也分两步：

计算balance + n，存入临时变量中；
将临时变量的值赋给balance。
也就是可以看成：

x = balance + n
balance = x"""
import time, threading
balance = 0
def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

lock = threading.Lock()

def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)