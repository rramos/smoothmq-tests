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
go run .
```

Then create a new queue **text-queue** when going to <http://localhost:3000>

And execute the test script that will create a new message on that queue

```sh
python test.py
```

## References ##

* https://github.com/poundifdef/SmoothMQ
