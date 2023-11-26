from datetime import datetime


now = datetime.now()
message = f'{now:%M:%S} Logged!'

print(message)
