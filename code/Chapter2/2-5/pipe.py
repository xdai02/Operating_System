import multiprocessing

def send_data(pipe, data):
    pipe.send(data)
    print("[Process %d] Sent: %s" % (
        multiprocessing.current_process().pid,
        data
    ))

def recv_data(pipe):
    print("[Process %d] Received: %s" % (
        multiprocessing.current_process().pid, 
        pipe.recv()
    ))

def main():
    send_end, recv_end = multiprocessing.Pipe()
    
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