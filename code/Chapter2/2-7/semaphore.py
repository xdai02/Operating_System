import multiprocessing
import time

def work(sema):
    if sema.acquire():
        print("[Process %d] Start" % 
            multiprocessing.current_process().pid)
        time.sleep(2)       # simulate process execution
        print("[Process %d] End" % 
            multiprocessing.current_process().pid)
        sema.release()

def main():
    # allow 3 processes to execute concurrently
    sema = multiprocessing.Semaphore(3)
    workers = [
        multiprocessing.Process(target=work, args=(sema,))
        for _ in range(10)
    ]

    for worker in workers:
        worker.start()
    for worker in workers:
        worker.join()

if __name__ == "__main__":
    main()