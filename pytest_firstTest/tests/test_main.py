import pytest

from main import set_func, max_key, foo

@pytest.mark.parametrize(
    "x, result", [
        ({'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}, {98, 35, 15, 213, 54, 119})
    ]
)
def test_set_func(x, result):
    res = set_func(x)
    assert res == result

@pytest.mark.parametrize(
    "x, result", [
        ({'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}, 'yandex')
    ]
)
def test_max_key(x, result):
    res = max_key(x)
    assert res == result

@pytest.mark.parametrize(
    "x, result", [
        (['2018-01-01', 'yandex', 'cpc', 100], {'2018-01-01': {'yandex': {'cpc': 100}}})
    ]
)
def test_foo(x, result):
    res = foo(x)
    assert res == result

