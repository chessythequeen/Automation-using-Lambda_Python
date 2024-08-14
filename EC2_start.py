
import json
import boto3
import datetime

# Initialize boto3 clients
ec2 = boto3.client('ec2')
sns = boto3.client('sns')

# EC2 instance IDs to be started
INSTANCE_IDS = ['i-0b2727d9688de2756','i-04568720044ba3c42','i-0d95bb7869c352c92','i-0f1d54a7622aeceb6'll]

# SNS Topic ARN
SNS_TOPIC_ARN = 'arn:aws:sns:eu-west-3:654654139557:Server-start-notification'

def lambda_handler(event, context):
    # Start the EC2 instances
    response = ec2.start_instances(InstanceIds=INSTANCE_IDS)
    
    # Check the starting status
    starting_instances = [instance['InstanceId'] for instance in response['StartingInstances']]
    
    # Create a notification message
    message = f"Started EC2 instances: {', '.join(starting_instances)}"
    
    # Send the notification to SNS
    sns_response = sns.publish(
        TopicArn='arn:aws:sns:eu-west-3:654654139557:Server-start-notification',
        Message=message,
        Subject='EC2 Instances Started'
    )
    
    # Return a response
    return {
        'statusCode': 200,
        'body': json.dumps('Notification sent successfully!')
    }
