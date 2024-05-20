import json
import boto3
import random
import string

sqs_client = boto3.client('sqs')
  # replace with your SQS Queue URL

def data_generator():
    message = {
        "bookingId": str(random.randint(10000, 99999)),
        "userId": ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)),
        "propertyId": ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)),
        "location": random.choice(["Tampa, Florida", "Hyd, Ind", "Blr, Ind"]),
        "startDate": startDate,
        "endDate": endDate,
        "price": '$ ' + str(random.randint(100, 999))
    }
    return message

def lambda_handler(event, context):
    sqs_client = boto3.client('sqs')
    for i in range(5):
        sqs_client.send_message(QUEUE_URL = 
                                'https://sqs.ap-south-1.amazonaws.com/233025381364/AirBnBbookingQueue',
                                 MessageBody = json.dumps(data_generator())
                                )
lambda_handler(1,2)