import pytest


FUNCTIONAL = 'functional'


def pytest_addoption(parser):
    parser.addoption(
        f'--{FUNCTIONAL}', action='store_true', default=False, help=f"enable {FUNCTIONAL} tests"
    )
 

def pytest_configure(config):
    config.addinivalue_line("markers", f"{FUNCTIONAL}")


def pytest_collection_modifyitems(config, items):
    if config.getoption(f"--{FUNCTIONAL}"):
        return
    skip_mark = pytest.mark.skip(reason=f"need --{FUNCTIONAL} option to run")
    for item in items:
        if FUNCTIONAL in item.keywords:
            item.add_marker(skip_mark)
