import pytest


@pytest.fixture(
    scope="module",
    params=[
        pytest.param({"amount": 25.1, "tax": 0.108, "total": 27.8108}, id="passing"),
        pytest.param({}, id="empty dict"),
        pytest.param({"amount": 25.1, "tax": 0.18, "total": None}, id="tax too high"),
    ],
)
def obj(request):
    """Object under test"""
    return request.param


def test_obj_structure(obj):
    assert isinstance(obj, dict)
    assert len(obj) == 3


@pytest.mark.depends_on("test_obj_structure")
def test_amount(obj):
    assert "amount" in obj
    assert isinstance(obj["amount"], float)


@pytest.mark.depends_on("test_obj_structure")
def test_tax(obj):
    assert "tax" in obj
    assert isinstance(obj["tax"], float)
    assert obj["tax"] < 0.15  # Tax should be less than 15%


@pytest.mark.depends_on("test_amount", "test_tax")
def test_total(obj):
    assert "total" in obj
    assert obj["amount"] * (1 + obj["tax"]) == obj["total"]
