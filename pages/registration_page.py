from selene import browser, have, command
from utils import resource


class RegistrationPage:

    def open(self):
        browser.open('automation-practice-form')

        # уменьшаем масштаб страницы до 65%
        browser.driver.execute_script(
            "document.querySelector('.body-height').style.transform='scale(.65)'")

        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3))
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        browser.element(".text-center").should(have.text("Practice Form"))

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_user_email(self, value):
        browser.element('#userEmail').type(value)

    def select_gender(self, gender_name):
        browser.all('[name=gender]').element_by(have.value(gender_name)).element(
            '..').click()

    def fill_mobile_number(self, value):
        browser.element('#userNumber').type(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(f'.react-datepicker__day--0{day}:not('
                        f'.react-datepicker__day--outside-month)').click()

    def fill_subjects(self, values: tuple):
        for value in values:
            browser.element('#subjectsInput').type(value).press_tab()

    def select_hobbies(self, values: tuple):
        for value in values:
            browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()

    def upload_picture(self, value):
        browser.element('#uploadPicture').send_keys(resource.path(value))

    def fill_address(self, value):
        browser.element('#currentAddress').type(value)

    def select_state(self, value):
        browser.element('#state').perform(command.js.scroll_into_view).click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(
            value)).click()

    def select_city(self, value):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(
            value)).click()

    def submit(self):
        browser.element('#submit').perform(command.js.click)

    def should_have_registered_user_with(self, values: tuple):
        browser.element('.modal-content').element('table').all('tr').all(
            'td').even.should(have.exact_texts(values))
