# Perf-test
Epic Joker

If you do not have python set up in your system

# Install Python

```shell
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

```shell
easy_install pip
```

# Install locust

```shell
pip install locustio
```

# Perf test setup and run
Now clone the repo and run the below commands
```shell
cd perf-test
```

Firstly we have to generate the session_id to run the perf test on all the endpoints
to obtain that run the below

```shell
python session_id_generator.py
```

wait for 5 secs as csv file will be created 

```shell
locust -f play_perf_test.py
```

after running this you will see the below in the terminal
```
[2019-11-18 02:29:36,947] Chandru.local/INFO/locust.main: Starting web monitor at *:8089
[2019-11-18 02:29:36,947] Chandru.local/INFO/locust.main: Starting Locust 0.9.0

```

open the below url in the web browser

```bash
http://localhost:8089/
```

start will less users data and with hatch rate of 10sec by entering 10 in number of user to simulate and enter 10 in 
hatch rate field

dashboard will display the RPS with respective to the data

stop the run and kill the process from the terminal run the below command for rest of the tests

```shell
locust -f primary_endpoints_perf_test.py
```

Here in this framework we can achieve higher request by connecting as master and slaves using cluster connect

##To get 100RPS(Request per second)
```bash
Enter number of user to simulate = 100
Enter hatch rate = 20

```




