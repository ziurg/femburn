from app.domain.model.fem_structure import FEM, Node, Element
from app.adapters.nastran_interface import NastranParser


def test_load_nastran_grid_and_ctria3(nastran_file):
    """Test Basic nastran file loading.

    Given a Nastran file containing GRID and CTRIA3 element.

    When load the file

    Then we get a Finite Element Model with corresponding nodes and elements

    Parameters
    ----------
    nastran_file : fixture
        temporary file create in conftest.py
    """
    ni = NastranParser()
    model = FEM()
    model.load(ni, nastran_file)
    assert model.nodes == {
        12: Node(id=12, x=0.12, y=15.0, z=-0.91),
        13: Node(id=13, x=-16.0, y=-4.0, z=0.0),
        14: Node(id=14, x=8.4, y=15.0, z=3.2),
    }
    assert model.elements == {1: Element(id=1, nodes=[12, 13, 14])}
