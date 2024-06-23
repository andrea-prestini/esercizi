from faker import Faker


locales = ["en_US", "es_ES", "fr_FR", "de_DE", "it_IT"]


fake_generators = {locale: Faker(locale) for locale in locales}


number = 20

for _ in range(number):
    locale = Faker().random.choice(locales)
    fake = fake_generators[locale]
    name = fake.name()
    print(locale[3:] + " -> " + name)
