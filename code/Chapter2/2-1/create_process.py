import multiprocessing

def worker():
    print("[Process] id=%d, name=%s" % (
        multiprocessing.current_process().pid,
        multiprocessing.current_process().name)
    )

def main():
    print("[Main Process]id=%d, name=%s" % (
        multiprocessing.current_process().pid,
        multiprocessing.current_process().name)
    )
    
    for i in range(3):
        process = multiprocessing.Process(target=worker, name="Process %d" % i)
        process.start()

if __name__ == "__main__":
    main()