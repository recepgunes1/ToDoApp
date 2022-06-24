from datetime import datetime
from hashlib import md5


def create_md5(plain: str) -> str:
    return md5(plain.encode()).hexdigest()


def convert_to_date(string: str) -> datetime:
    return datetime.strptime(string, '%Y-%m-%d')
