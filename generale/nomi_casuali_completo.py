
from faker import Faker
import random
import pandas as pd


# Inizializzare il generatore di dati Faker
fake = Faker()

# Generare dati per n utenti
num_users = 100
user_data = []


for _ in range(num_users):
    user = {
        "id": fake.uuid4(),
        "name": fake.name(),
        "email": fake.email(),
        "address": fake.address(),
        "birthdate": fake.date_of_birth(minimum_age=18, maximum_age=50),
        "company": fake.company(),
        "job_title": fake.job(),
        "phone_number": fake.phone_number(),
        "credit_card_number": fake.credit_card_number(),
        "credit_card_expiry": fake.credit_card_expire(),
        "iban": fake.iban(),
        "username": fake.user_name(),
        "password": fake.password(),
        "last_login": fake.date_time_this_year(),
        "signup_date": fake.date_time_between(start_date="-2y", end_date="now")

    }

    user_data.append(user)


# Convertire i dati in un DataFrame pandas
df_users = pd.DataFrame(user_data)

print(df_users.head(3))
