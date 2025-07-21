import boto3
import json
import os

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    output_bucket = os.environ['OUTPUT_BUCKET']

    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']

        response = s3.get_object(Bucket=bucket, Key=key)
        content = response['Body'].read().decode('utf-8')

        lines = content.strip().split('\n')
        result = {
            'filename': key,
            'line_count': len(lines)
        }

        output_key = f"processed/{key}.json"
        s3.put_object(
            Bucket=output_bucket,
            Key=output_key,
            Body=json.dumps(result)
        )

    return {'status': 'success'}
