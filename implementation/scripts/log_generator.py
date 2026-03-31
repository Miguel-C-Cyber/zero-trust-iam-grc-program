import random
import datetime

users = ["Jane", "Steven", "Amanda"]
resources = ["Admin Portal", "HR Files", "Finance DB"]


results = [
    "Allowed",
    "Denied (MFA missing)",
    "Denied (Insufficient privileges)",
    "Denied (Account locked)"
]

with open("../logs/user_access.log", "a") as f:
    for _ in range(10):
        timestamp = (datetime.datetime.now() + datetime.timedelta(seconds=_)).strftime("%Y-%m-%d %H:%M:%S")
        user = random.choice(users)
        resource = random.choice(resources)

        result = random.choice(results)

        f.write(f"{timestamp} - User: {user} - Access: {resource} - Result: {result}\n")