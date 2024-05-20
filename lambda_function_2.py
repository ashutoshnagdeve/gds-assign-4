import json

def lambda_handler(event, context):
    try:
        print('Event', event)
        print('context', context)
        message = json.loads(events[0]['body'])
        print(message)
        if (message['StartDate'] == message['endDate']):
            message = {}
        return {
            'message': message
        }
    except Exception as e:
        return {
            'Error message': str(e)
        }