#!/usr/bin/env python

# データ保存(Process A)

import datetime
import random
from time import sleep

from mongoengine import connect
from uuid6 import uuid7

from models import User, UserState


def remove_randome_object():
    count = User.objects.count()
    del_index = random.randint(0, count)
    for index, u in enumerate(User.objects):
        if index != del_index:
            continue
        print(f"A: del e_id: {u.e_id} uuid: {u.uuid}")
        u.delete()
        return


def main():

    connect('user_table')

    print("start A")

    while(1):
        # num分のデータ生成、削除
        # 負数は削除
        num = random.randint(-3, 3)
        if num == 0:
            continue

        count = User.objects.count()
        # 削除するほどの個数がない場合は何もしない
        if num < 0 and count == 0:
            continue

        # 負(削除)
        if num < 0:
            for index in range(0, abs(num)):
                remove_randome_object()
        else:
            # 正(追加/更新)
            for index in range(0, abs(num)):
                e_id = random.randint(0, 30000)
                u = User.objects.filter(e_id=e_id)
                if u:
                    # 更新
                    print(f"A: update t: {now} e_id: {u.e_id} uuid: {u.uuid} state: {u.user_state.state}")
                    u.uuid = uuid7()
                    u.save()
                    continue
                # 新規追加
                us = UserState(state="NOT RUN")
                us.save()
                u = User(e_id=e_id, uuid=str(uuid7()), user_state=us)
                u.save()

        for u in User.objects:
            now = datetime.datetime.now()
            if u.user_state:
                print(f"A: t: {now} e_id: {u.e_id} uuid: {u.uuid} state: {u.user_state.state}")
            else:
                print(f"A: t: {now} e_id: {u.e_id} uuid: {u.uuid} state: {u.user_state}")

        # sleep(5)

if __name__ == '__main__':
    main()