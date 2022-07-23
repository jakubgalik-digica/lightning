# Copyright The PyTorch Lightning team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from os import environ

from pytorch_lightning.loggers.base import (  # LightningLoggerBase imported for backward compatibility
    LightningLoggerBase,
)
from pytorch_lightning.loggers.csv_logs import CSVLogger
from pytorch_lightning.loggers.logger import Logger, LoggerCollection
from pytorch_lightning.loggers.tensorboard import TensorBoardLogger

__all__ = ["CSVLogger", "LightningLoggerBase", "Logger", "LoggerCollection", "TensorBoardLogger"]

from pytorch_lightning.loggers.comet import _COMET_AVAILABLE, CometLogger  # noqa: F401
from pytorch_lightning.loggers.mlflow import MLFlowLogger  # noqa: F401
from pytorch_lightning.loggers.neptune import NeptuneLogger  # noqa: F401
from pytorch_lightning.loggers.wandb import WandbLogger  # noqa: F401

if _COMET_AVAILABLE:
    __all__.append("CometLogger")
    # needed to prevent ModuleNotFoundError and duplicated logs.
    environ["COMET_DISABLE_AUTO_LOGGING"] = "1"
