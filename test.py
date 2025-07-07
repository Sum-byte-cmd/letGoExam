import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestWebsite:
  @pytest.fixture(autouse=True)
  def browser_setup_and_teardown(self):
    self.use_selenoid = False

    if self.use_selenoid:
      self.browser = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub'
      )
    else:
      self.browser = webdriver.Chrome()

    self.browser.maximize_window()
    self.browser.implicitly_wait(10)
    self.wait = WebDriverWait(self.browser, 10)

    yield

    self.browser.quit()

  def test_search_and_filter_on_letgo(self):
    self.browser.get("https://www.letgo.com")

    search_input = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "searchTb")))
    search_input.send_keys("bike")
    search_input.send_keys(Keys.ENTER)

    cross_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "cross-icon-button")))
    cross_button.click()

    accordion_title = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "accordion-title")))
    accordion_title.click()

    checkbox = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='search-ssr-page']/div[2]/aside/div[3]/div[2]/div[2]/div/div/label")))
    checkbox.click()

    apply_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-contained")))
    apply_button.click()

    favorite_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "item-card-favorite-button")))
    favorite_button.click()