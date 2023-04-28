import base64
import os
from twilio.rest import Client

def hello_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    print(pubsub_message)

    account_sid = 'AC32557e1cf7fba3732f7c49c82c565c6e'
    auth_token = '6d92e8bf07acf5ada92621b882990a46'
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
                              body='Message from twillo pubsub : ' +pubsub_message,
                              from_='+16073262769',
                              to='+5146642722'
                          )

    print(message.sid)
