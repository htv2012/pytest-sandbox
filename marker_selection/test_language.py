import pytest


@pytest.mark.parametrize(
    "language",
    [
        pytest.param("en", marks=[pytest.mark.license(license_kind="individual")]),
        pytest.param("fr", marks=[pytest.mark.license(license_kind="trial")]),
        pytest.param("it", marks=[pytest.mark.license(license_kind="enterprise")]),
    ],
)
def test_lang(language, request):
    pass
