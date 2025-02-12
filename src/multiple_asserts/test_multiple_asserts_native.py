import pytest


@pytest.mark.parametrize(
    "json_data",
    [
        pytest.param({"key": "good afternoon!"}),
        pytest.param({}, marks=pytest.mark.xfail(reason="empty JSON object")),
        pytest.param(
            {"key": "good morning!", "evil key!": "i shouldn't be here!"},
            marks=pytest.mark.xfail(reason="evil key present"),
        ),
    ],
)
def test_multiple_assertions(json_data: dict):
    actual = {
        "key is present": "key" in json_data,
        "key value is": json_data.get("key"),
        "evil key is missing": "evil key!" not in json_data,
    }

    expected = {
        "key is present": True,
        "key value is": "good afternoon!",
        "evil key is missing": True,
    }

    assert expected == actual
