from azure.servicebus import QueueClient, Message

queueName = "test"
connStr = "Endpoint=sb://airflowservicebus.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=sQSuc6+5wBja34PXdrwAp3yqxkces/3juf0xhx3imEo="

def SendMessage(message):
    # Create the QueueClient
    queue_client = QueueClient.from_connection_string(connStr, queueName)
    # Send a test message to the queue
    msg = Message(message)
    queue_client.send(msg)
    print("Message: {0} has sended to ServiceBus queue: {1}".format(msg, queueName)) 


def ReceiveMessages():
    from azure.servicebus import QueueClient

    # Create the QueueClient
    queue_client = QueueClient.from_connection_string(connStr, queueName)

    # Receive the message from the queue
    with queue_client.get_receiver() as queue_receiver:
        messages = queue_receiver.fetch_next(timeout=3)
        for message in messages:
            print("Message has received: '{0}'".format(message))
            message.complete()