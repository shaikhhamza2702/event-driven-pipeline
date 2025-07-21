import boto3
import json
import datetime
import os

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    output_bucket = os.environ['OUTPUT_BUCKET']

    response = s3.list_objects_v2(Bucket=output_bucket, Prefix='processed/')
    summary = []

    for obj in response.get('Contents', []):
        key = obj['Key']
        file = s3.get_object(Bucket=output_bucket, Key=key)
        data = json.loads(file['Body'].read().decode('utf-8'))
        summary.append(data)

    today = datetime.date.today().isoformat()
    report_key = f"reports/report-{today}.json"

    s3.put_object(
        Bucket=output_bucket,
        Key=report_key,
        Body=json.dumps(summary, indent=2)
    )

    return {'status': 'report generated'}
