import data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def click_on_personal_mode(self):
        self.driver.find_element(By.XPATH,"//div[@class='modes-container']//div[@class='mode'][2]").click()

    def click_on_order_a_taxi(self):
        WebDriverWait(self.driver,100).until(expected_conditions.element_to_be_clickable((By.XPATH,"//div[@class='results-text']//button[contains(text(), 'Pedir un taxi')]")))
        self.driver.find_element(By.CSS_SELECTOR,"button.button.round").click()

    def click_on_comfort_tariff(self):
        WebDriverWait(self.driver,100).until(expected_conditions.element_to_be_clickable((By.XPATH,"//div[text()='Comfort']")))
        self.driver.find_element(By.XPATH,"//div[text()='Comfort']").click()

    def set_phone_number(self):
        self.driver.find_element(By.XPATH,"//div[text()='Número de teléfono']").click()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='modal']//div[@class='section active']")))

        phone_field = self.driver.find_element(By.ID,"phone")
        phone_field.send_keys(data.phone_number)

        self.driver.find_element(By.CSS_SELECTOR,"button.button.full").click()

    def enter_sms_code(self):
        code = retrieve_phone_code(self.driver)
        sms_code_field = self.driver.find_element(By.XPATH,"//div[@class='input-container']//input[@id='code']")
        sms_code_field.send_keys(code)

        sms_code_confirm_button = self.driver.find_element(By.XPATH,"//button[text()='Confirmar']")
        sms_code_confirm_button.click()

    def add_credit_card(self):
        self.driver.find_element(By.CSS_SELECTOR,"div.pp-button.filled").click()
        self.driver.find_element(By.CSS_SELECTOR,"div.pp-row.disabled").click()

        card_number_field = self.driver.find_element(By.CSS_SELECTOR,"input#number.card-input")
        card_code_field = self.driver.find_element(By.CSS_SELECTOR,"input#code.card-input")

        card_number_field.send_keys(data.card_number)
        card_code_field.send_keys(data.card_code)

        self.driver.find_element(By.CSS_SELECTOR,"div.plc").click()

        self.driver.find_element(By.XPATH,"//button[text()='Agregar']").click()
        self.driver.find_element(By.XPATH,"//div[@class='payment-picker open']//div[@class='modal']//div[@class='section active']//button[@class='close-button section-close']").click()

    def set_driver_message(self):
        self.driver.find_element(By.ID,"comment").send_keys(data.message_for_driver)

    def click_on_blanket_and_scarves_slider(self):
        self.driver.find_element(By.CSS_SELECTOR,"span.slider.round").click()

    def add_2_ice_creams(self):
        increase_button = self.driver.find_element(By.XPATH,".//div[@class='counter']//div[@class='counter-plus'][1]")
        increase_button.click()
        increase_button.click()

    def click_on_reserve_button(self):
        self.driver.find_element(By.CSS_SELECTOR,"span.smart-button-main").click()

    def wait_for_taxi_driver_information(self):
        WebDriverWait(self.driver, 100).until(expected_conditions.visibility_of_element_located((By.XPATH,"(//div[@class='order-btn-group'])[1]//div[2]")))

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        options = webdriver.ChromeOptions()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})

        cls.driver = webdriver.Chrome(service =webdriver.ChromeService(), options=options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        WebDriverWait(self.driver,5).until(expected_conditions.presence_of_element_located((By.ID,"from")))
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_select_comfort_tariff(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_on_personal_mode()
        routes_page.click_on_order_a_taxi()
        routes_page.click_on_comfort_tariff()
        selected_tariff = self.driver.find_element(By.CSS_SELECTOR,"div.tcard.active").text
        assert 'Comfort' in selected_tariff

    def test_fill_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_phone_number()
        routes_page.enter_sms_code()
        phone_number_confirmed = self.driver.find_element(By.XPATH,"//div[@class='np-button filled']").text
        assert phone_number_confirmed == data.phone_number

    def test_add_credit_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_credit_card()
        credit_card_added = self.driver.find_element(By.XPATH,"//div[@class='pp-value-text']").text
        assert credit_card_added == 'Tarjeta'

    def test_set_driver_message(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_driver_message()
        message_added = self.driver.find_element(By.CSS_SELECTOR,"input#comment.input").get_attribute('value')
        assert message_added == data.message_for_driver

    def test_add_blanket_and_scarves(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_on_blanket_and_scarves_slider()
        checkbox = self.driver.find_element(By.XPATH,"(//input[@class='switch-input'])[1]")
        assert checkbox.is_selected()

    def test_add_2_ice_creams(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_2_ice_creams()
        ice_cream_counter = self.driver.find_element(By.CSS_SELECTOR,"div.counter-value").text
        assert ice_cream_counter == "2"

    def test_show_search_for_taxi_information(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_on_reserve_button()
        taxi_search = self.driver.find_element(By.XPATH,"//div[@class='order-header-title']").text
        assert taxi_search == 'Buscar automóvil'

    def test_show_taxi_driver_information(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.wait_for_taxi_driver_information()
        details_button = self.driver.find_element(By.XPATH,"(//div[@class='order-btn-group'])[1]//div").text
        assert '4,9' in details_button

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
