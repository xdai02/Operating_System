import multiprocessing

def send_data(pipe, data):
    """
        往管道发送数据
        Args:
            pipe (Pipe): 管道
            data (str): 发送的数据
    """
    pipe.send(data)
    print("【进程%d】发送数据：%s" % (
        multiprocessing.current_process().pid,
        data
    ))

def recv_data(pipe):
    """
        从管道接收数据
        Args:
            pipe (Pipe): 管道
    """
    print("【进程%d】接收数据：%s" % (
        multiprocessing.current_process().pid, 
        pipe.recv()
    ))

def main():
    # 管道分为发送端和接收端
    send_end, recv_end = multiprocessing.Pipe()
    # 创建两个子进程，将管道传递到对应的处理函数
    sender = multiprocessing.Process(
                target=send_data,
                args=(send_end, "Hello!")
            )
    receiver = multiprocessing.Process(
                target=recv_data,
                args=(recv_end,)
            )
    sender.start()
    receiver.start()

if __name__ == "__main__":
    main()