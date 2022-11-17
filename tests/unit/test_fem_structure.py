from app.domain.model.fem_structure import FEM, Node
import pytest


def test_create_node():
    n = Node(id=11, x=1.0, z=12.0)
    assert n.id == 11
    assert n.x == 1.0
    assert n.y == 0.0
    assert n.z == 12.0


def test_add_node():
    m = FEM()
    m.create_node(id=11, x=1.0, z=12.0)


def test_add_element():
    m = FEM()
    m.create_element(id=11, nodes=[12, 13, 14, 15])


def test_create_nodes_from_list():
    m = FEM()
    node_list = [11, 12, 13, 14, 15, 16, 17, 18]
    m.create_nodes(node_list)
    for nid in node_list:
        assert nid in m.nodes


def test_create_nodes_from_number():
    m = FEM()
    number = 12
    m.create_nodes(number)
    assert len(m.nodes) == number


@pytest.fixture()
def model() -> FEM:
    m = FEM()
    m.create_nodes(8)
    m.add_element(id=101, nodes=[1, 2, 3, 4, 5, 6, 7, 8])
    return m


# def test_affect_material_to_elements(model):
#     mat = Material()

# def test_get_cdg_without_material(model):
#     mat = Material()
#     model.add_material
#     pass


# def test_get_cdg_with_unique_material():
#     pass


# def test_get_cdg_with_two_materials():
#     pass


# def test_get_element_type():
#     assert Element(id=1, nodes=[11, 12, 13, 14]).type == "TETRA"
#     assert Element(id=1, nodes=[11, 12, 13, 14, 15]).type == "PYRA"
#     assert Element(id=1, nodes=[11, 12, 13, 14, 15, 16]).type == "PENTA"
#     assert Element(id=1, nodes=[11, 12, 13, 14, 15, 16, 17, 18]).type == "HEXA"
