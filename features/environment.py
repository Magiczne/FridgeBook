from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
	context.browser = webdriver.Chrome(ChromeDriverManager().install())
	context.browser.implicitly_wait(1)
	context.server_url = 'http://localhost:8000'

def after_all(context):
	context.browser.quit()

def before_feature(context, feature):
	pass