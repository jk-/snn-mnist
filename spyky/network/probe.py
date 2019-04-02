from abc import ABC, abstractmethod
from typing import NoReturn, Union, Iterable
from spyky.network import AbstractLayer, AbstractConnection


class AbstractProbe(ABC):
    def __init__(self) -> NoReturn:
        super().__init__()

    @abstractmethod
    def get(self) -> NoReturn:
        pass

    @abstractmethod
    def save(self) -> NoReturn:
        psas

    @abstractmethod
    def reset(self) -> NoReturn:
        pass


class Probe:
    def __init__(
        self,
        target: Union[AbstractLayer, AbstractConnection],
        vars: Iterable[str],
    ) -> NoReturn:
        pass
