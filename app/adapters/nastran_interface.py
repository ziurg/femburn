"""
Module permettant le chargement d'un modèle FEM au format Nastran, composé d'éléments tétraédriques.
"""

from app.domain.model.fem_structure import FEM
from app.domain.ports.model_interface import ModelInterface
from typing import List


def split_by_8(text: str, chunk_size: int = 8) -> List[str]:
    return [text[i : i + chunk_size] for i in range(0, len(text), chunk_size)]


class NastranParser(ModelInterface):
    def load(self, model: FEM, file: str) -> FEM:
        """Read an MSC Nastran bulk file

        Args:
            file (str): path to the file to parse.

        Returns:
            Structure: Finite Element Model of the structure

        Notes:
            This is a function example not really loading Nastran
            files, but only files with nodes written in the
            following format :
            1, 12.3, 5.4, -0.3
            2, -10., 5.3, 8.2
        """
        with open(file, "r") as f:
            lines = (line.strip() for line in f.readlines())
            lines = (line for line in lines if line)
            for line in lines:
                fields = map(str.strip, split_by_8(line))
                [name, field1, _, field3, field4, field5, *_] = fields
                if name == "GRID":
                    model.create_node(
                        id=int(field1),
                        x=float(field3),
                        y=float(field4),
                        z=float(field5),
                    )
                elif name == "CTRIA3":
                    model.create_element(
                        id=int(field1), nodes=[int(field3), int(field4), int(field5)]
                    )
        return model
