"""
Module servant à l'inversion de dépendances.
"""

import abc
from app.domain.model.fem_structure import FEM


class ModelInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def load(self, model: FEM, file: str) -> FEM:
        raise NotImplementedError
