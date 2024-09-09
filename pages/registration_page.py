
import os
from selene import browser, have
from user_data.user_data import user

class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')

    def type_first_name(self, first_name):
        browser.element('#firstName').type(first_name)

    def type_last_name(self, last_name):
        browser.element('#lastName').type(last_name)

    def type_email(self, email):
        browser.element('#userEmail').type(email)

    def choose_gander(self):
        browser.element('[for="gender-radio-1"]').click()

    def type_phone_number(self, number):
        browser.element('#userNumber').type(number)

    def type_birth_date(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').element(f'[value = "{year}"]').click()
        browser.element('.react-datepicker__month-select').type(month).click()
        browser.element(f'.react-datepicker__day--0{day}').click()

    def type_subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def select_hobbies(self):
        browser.element('[for="hobbies-checkbox-1"]').click()
        browser.element('[for="hobbies-checkbox-3"]').click()

    def upload_picture(self):
        browser.element('#uploadPicture').send_keys(os.path.abspath('resources/test_file.jpeg'))

    def type_current_address(self, address):
        browser.element('#currentAddress').type(address)

    def type_state(self, state):
        browser.element('#react-select-3-input').type(state).press_enter()

    def type_city(self, city):
        browser.element('#react-select-4-input').type(city).press_enter()

    def click_submit_button(self):
        browser.element('#submit').click()

    def register_user(self):
        self.open()
        self.type_first_name(user.first_name)
        self.type_last_name(user.last_name)
        self.type_email(user.email)
        self.type_birth_date(user.year_of_birth, user.month_of_birth, user.day_of_birth)
        self.type_subjects(user.subjects)
        self.select_hobbies()
        self.upload_picture()
        self.type_current_address(user.address)
        self.type_state(user.state)
        self.type_city(user.city)
        self.click_submit_button()



    def assert_user_data_form(self, user):
        browser.element('.table').all('td').even.should(have.exact_texts(
            f'{user.first_name}{user.last_name}',
            f'{user.email}',
            f'{user.gender}',
            f'{user.phone_number}',
            f'{user.day_of_birth}{user.month_of_birth}{user.year_of_birth}',
            f'{user.subjects}',
            f'{user.hobbies}',
            f'{user.picture}',
            f'{user.address}',
            f'{user.state}{user.city}'))


