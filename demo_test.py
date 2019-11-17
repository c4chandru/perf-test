from locust import HttpLocust, TaskSet, task
import os
import csv
from uuid import uuid4
import random

token_data = './tokenData.csv'


class LoadTestTask(TaskSet):

    def __init__(self, parent):
        super(LoadTestTask, self).__init__(parent)
        self.task_id = "TASK-{}".format(uuid4())

        with open(token_data) as txn_file:
            token_reader = csv.reader(txn_file, delimiter=',', quotechar='|')
            self.token_list = list(token_reader)

    def on_start(self):
        print self.task_id

    @task(1)
    def play(self):

        value = random.choice(self.token_list)

        sid = value[0]

        print(sid)

        endpoint = ":8001/game/play"

        headers = {"Content-Type": "application/json"}

        body = {
            "g": "epicjoker",
            "sid": sid,
            "ba": 2500,
            "ga": "spin"
        }

        with self.client.post(endpoint, headers=headers, json=body,
                              name="Play", catch_response=True) as response:

            if response.status_code == 200:
                response.success()
                print response.status_code
            else:
                print response.status_code
                return False


class WebsiteUser(HttpLocust):
    host = os.getenv('TARGET_URL', "https://api.relaxg.net")
    task_set = LoadTestTask
    min_wait = 3
    max_wait = 5