import boto3
import datetime

ec2 = boto3.client('ec2')
sns = boto3.client('sns')

def lambda_handler(event, context):
    
    
    
    volumes = ec2.describe_volumes()

    
    for volume in volumes['Volumes']:
        volume_id = volume['VolumeId']
        snapshot_description = f"DailySnapshot_{volume_id}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        
        snapshot = ec2.create_snapshot(VolumeId=volume_id, Description=snapshot_description)
        print(f"Snapshot created by chessy: {snapshot['SnapshotId']}")
        
        
        sns.publish(
            TopicArn='arn:aws:sns:us-east-1:882902190416:ebs-snapshot-sns',
            Subject='EBS Snapshot Created',
            Message=f"Snapshot {snapshot['SnapshotId']} created for volume {volume_id}."
        )


