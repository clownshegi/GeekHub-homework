import os
import shutil
from pathlib import Path
from io import BytesIO
from PIL import Image
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://robotsparebinindustries.com/"
OUTPUT_DIR = Path(__file__).resolve().parent / 'generated_images'
SERVICE = ChromeService(ChromeDriverManager().install())
IMAGE_WIDTH = 342
IMAGE_HEIGHT = 200


class BotCustomizer:
    def __init__(self):
        self.output_directory = OUTPUT_DIR
        self.current_image = None
        self.browser = webdriver.Chrome(service=SERVICE)
        self.browser.get(BASE_URL)
        self.clean_output()
        self.setup_output()

    def clean_output(self):
        if os.path.exists(self.output_directory):
            shutil.rmtree(self.output_directory)

    def setup_output(self):
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)

    def order_navigation(self):
        nav_links = self.browser.find_elements(By.CLASS_NAME, "nav-link")
        order_robot_element = nav_links[-1]
        order_robot_element.click()

    def wait_for_element(self, xpath_element):
        wait = WebDriverWait(self.browser, 20).until(
            EC.visibility_of_element_located((
                By.XPATH,
                xpath_element
            )
            )
        )
        return wait

    def close_modal(self):
        xpath = "//button[@class='btn btn-danger' and text()='I guess so...']"

        close_button = self.wait_for_element(xpath)
        close_button.click()

    def customize_robot_order(self, data_args):
        head_value, body_value, legs_value, address_value = data_args

        input_elements = self.browser.find_elements(By.CLASS_NAME, "form-control")

        head_element = self.browser.find_element(By.XPATH, f"//option[@value={head_value}]")
        body_element = self.browser.find_element(By.XPATH, f"//input[@value={body_value}]/ancestor::label")
        legs_element = input_elements[0]
        address_element = input_elements[1]

        head_element.click()
        body_element.click()
        legs_element.send_keys(legs_value)
        address_element.send_keys(address_value)

    def preview_activation(self):
        try:
            while True:
                preview_button = self.browser.find_element(By.XPATH, f'//button[@id="preview"]')
                self.browser.execute_script("arguments[0].click();", preview_button)
                xpath = "//div[@id='robot-preview-image']"
                image = self.wait_for_element(xpath).find_element(By.XPATH, xpath)
                if image:
                    break
        except Exception:
            pass

    def order_activation(self):
        try:
            while True:
                order_button = self.browser.find_element(By.XPATH, '//button[@id="order"]')
                self.browser.execute_script("arguments[0].click();", order_button)
        except Exception:
            pass

    def get_order_status(self):
        xpath = "//p[@class='badge badge-success']"
        status = self.wait_for_element(xpath)
        return status.find_element(By.XPATH, xpath).text

    def generate_robot_image(self, data_args):
        image_urls = [
            f"{BASE_URL}heads/{data_args[0]}.png",
            f"{BASE_URL}bodies/{data_args[1]}.png",
            f"{BASE_URL}legs/{data_args[2]}.png"
        ]

        images = []
        for url in image_urls:
            response = requests.get(url)

            img = Image.open(BytesIO(response.content))
            img_resized = img.resize((IMAGE_HEIGHT, IMAGE_HEIGHT))
            images.append(img_resized)

        widths, heights = zip(*(i.size for i in images))
        combined_image = Image.new('RGB', (max(widths), sum(heights)))

        y_offset = 0
        for img in images:
            combined_image.paste(img, (0, y_offset))
            y_offset += img.size[1]

        self.current_image = combined_image

        y_offset = 0
        for img in images:
            combined_image.paste(img, (0, y_offset))
            y_offset += img.size[1]

        self.current_image = combined_image

    def save_generated_image(self):
        status = self.get_order_status()
        file_name = f"{self.output_directory}/_{status}_robot.jpg"
        self.current_image.save(file_name)

    def process_robot_orders(self):
        data = self.retrieve_robot_data(BASE_URL)
        for data_item in data:
            self.close_modal()
            self.customize_robot_order(data_item)
            self.preview_activation()
            self.generate_robot_image(data_item)
            self.order_activation()
            self.save_generated_image()
            self.navigate_to_next_robot()

    def navigate_to_next_robot(self):
        next_robot_button = self.browser.find_element(
            By.XPATH,
            "//button[@id='order-another']"
        )
        self.browser.execute_script("arguments[0].click();", next_robot_button)

    def start_process(self):
        self.order_navigation()
        self.process_robot_orders()

    @staticmethod
    def retrieve_robot_data(url):
        csv_data = []

        csv_url = "orders.csv"
        request_url = url + csv_url
        response = requests.get(url=request_url)
        csv_list = response.text.split("\n")
        csv_list.pop(0)

        for item in csv_list:
            new_list = item.split(",")[1:]
            csv_data.append(new_list)

        return csv_data

    def __del__(self):
        self.browser.quit()


custom_bot = BotCustomizer()
custom_bot.start_process()
