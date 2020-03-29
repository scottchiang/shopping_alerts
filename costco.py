import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

items = [
	'https://www.costco.com/kirkland-signature-bath-tissue%2c-2-ply%2c-425-sheets%2c-30-rolls.product.100142093.html',
	'https://www.costco.com/clorox-disinfecting-wipes,-variety-pack,-85-count,-5-pack.product.100534416.html',
	'https://www.costco.com/kirkland-signature-create-a-size-paper-towels%2c-2-ply%2c-160-sheets%2c-12-count.product.100234271.html'
]

zip_code = '12345' # put your zip code here

def main():
	for item in items:
		driver = get_driver()
		driver.get(item)

		try:
			driver.find_element_by_xpath('//*[@id="postal-code-input"]').send_keys(zip_code)
			driver.find_element_by_xpath('//*[@id="postal-code-submit"]').click()
		except NoSuchElementException:
			print(f'Zip code already set to {zip_code}')

		source = driver.page_source
		driver.quit()

		process_status(source)

def get_driver():
	chrome_options = Options()
	chrome_options.add_argument("--headless")
	chrome_options.add_argument("--no-sandbox")
	chrome_options.add_argument("--disable-dev-shm-usage")
	chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:74.0) Gecko/20100101 Firefox/74.0")
	return webdriver.Chrome(options=chrome_options)

def process_status(source):
	# Output the item status
	soup = BeautifulSoup(source, 'html.parser')
	item = soup.find("h1").text
	cart_btn_value = soup.find("input", {"id": "add-to-cart-btn"}).get('value')
	if cart_btn_value == 'Add to Cart':
		status = 'Available'
	else:
		status = 'Unavailable'
	print(f'Item Name: {item}')
	print(f'Status: {status}')

if __name__ == "__main__":
	main()
