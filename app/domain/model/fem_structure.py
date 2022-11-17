from dataclasses import dataclass
from typing import TYPE_CHECKING, Dict, List, Optional, Union
from functools import singledispatchmethod

if TYPE_CHECKING:
    from app.domain.ports.model_interface import ModelInterface


@dataclass
class Element:
    id: int
    nodes: List[int]

    def __contains__(self, nid: int) -> bool:
        return nid in self.nodes


@dataclass
class Node:
    id: int
    x: Optional[float] = 0.0
    y: Optional[float] = 0.0
    z: Optional[float] = 0.0


@dataclass
class FEM:
    """Element Finite Model for 3D elements"""

    nodes: Optional[Dict[int, Node]] = None
    elements: Optional[Dict[int, Element]] = None

    def __post_init__(self):
        self.nodes = {}
        self.elements = {}

    def create_node(self, **kwarg) -> None:
        n = Node(**kwarg)
        self.nodes[n.id] = n

    def create_element(self, **kwarg) -> None:
        e = Element(**kwarg)
        self.elements[e.id] = e

    @singledispatchmethod
    def create_nodes(self, item: Union[int, list]):
        raise NotImplementedError

    @create_nodes.register(int)
    def _(self, number: int) -> None:
        """Crée le nombre de noeuds demandé.

        Parameters
        ----------
        number : int
            nombre de noeuds à créer
        """
        for _ in range(number):
            try:
                free_id = max(self.nodes.keys()) + 1
            except ValueError:  # Empty nodes
                free_id = 1
            self.nodes[free_id] = Node(id=free_id)

    @create_nodes.register(list)
    def _(self, nodes: List[int]) -> None:
        """Crée des noeuds à partir d'une liste d'identifiants

        Parameters
        ----------
        nodes : List[int]
            liste d'identifiants
        """
        for nid in nodes:
            self.nodes[nid] = Node(id=nid)

    @singledispatchmethod
    def __contains__(self, _) -> bool:
        raise NotImplementedError("This object type is not valid for this method.")

    @__contains__.register(Node)
    def _(self, n: Node) -> bool:
        return n.id in self.nodes

    @__contains__.register(Element)
    def _(self, e: Element) -> bool:
        return e.id in self.elements

    def load(self, fem_interface: "ModelInterface", file: str):
        return fem_interface.load(self, file)
