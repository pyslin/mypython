#个进程至少有一个线程或多个线程，线程是最小的执行单元

from multiprocessing import Process
import os

def run_proc(name):
    print('Run child process %s(%s)...'%(name,os.getpid()))

# os.getpid()获取当前进程id     os.getppid()获取父进程id

if __name__ == '__main__':
    print('Parent process %s'%os.getppid())
#创建子进程时，只需要创建Process的实例传入一个执行函数和函数的参数
    p = Process(target=run_proc,args=('test',))

    print('Child process will start.')
#用start()方法启动，join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    p.start()
    p.join()
    print('Child process end.')

