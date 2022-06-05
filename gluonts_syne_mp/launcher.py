import logging
from pathlib import Path

import numpy as np

from sagemaker.pytorch import PyTorch

from syne_tune.backend import LocalBackend, SageMakerBackend
from syne_tune.backend.sagemaker_backend.sagemaker_utils import get_execution_role
from syne_tune.optimizer.baselines import ASHA
from syne_tune.optimizer.schedulers import FIFOScheduler
from syne_tune import Tuner, StoppingCriterion
from syne_tune.config_space import loguniform, lograndint


if __name__ == "__main__":

    logging.getLogger().setLevel(logging.INFO)
    config_space = {
        "lr": loguniform(1e-4, 1e-1),
    }

    mode = "min"
    metric = "epoch_loss"

    if False:
        trial_backend = SageMakerBackend(
            sm_estimator=PyTorch(
                entry_point="mp_queue.py",
                source_dir=".",
                instance_type="local",
                instance_count=1,
                role=get_execution_role(),
                py_version="py38",
                framework_version="1.10.0",
                base_job_name="hpo-gluonts",
            ),
            metrics_names=[metric],
        )
    else:
        trial_backend = LocalBackend(entry_point="./mp_queue.py")

    scheduler = ASHA(
        config_space, max_t=10, resource_attr="epoch", mode="min", metric=metric
    )

    tuner = Tuner(
        trial_backend=trial_backend,
        scheduler=scheduler,
        stop_criterion=StoppingCriterion(max_num_trials_finished=10),
        n_workers=4,
        max_failures=1,
    )
    tuner.run()
