import multiprocessing  # 导入多进程模块
# 获取CPU的可用数量
print("CPU内核数量：%d" % multiprocessing.cpu_count())