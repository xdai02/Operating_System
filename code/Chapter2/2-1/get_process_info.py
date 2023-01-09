import psutil

def main():
    for process in psutil.process_iter():
        print("[Process] id=%d, name=%s, created=%s" % (
            process.pid, process.name,
            process.create_time())
        )

if __name__ == "__main__":
    main()