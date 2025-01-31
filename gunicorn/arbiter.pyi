import socket
from signal import Signals
from types import FrameType
from typing import TYPE_CHECKING, Any, Dict, List, Tuple

from _typeshed import Incomplete

from gunicorn import SERVER_SOFTWARE, __version__, sock, systemd, util
from gunicorn.app.base import BaseApplication
from gunicorn.errors import AppImportError, HaltServer
from gunicorn.pidfile import Pidfile

if TYPE_CHECKING:
    from gunicorn.workers.base import Worker

class Arbiter:
    WORKER_BOOT_ERROR: int
    APP_LOAD_ERROR: int
    START_CTX: dict[Any, Any]
    LISTENERS: list[Any]
    WORKERS: dict[int, Worker]
    PIPE: list[tuple[int, int]]
    SIG_QUEUE: list[Any]
    SIGNALS: Incomplete
    SIG_NAMES: Incomplete
    log: Incomplete
    pidfile: Incomplete
    systemd: bool
    worker_age: int
    reexec_pid: int
    master_pid: int
    master_name: str
    def __init__(self, app: BaseApplication) -> None: ...
    num_workers: Incomplete
    app: BaseApplication
    cfg: Incomplete
    worker_class: Incomplete
    address: Incomplete
    timeout: Incomplete
    proc_name: Incomplete
    def setup(self, app: BaseApplication) -> None: ...
    pid: int
    def start(self) -> None: ...
    def init_signals(self) -> None: ...
    def signal_(self, sig: Signals, frame: FrameType | None) -> None: ...
    def run(self) -> None: ...
    def handle_chld(self, sig: Signals, frame: FrameType | None) -> None: ...
    def handle_hup(self) -> None: ...
    def handle_term(self) -> None: ...
    def handle_int(self) -> None: ...
    def handle_quit(self) -> None: ...
    def handle_ttin(self) -> None: ...
    def handle_ttou(self) -> None: ...
    def handle_usr1(self) -> None: ...
    def handle_usr2(self) -> None: ...
    def handle_winch(self) -> None: ...
    def maybe_promote_master(self) -> None: ...
    def wakeup(self) -> None: ...
    def halt(self, reason: Incomplete | None = ..., exit_status: int = ...) -> None: ...
    def sleep(self) -> None: ...
    def stop(self, graceful: bool = ...) -> None: ...
    def reexec(self) -> None: ...
    def reload(self) -> None: ...
    def murder_workers(self) -> None: ...
    def reap_workers(self) -> None: ...
    def manage_workers(self) -> None: ...
    def spawn_worker(self) -> None: ...
    def spawn_workers(self) -> None: ...
    def kill_workers(self, sig: Signals) -> None: ...
    def kill_worker(self, pid: int, sig: Signals) -> None: ...
