from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import json
import parameters

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)
driver.get("https://accounts.google.com/o/oauth2/auth/identifier?client_id=717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fstackauth.com%2Fauth%2Foauth2%2Fgoogle&state=%7B%22sid%22%3A1%2C%22st%22%3A%2259%3A3%3Abbc%2C16%3A7e0f26118e5f8223%2C10%3A1659613239%2C16%3A8a8b65da787d859b%2C981a23f9ec9f56a8f0ed96cc1bc3b166069942b7636d6becdedddf678b844bac%22%2C%22cid%22%3A%22717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com%22%2C%22k%22%3A%22Google%22%2C%22ses%22%3A%2272a75faea9ff490390ccfd860c34ee1b%22%7D&response_type=code&service=lso&flowName=GeneralOAuthFlow")

driver.find_element(By.ID, 'identifierId').send_keys(parameters.gmail_address)

