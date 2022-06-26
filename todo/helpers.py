from collections import OrderedDict
from datetime import datetime
from hashlib import md5
from os import remove
from os.path import exists

import matplotlib.pyplot as plt

from todo.config import Config


def create_md5(plain: str) -> str:
    return md5(plain.encode()).hexdigest()


def convert_to_date(string: str) -> datetime:
    return datetime.strptime(string, '%Y-%m-%d')


def draw_plot(data: dict, uid: int):
    data = OrderedDict(sorted(data.items()))
    path = f'{Config.STATIC_FOLDER}/images/{uid}.png'
    if exists(path):
        remove(path)
    status = list(map(lambda x: x.upper(), data.keys()))
    values = list(data.values())
    plt.bar(status, values, color=['green', 'red', 'gray', 'cyan'])
    plt.savefig(path)
    plt.close()


def is_password_safe(password: str) -> tuple:
    if 3 >= len(password):
        return False, 'Password must be at least 4 character.'
    if password.isnumeric():
        return False, 'Password must contain letter.'
    if password.islower():
        return False, 'Password must contain at least 1 upper case.'
    if password.isupper():
        return False, 'Password must contain at least 1 lower case.'
    return True, 'Success'
