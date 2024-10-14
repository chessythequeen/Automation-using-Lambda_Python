# Lambda-challenges
This repo contains lambda projects to automate a wide range of tasks and processes in AWS

**EBS_automatic_snapshot.py**
Automates the process of creation EBS snapshot. Follow this step by step guide https://medium.com/@janetchessybrand/automate-ebs-snapshot-with-lambda-c1f360c85ae7
![EBS snapshot automation drawio](https://github.com/user-attachments/assets/fc57d6c7-da18-4bb7-9c70-96363d7b04a0)


**EC2_start.py**
Automates the start of instances at a particular time in a day

**restart_lambda_challenge**
This is one of the AWS Restart challenges, restart is a 12 week training program. 
Lambda function is triggered when a new object is created in an S3 bucket. It reads the content of the file, counts the number of words in it, and then sends this information as a notification through SNS
