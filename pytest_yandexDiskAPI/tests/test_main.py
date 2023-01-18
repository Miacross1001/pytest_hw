import pytest
from main import API_disk

@pytest.mark.parametrize(
    "x, result", [
        ('112', '<Response [201]>')
    ]
)
def test_yandexDiskAPI(x, result):
    res = API_disk(x)
    assert res != result #Create folder