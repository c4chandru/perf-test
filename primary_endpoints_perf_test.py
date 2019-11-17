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
        print(self.task_id)

    @task(1)
    def ping_post(self):
        '''
        This methdod to check the status of the play post play call
        should return 200 status code
        '''

        value = random.choice(self.token_list)

        sid = value[0]

        endpoint = ":8001/game/ping"

        headers = {"Content-Type": "application/json"}

        body = {
            "sid": sid
        }

        with self.client.post(endpoint, headers=headers, json=body,
                              name="ping_post", catch_response=True) as response:

            if response.status_code == 200:
                response.success()
                print(response.status_code)
            else:
                print(response.status_code)
                return False

    @task(1)
    def ping_options(self):

        '''
        This methdod to check the status of the play post play call
        should return 204 status code
        '''
        value = random.choice(self.token_list)

        sid = value[0]


        endpoint = ":8001/game/ping"

        headers = {"Content-Type": "application/json"}

        body = {
            "sid": sid
        }

        with self.client.options(endpoint, headers=headers, json=body,
                              name="ping_options", catch_response=True) as response:

            if response.status_code == 200 or 204:
                response.success()
                print(response.status_code)
            else:
                print(response.status_code)
                return False

    @task(1)
    def setrestorestate_options(self):

        '''
        This methdod to check the status of the play post play call
        should return 204 status code
        '''

        value = random.choice(self.token_list)

        sid = value[0]

        endpoint = ":8001/game/setrestorestate"

        headers = {"Content-Type": "application/json"}

        body = {
            "sid": sid
        }

        with self.client.options(endpoint, headers=headers, json=body,
                                 name="setrestorestate_options", catch_response=True) as response:

            if response.status_code == 200 or 204:
                response.success()
                print(response.status_code)
            else:
                print(response.status_code)
                return False

    @task(1)
    def setrestorestate_post(self):

        '''
        This methdod to check the status of the play post play call
        should return 200 status code
        '''

        value = random.choice(self.token_list)

        sid = value[0]

        endpoint = ":8001/game/setrestorestate"

        headers = {"Content-Type": "application/json"}

        body = {
            "sid": sid
        }

        with self.client.post(endpoint, headers=headers, json=body,
                                 name="setrestorestate_post", catch_response=True) as response:

            if response.status_code == 200:
                response.success()
                print(response.status_code)
            else:
                print(response.status_code)
                return False


class WebsiteUser(HttpLocust):
    host = os.getenv('TARGET_URL', "https://api.relaxg.net")
    task_set = LoadTestTask
    min_wait = 3
    max_wait = 5