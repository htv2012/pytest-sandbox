import pytest


def _verify_even(n):
    assert n % 2 == 0, "Even test"


def _verify_positive(n):
    assert n > 0, "Positive test"


@pytest.mark.xfail(reason="Failed for demo only")
def test_value():
    value = -5
    errors = []
    for check in [_verify_even, _verify_positive]:
        try:
            check(value)
        except AssertionError as error:
            errors.append(error)

    if errors:
        msg = "\n".join(str(e) for e in errors)
        msg = f"\n{msg}"
        pytest.fail(msg)
