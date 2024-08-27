# Lambda-challenges
This repo contains lambda projects to automate a wide range of tasks and processes eg  Lambda to automatically resize and compress images when they are uploaded to an S3 bucket
**EBS_automatic_snapshot.py**
Automates the process of creation EBS snapshot

**EC2_start.py**
Automates the start of instances at a particular time in a day

**restart_lambda_challenge**
This is one of the AWS Restart challenges, restart is a 12 week training program. 
Lambda function is triggered when a new object is created in an S3 bucket. It reads the content of the file, counts the number of words in it, and then sends this information as a notification through SNS
