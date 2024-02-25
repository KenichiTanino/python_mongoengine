#!/usr/bin/env python

# データ表示/追記(Process B)

import datetime
import random
from time import sleep

from mongoengine import connect

from models import User, UserState


def remove_randome_object():
    count = User.objects.count()
    del_index = randome.randint(0, count)
    for index, u in enumerate(User.objects):
        if index != del_index:
            continue
        u.delete()


def main():

    connect('user_table')

    print("start B")

    while(1):

        for u in User.objects:
            now = datetime.datetime.now()
            if u.user_state:
                print(f"B: t: {now} e_id: {u.e_id} uuid: {u.uuid} state: {u.user_state.state}")
            else:
                print(f"B: t: {now} e_id: {u.e_id} uuid: {u.uuid} state: {u.user_state}")

            # num: 1 データ追記
            num = random.randint(0, 1)
            if not u.e_id:
                continue
            if num == 0:
                print(f"B: t: {now} e_id: {u.e_id} uuid: {u.uuid} now write state")
                us = UserState(state="RUN")
                u.user_state = us
                u.user_state.save()
                u.save()

        # sleep(5)


if __name__ == '__main__':
    main()