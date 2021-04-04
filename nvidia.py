# BestBuy
# availible button class:
# "btn btn-primary btn-lg btn-block btn-leading-ficon add-to-cart-button"

# sold out button class:
# "btn btn-disabled btn-lg btn-block add-to-cart-button"

# RTX 3060TI
# https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402
# RTX 3070
# https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442
# RTX 3080
# https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440
# RTX 3090
# https://www.bestbuy.com/site/nvidia-geforce-rtx-3090-24gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429434.p?skuId=6429434

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import time
from random import randint

thirty_sixty = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402"
thirty_seventy = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442"
thirty_eighty = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440"
thirty_ninety = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3090-24gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429434.p?skuId=6429434"

# Options for Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(
    ChromeDriverManager().install(), chrome_options=chrome_options)

# Opening website
driver.get(thirty_eighty)
# choosing region, US
driver.find_element_by_class_name("us-link").click()
# Waiting until page loads


def random():
    time.sleep(randint(8, 15))


def buying_gpu():
    add_to_cart = driver.find_element_by_xpath(
        "//div[@class='fulfillment-add-to-cart-button']/div/div[@style='position:relative']/button[@class='btn btn-primary btn-lg btn-block btn-leading-ficon add-to-cart-button']")
    add_to_cart.click()
    random()
    # close_pop_out = driver.find_element_by_class_name(
    #     "btn-default-link close-modal-x").click()
    # random()
    # cart = driver.find_element_by_class_name("cart-label").click()
    # random()


# Checking if Sold Out button is present
sold_out = driver.find_element_by_xpath(
    "//div[@class='fulfillment-add-to-cart-button']/div/div[@style='position:relative']/button[@class='btn btn-disabled btn-lg btn-block add-to-cart-button']")
unavailible = True
while unavailible:
    # Printing an outcome
    if sold_out:
        print("Sold Out")
        unavailible = True
    else:
        # if Availible, it would print an URL of the page
        print(driver.current_url)
        buying_gpu()
        unavailible = False

time.sleep(randint(8, 15))
driver.quit()
