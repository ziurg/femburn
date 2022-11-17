import pytest
import shutil
from os.path import dirname


@pytest.fixture(scope="module")
def nastran_file(tmpdir_factory):
    txt = (
        "GRID    12              0.12    15      -0.91   \n"
        "GRID    13              -16.0   -4      0.0     \n"
        "GRID    14              8.4     15      3.2     \n"
        "CTRIA3  1               12      13      14      \n"
    )
    file_ = tmpdir_factory.mktemp("data").join("nastran_example.bdf")
    print("file : {}".format(str(file_)))
    with file_.open("w") as f:
        f.write(txt)
    yield file_
    print("delete : {}".format(str(dirname(dirname(file_)))))
    shutil.rmtree(dirname(dirname(file_)), ignore_errors=True)
