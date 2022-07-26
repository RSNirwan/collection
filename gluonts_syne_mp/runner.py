from argparse import ArgumentParser
from collections import defaultdict
import logging
import multiprocessing as mp

from gluonts.model.deepar import DeepAREstimator
from gluonts.dataset.repository.datasets import get_dataset
from gluonts.mx import Trainer
from gluonts.evaluation import make_evaluation_predictions, Evaluator

from gluonts.mx.trainer.callback import Callback
from gluonts.core.component import validated
from syne_tune.report import Reporter

import numpy as np


class CB(Callback):
    @validated()
    def __init__(self, queue):
        self.queue = queue

    def on_epoch_end(self, epoch_no, epoch_loss, *args, **kwargs):
        self.queue.put((epoch_no, epoch_loss))
        return True


def run_deepar(queue, lr):
    dataset = get_dataset("m4_hourly")
    model = DeepAREstimator(
        freq=dataset.metadata.freq,
        prediction_length=dataset.metadata.prediction_length,
        trainer=Trainer(epochs=10, learning_rate=lr, callbacks=[CB(queue)]),
    )
    predictor = model.train(dataset.train)
    queue.put((-1, 0))


def syne_reporter(queue, num_senders):
    report = Reporter()
    di = defaultdict(list)
    while True:
        event = queue.get()
        di[event[0]].append(event[1])
        if -1 in di and len(di[-1]) == num_senders:
            return
        for k in list(di.keys()):
            if len(di[k]) == num_senders:
                report(epoch=k + 1, epoch_loss=np.mean(di.pop(k)))


def run_inner(lr):
    queue = mp.Queue()
    num_sender = 5
    processes = []
    for i in range(num_sender):
        p = mp.Process(target=run_deepar, args=(queue, lr))
        p.start()
        processes.append(p)
    rec = mp.Process(target=syne_reporter, args=(queue, num_sender))
    rec.start()

    for p in processes:
        p.join()
    rec.join()


if __name__ == "__main__":
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    parser = ArgumentParser()
    parser.add_argument("--lr", type=float, default=0.001)
    args, _ = parser.parse_known_args()
    run_inner(args.lr)
