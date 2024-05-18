from argparse import ArgumentParser, Namespace

from _typeshed import Incomplete
from _typeshed.wsgi import WSGIApplication as _WSGIApplication

from gunicorn import debug as debug
from gunicorn import util as util
from gunicorn.arbiter import Arbiter as Arbiter
from gunicorn.config import Config
from gunicorn.config import get_default_config_file as get_default_config_file

# from abc import abstractmethod, ABCMeta

class BaseApplication:
    usage: str | None
    cfg: Config
    callable: None | _WSGIApplication
    prog: str | None
    logger: Incomplete
    def __init__(self, usage: str | None = ..., prog: str | None = ...) -> None: ...
    def do_load_config(self) -> None: ...
    def load_default_config(self) -> None: ...
    def init(
        self, parser: ArgumentParser, opts: Namespace, args: list[str]
    ) -> None: ...
    def load(self) -> _WSGIApplication: ...
    def load_config(self) -> None: ...
    def reload(self) -> None: ...
    def wsgi(self) -> _WSGIApplication: ...
    def run(self) -> None: ...

class Application(BaseApplication):
    def chdir(self) -> None: ...
    def get_config_from_filename(self, filename: str) -> Config: ...
    def get_config_from_module_name(self, module_name: str) -> Config: ...
    def load_config_from_module_name_or_filename(self, location: str) -> Config: ...
    def load_config_from_file(self, filename: str) -> Config: ...
    def load_config(self) -> None: ...
    def run(self) -> None: ...
