#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# task.py for windows
import time, sys, queue, random
from multiprocessing.managers import BaseManager
#初始化管理器
BaseManager.register('get_task')
BaseManager.register('get_result')
conn = BaseManager(address = ('127.0.0.1',5002), authkey = b'123')
#尝试连接
try:
    conn.connect()
except:
    print('连接失败')
    sys.exit();
#获得任务，结果队列
task = conn.get_task()
result = conn.get_result()

while not task.empty():
    #获得任务（也就完成计算）及序号
    n = task.get(timeout = 1)

    print('run task %d' % n)
    #休息随机秒
    sleeptime = random.randint(0,3)
    time.sleep(sleeptime)
    rt = (n, sleeptime)
    
    #返回结果，及序号
    result.put(rt)

if __name__ == '__main__':
    pass;


"""
import time,sys,queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

q =queue.Queue()
#这个管理器只从网络获取队列queue，所以注册时只提供名字
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')
#连接到服务器，就是运行task_master.py的机器
server_addr = '127.0.0.1'
print('Connect to server %s...'%server_addr)
#端口 验证码保持和task_master.py保持一致（就是登录它）
m = QueueManager(address=(server_addr,5000),authkey=b'abc')
#启动连接
m.connect()
#指向队列对象
task = m.get_task_queue()
result = m.get_result_queue()
## 从task队列取任务,并把结果写入result队列:
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d'%(n,n))
        r = '%d * %d = %d' %(n,n,n*n)
        time.sleep(1)
        result.put(r)
    except q.Empty:
        print('task queue is empty.')

print('worker exit.')

"""

