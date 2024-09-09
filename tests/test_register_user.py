from pages.registration_page import RegistrationPage


def test_user_registration():
    registration_page = RegistrationPage()
    registration_page.register_user()
    registration_page.assert_user_data_form()