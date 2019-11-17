import requests
token_data = './tokenData.csv'


class Token:

    def __init__(self):

        self.url = "https://api.relaxg.net"
        self.gameref = "epicjoker"
        self.ticket = "testticket-priit3"
        self.partnerid = "1"
        self.mode = "dev"
        self.channel = "web"
        self.clientid = ""

    def get_token(self):
        '''
        In this method token and user id is created and returned from post call.
        It is passed to generate session_id
        '''

        end_point = self.url+"/capi/1.0/casino/token/gettoken"

        headers = {"Content-Type":"application/json"}

        body= {
            "gameref":self.gameref,
            "ticket":self.ticket,
            "partnerid":self.partnerid,
            "mode":self.mode,
            "channel":self.channel,
            "clientid":self.clientid
        }

        response = requests.post(end_point, headers =headers, json=body)
        temp = response.json()
        user_id = temp['response']['userid']
        token = temp['response']['token']

        return user_id, token

    def get_session_id(self):

        '''
        Here session id i.e sid is generated using user_id and token
        from /gettoken endpoint's response
        '''

        data = Token()
        user_id = data.get_token()[0]
        token = data.get_token()[1]

        session_endpoint = self.url+":8001/game/rmlogin"

        headers = {"Content-Type":"application/json"}

        body = {
            "token": token,
            "userid": user_id,
            "mode": self.mode,
            "partnerid": self.partnerid,
            "channel": self.channel,
            "clientid": "",
            "g": self.gameref,
            "immediatePayouts":"false"
        }

        response = requests.post(session_endpoint, headers=headers, json=body)
        res_data = response.json()
        sid = res_data['sid']

        return sid

    def generate_session_id(self):

        '''
        In this method we can create a file with Static session id's that are needed for the perf test
        of all the endpoints,to avoid time complexity as while running the perf we are adding it to a csv file
        '''

        token = []

        data = Token()

        for x in range(10):

            x = data.get_session_id()
            token.append(x)

        with open('tokenData.csv', 'w') as csvfile:
            for item in token:
                csvfile.write(item + '\n')


data = Token()
data.generate_session_id()
