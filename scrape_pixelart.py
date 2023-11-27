from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import requests


name_of_ball = str(input('What ball you want to get pixel art from?: '))
compacted_with_url = name_of_ball.replace(' ', '_')

chrome_options = Options()

chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--headless")

wd = webdriver.Chrome(options=chrome_options)
website_url = "https://www.polandballwiki.com/wiki/" + compacted_with_url + 'ball'

wd.get(website_url)
print('opened up the browser...')
time.sleep(3)
print('getting the links.')
### get url.
image_tags = wd.find_elements(By.XPATH, f"//h2[@class='pi-item pi-item-spacing pi-title']//span[@style='font-size:16px; line-height:120% !important; text-align: center; display: block; padding-top:2px']//span[@class='mw-default-size']//a[@href='/wiki/File:{compacted_with_url}-icon.png']//img")
image_urls = [img.get_attribute('src') for img in image_tags]

### download images.
print('Downloading...')
time.sleep(2)
response = requests.get(image_urls[0], stream=True)
with open(f'results/{name_of_ball}.png', 'wb') as f:
    for chunk in response.iter_content(chunk_size=128):
        f.write(chunk)
        print(f'Pixel art of the country: {name_of_ball} has been downloaded successfully.')

wd.close()