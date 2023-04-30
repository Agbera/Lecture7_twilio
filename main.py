import base64
import os
from twilio.rest import Client
source_Number='+16073262769'
destination_numbers=['+5146642722','+2348120602849','+2348088320487','+2348034254634','+2347015984468','+2348140313002','+15148946725']

def hello_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    print(pubsub_message)

    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
                              body='Message from twillo pubsub : ' +pubsub_message,
                              from_=source_Number,
                              to=each_destination_number
                          )

    print(message.sid)
