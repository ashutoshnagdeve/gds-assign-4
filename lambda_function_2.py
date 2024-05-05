import json
import boto3
from datetime import datetime

s3_client = boto3.client('s3')

def calculate_booking_duration(start_date, end_date):
    start_dt = datetime.strptime(start_date, "%Y-%m-%d")
    end_dt = datetime.strptime(end_date, "%Y-%m-%d")
    duration_days = (end_dt - start_dt).days
    return duration_days

def lambda_handler(event, context):
    filtered_records = []
    
    for record in event['Records']:
        # Extract relevant data from the EventBridge event
        if record.get('eventName') == 'INSERT' and 'NewImage' in record:
            new_image = record['NewImage']
            start_date = new_image.get('startDate')
            end_date = new_image.get('endDate')
            
            # Calculate booking duration
            if start_date and end_date:
                duration_days = calculate_booking_duration(start_date, end_date)
                if duration_days > 1:
                    filtered_records.append(new_image)
    
    # Write filtered records to an S3 bucket
    bucket_name = 's3-airbnb-landing'
    key = 'filtered_records.json'
    s3_client.put_object(
        Bucket=bucket_name,
        Key=key,
        Body=json.dumps(filtered_records),
        ContentType='application/json'
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Filtered records with booking duration more than 1 day written to S3 bucket!')
    }
