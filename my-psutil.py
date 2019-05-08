#psutil = process and system utilities设施

import psutil

print(psutil.cpu_count())
#cpu逻辑数量
print(psutil.cpu_count(logical=False))
#cpu物理核心
print(psutil.cpu_times())
for x in range(10):
    print(psutil.cpu_percent(interval=1,percpu=True))
    #CPU使用率，每秒刷新一次，累计10次



#使用psutil获取物理内存和交换内存信息
print(psutil.virtual_memory())
print(psutil.swap_memory())


#通过psutil获取磁盘分区、磁盘使用率和磁盘IO信息
print(psutil.disk_partitions())# 磁盘分区信息
print(psutil.disk_usage('/')) # 磁盘使用情况
print(psutil.disk_io_counters())# 磁盘IO

#psutil可以获取网络接口和网络连接信息：
print(psutil.net_io_counters())# 获取网络读写字节／包的个数
print(psutil.net_if_addrs()) # 获取网络接口信息
print(psutil.net_if_stats())# 获取网络接口状态
#要获取当前网络连接信息
print(psutil.net_connections())

#获取进程信息
print(psutil.pids())#process id s
p = psutil.Process(672)
print(p.name())# 进程名称
print(p.exe()) # 进程exe路径
print(p.cwd())# 进程工作目录
print(p.cmdline())# 进程启动的命令行
print(p.ppid())# 父进程ID
print(p.children())# 子进程列表
print(p.status)
p.username()  # 进程用户名
p.create_time() # 进程创建时间
p.terminal() # 进程终端
p.cpu_times() # 进程使用的CPU时间
p.memory_info()
p.open_files() # 进程打开的文件
p.connections() # 进程相关网络连接
p.num_threads() # 进程的线程数量
p.threads() # 所有线程信息
p.environ() # 进程环境变量
p.terminate() # 结束进程