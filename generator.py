import uuid
import random
from datetime import datetime

users = ["u1","u2","u3","u4","u5"]
locations = ["Chennai", "Delhi", "Hyderabad", "Mumbai"]

def generate_transaction():
    return {
        "transaction_id": str(uuid.uuid4()),
        "user_id": random.choice(users),
        "amount": random.randint(100, 10000),
        "location": random.choice(locations),
        "timestamp": datetime.now().isoformat()
    }