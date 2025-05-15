from faker import Faker
fake = Faker()

# Generate 5 fake names and addresses
for _ in range(5):
    print(f"Name: {fake.name()}")
    print(f"Address: {fake.address()}")
    print("---")
