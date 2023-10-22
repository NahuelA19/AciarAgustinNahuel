import pytest
from sum_figures import sum_figures

@pytest.mark.parametrize("num, res",[
    (52,7),
    (1231,7),
    (77777777777,77),
    (43,7),
])
def test_cifras(num, res):
    assert sum_figures(num) == res