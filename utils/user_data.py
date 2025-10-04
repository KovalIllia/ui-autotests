from dataclasses import dataclass, field
from utils.data_generators import generate_password
from faker import Faker

fake = Faker()
@dataclass
class UserData:
    password: str = field(default_factory=generate_password)
    first_name: str = field(default_factory=fake.first_name)
    last_name: str = field(default_factory=fake.last_name)
    company: str = field(default_factory=fake.company)
    address: str = field(default_factory=fake.address)
    secondary_address: str = field(default_factory=fake.address)
    state: str = field(default_factory=fake.state)
    city: str = field(default_factory=fake.city)
    zipcode: str = field(default_factory=fake.zipcode)
    mobile: str = field(default_factory=fake.phone_number)


