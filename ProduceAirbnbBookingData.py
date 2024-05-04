import json
import boto3
import random
import string

sqs_client = boto3.client('sqs')
QUEUE_URL = 'https://sqs.ap-south-1.amazonaws.com/233025381364/AirBnBbookingQueue'  # replace with your SQS Queue URL

def data_generator():
    return {
        "bookingId":str(random.randint(10000, 99999)),
        "userId":''.join( random.choices(string.ascii_uppercase + string.digits, k = 10)),
        "propertyId":''.join( random.choices(string.ascii_uppercase + string.digits, k = 10)),
        "location": random.choice(["Tampa, Florida","Hyd, Ind","Blr, Ind"]),
        "startDate":random.choice(["2024-03-12","2024-03-13","2024-03-14"]),
        "endDate":random.choice(["2024-03-12","2024-03-13","2024-03-14"]),
        "price":'$ ' + str(random.randint(100,999))
    }

def lambda_handler(event, context):
    i=0
    while(i<5):
        sales_order = data_generator()
        print(sales_order)
        sqs_client.send_message(
            QueueUrl=QUEUE_URL,
            MessageBody=json.dumps(sales_order)
        )
        i += 1
    
    return {
        'statusCode': 200,
        'body': json.dumps('Sales order data published to SQS!')
    }