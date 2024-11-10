# README.md #

Sample repo fo testing SmoothMQ

## Requirements ##

* Python 
* boto3
* SmoothMQ

## Install ##

```sh
pip install -r requirements.txt
```

## Run ##

Start SmoothMQ

```sh
cd SmoothMQ/
go run . server
```
You should get some info at the end like...

```sh
...
Development SQS credentials:
    Access Key: DEV_ACCESS_KEY_ID
    Secret Key: DEV_SECRET_ACCESS_KEY

SQS Endpoint: http://localhost:3001
Dashboard: http://localhost:3000

```

## Create mock AWS credentials file ##

Create the file `~/.aws/credentials` with the folowing content

```sh
[default]
aws_access_key_id=DEV_ACCESS_KEY_ID
aws_secret_access_key=DEV_ACCESS_KEY_KEY
region=us-west-1

```

## Write a message to the queue ##

Then create a new queue **test-queue** when going to <http://localhost:3000>

And execute the test script that will create a new message on that queue

```sh
python test.py
```

## References ##

* https://github.com/poundifdef/SmoothMQ

