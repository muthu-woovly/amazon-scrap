from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import json
import time
import sys
from random import randrange
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import write

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

SERVER_URL = "http://localhost:3001/amazon"

while True:

	urls= [
		{
			"url": 'https://www.amazon.in/mCaffeine-Caffeinating-Breathable-Lightweight-Ultra-Comfortable/dp/B09BD5CY2G/',
		}
	]

	for target in urls:
		print("[processing] " + json.dumps(target, indent=1))
		url = target["url"]

		try:
			driver.get('https://www.amazon.in')
			time.sleep(5)
			driver.get(url)
			time.sleep(35)

			title = driver.find_element(By.ID,'productTitle').text
			# image_urls = driver.find_elements(By.XPATH,'//div[@id="altImages"]/ul/li//img')
			ratings_count = driver.find_element(By.ID,'acrCustomerReviewText').text
			ratings = driver.find_element(By.XPATH,'//*[@id="acrPopover"]/span[1]/a/span').text
			actual_price = driver.find_element(By.XPATH,'//*[@id="corePriceDisplay_desktop_feature_div"]/div[2]/span/span[1]/span[2]/span/span[2]').text
			discounted_price = driver.find_element(By.XPATH,'//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[3]/span[2]/span[2]').text
			# features = driver.find_elements(By.XPATH,'//div[@id="feature-bullets"]/ul/li')
			# ratings = driver.find_element(By.XPATH,'//span[@id="acrPopover"]').get_attribute("title")
			# returnable = bool(driver.find_element(By.XPATH,"//b[text()=' This item is Returnable ']"))
			sold_by = driver.find_element(By.XPATH,'//*[@id="bylineInfo"]').text
			print(sold_by)

			item = {
				"url": url,
				"title": title,
				# "imageUrls": [ image_url.get_attribute('src') for image_url in image_urls ],
				"actualPrice": actual_price,
				"discountedPrice": discounted_price,
				# "volume": volume,
				# "features": [ feature.text for feature in features ],
				"ratings": ratings,
				# "returnable": returnable,
				"soldBy": sold_by,
				"ratings_count": ratings_count
			}

			# product_response = requests.post(SERVER_URL + "/products", data=item)
			# product_json = product_response.json()
			# print(json.dumps(product_json, indent=1))
			print(item)
			write.writeGS(item)
			# target["status"] = "success"
		except:
			# time.sleep(60 * 100)
			exception_type, exception, traceback = sys.exc_info()
			print("[error]")
			target["status"] = "failure"

		# requests.put(SERVER_URL + "/targets/" + target["_id"], data=target)

		seconds = 60 + randrange(30)
		print("Sleeping for " + str(seconds) + " seconds...")
		time.sleep(seconds)
	else:
		print("Could not fetch any URLs to process. Retrying in 10 minutes...")
		time.sleep(60 * 10)
	break

driver.quit()
