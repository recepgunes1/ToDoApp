from datetime import datetime
from hashlib import md5

import matplotlib.pyplot as plt

from todo.config import Config


def create_md5(plain: str) -> str:
    return md5(plain.encode()).hexdigest()


def convert_to_date(string: str) -> datetime:
    return datetime.strptime(string, '%Y-%m-%d')


def draw_plot(data: dict, uid: int):
    status = list(map(lambda x: x.upper(), data.keys()))
    values = list(data.values())
    plt.bar(status, values, color=['blue', 'green', 'red', 'gray'])
    plt.savefig(f'{Config.STATIC_FOLDER}/images/{uid}.png')
