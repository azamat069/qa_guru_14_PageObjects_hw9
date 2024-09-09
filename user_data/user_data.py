import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    day_of_birth: str
    month_of_birth: str
    year_of_birth: str
    subjects: str
    hobbies: str
    picture: str
    address: str
    state: str
    city: str


user = User(first_name='Azamat',
            last_name='QA',
            email='email@email.com',
            gender='Male',
            phone_number='1234567890',
            day_of_birth='17',
            month_of_birth='April',
            year_of_birth='1999',
            subjects='Computer Science',
            hobbies='Sports, Music',
            picture='test_file.jpeg',
            address='Moscow Lenina 124 street',
            state='Haryana',
            city='Karnal'
            )
