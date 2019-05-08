class Student:
    pass

def process_student(name):
    # std是局部变量，但是每个函数都要用它，因此必须传进去：
    std = Student(name)
    do_task1(std)
    do_task2(std)

def do_task1(std):
    do_subtask11(std)
    do_subtask12(std)

def do_subtask11(std):
    pass
def do_subtask12(std):
    pass

def do_task2(std):
    do_subtask21(std)
    do_subtask22(std)
def do_subtask21(std):
    pass
def do_subtask22(std):
    pass


import threading
# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    std =local_school.student
    print('Hello,%s(in %s)'%(std,threading.current_thread().name))

def process_thread(name):
#用全局对象.student来指向name，这样就不会不同线程里被其它线程改变
#可以理解为全局变量local_school是一个dict，每个线程都有个值
# 不但可以用local_school.student，还可以绑定其他变量，如local_school.teacher等等
    local_school.student =name
    process_student()

t1 = threading.Thread(target=process_thread,args=('Alice',),name='Thread-a')
t2 = threading.Thread(target=process_thread,args=('Bob',),name='Thread-b')
t1.start()
t2.start()
t1.join()
t2.join()