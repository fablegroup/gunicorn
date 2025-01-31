from typing import TYPE_CHECKING

from _typeshed import Incomplete

from gunicorn import util

if TYPE_CHECKING:
    from gunicorn.config import Config

PLATFORM: str
IS_CYGWIN: bool

class WorkerTmp:
    def __init__(self, cfg: Config) -> None: ...
    def notify(self) -> None: ...
    def last_update(self) -> float: ...
    def fileno(self) -> int: ...
    def close(self) -> None: ...
