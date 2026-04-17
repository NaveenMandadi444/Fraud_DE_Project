from fastapi import FastAPI
from generator import generate_transaction
from connection import send_to_eventhub

app = FastAPI()

@app.get("/transaction")
def create_transaction():
    event = generate_transaction()
    send_to_eventhub(event)
    return {"message": "Transaction sent", "data": event}