from multiprocessing import Pool
import os, time ,random

def long_time_task(name):
    print('Run task %s(%s)'%(name,os.getpid()))
#用到time模块里的tiem（）等3个函数，random模块里random（）函数
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('Task %s run%0.2f second'%(name,(end-start)))
#0 代表按原数位，2f代表小数点后2位浮点


if __name__ == '__main__':
    print('Parent process %s.'%os.getppid())
    #同时4个Pool的对象
    p = Pool(4)
    #for循环运行5个进程
    for i in range(5):
        #读asinc，异步，apply_async()方法，传入执行对象，和函数参数list（记得逗号）
        p.apply_async(long_time_task,args=(i,))
    print('Waiting for all subprocesses done....')
#先调用close()，调用close()之后就不能继续添加新的Process了,不是关闭
 #对Pool对象调用join()方法会等待所有子进程执行完毕
    p.close()
    p.join()
    print('All subprocesses done.')


import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)
print('####')


#如果子进程还需要输入，则可以通过communicate()方法输入：

import subprocess

print('$ nslookup')
#subprocess模块 Popen类 communicate方法
p = subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PTPE,stderr=subprocess.PIPE)
output,err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:',p.returncode)


#上面的代码相当于在命令行执行命令nslookup，然后手动输入：

"""
set q=mx
python.org
exit
"""