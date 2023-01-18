

x_ = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}
def set_func(x):
    ids = x

    set_list = []

    for value in ids.values():
      for num in value:
        set_list.append(num)
    return set(set_list)

y_ = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
def max_key(y):
    stats = y

    max = 0
    key_max = ''

    for key, value in stats.items():
      if value > max:
        max = value
        key_max = key

    return key_max

z_ = ['2018-01-01', 'yandex', 'cpc', 100]
def foo(z):
    test_list = z
    test_dict = test_list[-1]

    for elem in test_list[-2::-1]:
        test_dict = {elem: test_dict}

    return test_dict
