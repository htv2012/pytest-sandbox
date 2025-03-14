import pytest


def pytest_generate_tests(metafunc: pytest.Metafunc):
    print("\n\n# Explore Metafunc")
    for name in dir(metafunc):
        if name.startswith("_"):
            continue
        obj = getattr(metafunc, name)
        if callable(obj):
            print(f"  - {name}()")
        else:
            print(f"  - {name}: {obj.__class__.__name__}")
    print()
