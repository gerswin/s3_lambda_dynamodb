import os
import boto3
BUCKET_NAME = os.getenv('STORAGE_BUCKET')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TABLE_NAME')
s3 = boto3.client('s3', region_name='us-east-1')
def handler(event, context):
    for record in event['Records']:
        file_key = record['s3']['object']['key']
        csv_file = s3.get_object(Bucket=BUCKET_NAME, Key=file_key)
        csv_content = csv_file['Body'].read().split(b'\n')
        with table.batch_writer() as batch:
            for row in csv_content:
                try:
                    row = row.decode('latin-1').split('|')
                    batch.put_item(
                        Item=row
                    )
                except Exception as e:
                    print(e)