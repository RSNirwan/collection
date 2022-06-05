from collections import defaultdict
import multiprocessing as mp

import numpy as np


def sender(queue, num):
    n = 10
    for i in range(n):
        val = np.random.normal(0, 1)
        queue.put((num, i, val))
    queue.put((num, -1, "done"))

def receiver(queue, num_sender):
    di = defaultdict(list)
    while True:
        event = queue.get()
        print(f"received event: {event}")
        di[event[1]].append(event[2])
        if -1 in di and len(di[-1])==num_sender:
            return
        for k in list(di.keys()):
            if len(di[k]) == num_sender:
                print(f"average {k}: {np.mean(di.pop(k))}")


def run_inner():
    queue = mp.Queue()
    num_sender = 5
    processes = []
    for i in range(num_sender):
        p = mp.Process(target=sender, args=(queue, i))
        p.start()
        processes.append(p)
    rec = mp.Process(target=receiver, args=(queue, num_sender))
    rec.start()

    for p in processes:
        p.join()
    rec.join()


if __name__ == "__main__":
    #with mp.Pool(2) as p:
        #p.map(run, [[],[]])
    run_inner()
