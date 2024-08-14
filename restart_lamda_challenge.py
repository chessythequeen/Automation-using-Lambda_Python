import boto3

s3 = boto3.client("s3")
sns = boto3.client("sns")

def lambda_handler(event, context):
   #print(event)
   
   bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
   object_key = event["Records"][0]["s3"]["object"]["key"]
   
   #print(bucket_name)
   #print(object_key)
   
   myobject = s3.get_object(
     Bucket=bucket_name,
     Key=object_key
     )
     
   word = len(myobject["Body"].read().decode("utf-8").split(" "))
   
   #print(word)
   
   sns.publish(
       TopicArn = "arn:aws:sns:us-east-1:523799770014:chessy",
       Subject = "word count",
       Message = "the s3 object has +str(word)"
       )
   

   
   return
