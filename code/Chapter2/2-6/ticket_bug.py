import multiprocessing
import time

def sell_ticket(dict):
    while True:
        # get the number of tickets left
        num = dict.get("ticket")
        
        if num > 0:
            time.sleep(1)   # simulate the time of selling a ticket
            num -= 1
            print("[Ticket Machine %d] Ticket sold. Ticket remaining: %d" % (
                multiprocessing.current_process().pid,
                num
            ))
            dict.update({"ticket":num})
        else:                               # no tickets left
            break

def main():
    # shared memory manager
    manager = multiprocessing.Manager()
    # dictionary shared by multiple processes
    ticket_dict = manager.dict(ticket=5)

    sellers = [
        multiprocessing.Process(
            target=sell_ticket, args=(ticket_dict,)
        ) 
        for _ in range(5)
    ]

    for seller in sellers:
        seller.start()
    for seller in sellers:
        seller.join()

if __name__ == "__main__":
    main()