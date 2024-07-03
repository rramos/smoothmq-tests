import boto3

sqs = boto3.client(
    'sqs',
    aws_access_key_id="DEV_ACCESS_KEY_ID",
    aws_secret_access_key="DEV_SECRET_ACCESS_KEY",
    endpoint_url='http://localhost:3001'
)

sqs.send_message(
    QueueUrl='http://localhost:3001/test-queue',
    MessageBody="hello world", 
)

