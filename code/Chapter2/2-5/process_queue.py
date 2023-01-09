import multiprocessing
import time

def produce(queue):
    for item in range(3):
        time.sleep(2)
        data = "data-%d" % item
        print("[%s] Produced: %s" % (
            multiprocessing.current_process().name,
            data
        ))
        queue.put(data)

def consume(queue):
    while True:
        print("[%s] Consumed: %s" % (
            multiprocessing.current_process().name,
            queue.get()
        ))

def main():
    queue = multiprocessing.Queue()
    producer = multiprocessing.Process(
                target=produce, name="Producer",
                args=(queue,)
            )
    consumer = multiprocessing.Process(
                target=consume, name="Consumer",
                args=(queue,)
            )
    producer.start()
    consumer.start()

if __name__ == "__main__":
    main()