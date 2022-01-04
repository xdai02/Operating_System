import multiprocessing

def worker():
    """
        进程处理函数
    """
    print("【进程】id：%d，名称：%s" % (
        multiprocessing.current_process().pid,
        multiprocessing.current_process().name)
    )

def main():
    print("【主进程】id：%d，名称：%s" % (
        multiprocessing.current_process().pid,
        multiprocessing.current_process().name)
    )
    
    # 创建3个进程
    for i in range(3):
        process = multiprocessing.Process(target=worker, name="进程%d" % i)
        process.start()

if __name__ == "__main__":
    main()