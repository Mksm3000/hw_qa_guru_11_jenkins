from pages.registration_page import RegistrationPage


def test_registration_form():
    registration_page = RegistrationPage()

    registration_page.open()
    registration_page.fill_first_name('Ivan')
    registration_page.fill_last_name('Petroff')
    registration_page.fill_user_email('ivan@petroff.com')
    registration_page.select_gender('Male')
    registration_page.fill_mobile_number('0958877666')
    registration_page.fill_date_of_birth(year='1984', month='April', day='12')
    registration_page.fill_subjects(('Ph', 'Ma'))
    registration_page.select_hobbies(('Reading', 'Music'))
    registration_page.upload_picture('qa_guru.png')
    registration_page.fill_address('Capital city, Liberty str, 17')
    registration_page.select_state('Uttar Pradesh')
    registration_page.select_city('Lucknow')
    registration_page.submit()

    registration_page.should_have_registered_user_with(('Ivan Petroff',
                                                        'ivan@petroff.com',
                                                        'Male',
                                                        '0958877666',
                                                        '12 April,1984',
                                                        'Physics, Maths',
                                                        'Reading, Music',
                                                        'qa_guru.png',
                                                        'Capital city, Liberty str, 17',
                                                        'Uttar Pradesh Lucknow',
                                                        ))
