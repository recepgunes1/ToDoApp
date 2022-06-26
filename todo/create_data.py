from datetime import datetime, timedelta
from random import randint

from todo.helpers import create_md5
from todo.models import User, Task


def create_users():
    list_of_users = []
    list_of_first_name = ['john', 'jack', 'zack', 'natasha', 'alev', 'buse', 'raymond', 'refik', 'katarina', 'nolan']
    list_of_last_name = ['smith', 'brown', 'kubric', 'tarantino', 'quentin']
    mail_template = 'user{}@mail.com'
    plain_password = '123456'
    hashed_password = create_md5(plain_password)
    for i in range(10):
        new_user = User(first_name=list_of_first_name[i], last_name=list_of_last_name[i % 5],
                        email=mail_template.format(str(i + 1)), password=hashed_password)
        list_of_users.append(new_user)
    return list_of_users


def create_tasks():
    list_of_tasks = []
    list_of_title = ['Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
                     'Aenean laoreet ipsum nec risus feugiat eleifend.',
                     'Proin ut ligula eget sem placerat convallis at vel tellus.',
                     'Nullam feugiat odio at est egestas, id tristique ante lacinia.',
                     'Sed a ligula in turpis commodo tempus et vitae magna.',
                     'Praesent iaculis odio ut mi porta, vitae facilisis elit tempor.',
                     'Vivamus sollicitudin sapien at lectus faucibus interdum.',
                     'In dictum turpis ut tempor vestibulum.',
                     'Nulla ac nisl eleifend, interdum magna ut, vestibulum enim.',
                     'Suspendisse ac magna consectetur, varius odio a, iaculis purus.',
                     'Phasellus a ligula quis justo rhoncus gravida at ut augue.',
                     'Quisque euismod urna in ipsum consequat finibus.']
    content = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut volutpat quis lacus at posuere. ' \
              'Vivamus nec nunc non ex posuere euismod. Donec accumsan risus id euismod fermentum. Duis nec purus diam. ' \
              'Sed sagittis tristique nisl, quis luctus justo posuere eu. Vestibulum sit amet feugiat mi. ' \
              'Donec id sapien tristique, congue nisl eu, fermentum quam. ' \
              'Vivamus arcu turpis, porttitor venenatis urna sed, viverra interdum magna. ' \
              'Donec metus risus, vulputate sed malesuada eu, sagittis id mauris. Nullam vulputate rhoncus imperdiet. ' \
              'Vestibulum tempor leo nisi, at tempor dui feugiat gravida. Maecenas ac commodo risus. ' \
              'Sed tincidunt hendrerit eros. ' \
              'Proin facilisis nulla non est rhoncus cursus. ' \
              'Ut lacinia sollicitudin quam, non imperdiet nibh porta quis.'
    list_of_status = ['idle', 'completed', 'deleted', 'gave_up']
    for i in range(100):
        status = list_of_status[randint(0, 3)]
        if status == 'completed':
            new_task = Task(title=list_of_title[randint(0, 10)], content=content, status=status,
                            expected_dead_line=datetime.now() + timedelta(randint(0, 365)),
                            ended_date=datetime.now() + timedelta(randint(0, 100)),
                            owner_id=randint(1, 11))
            list_of_tasks.append(new_task)
        else:
            new_task = Task(title=list_of_title[randint(0, 10)], content=content, status=status,
                            expected_dead_line=datetime.now() + timedelta(randint(0, 365)), owner_id=randint(1, 10))
            list_of_tasks.append(new_task)
    return list_of_tasks