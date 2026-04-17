import os
import json
from azure.eventhub import EventHubProducerClient, EventData
from dotenv import load_dotenv

load_dotenv()

producer = EventHubProducerClient.from_connection_string(
    conn_str=os.getenv("EVENT_HUB_CONNECTION_STRING"),
    eventhub_name=os.getenv("EVENT_HUB_NAME")
)

def send_to_eventhub(data):
    batch = producer.create_batch()
    batch.add(EventData(json.dumps(data)))
    producer.send_batch(batch)
    print("Event sent ✅")