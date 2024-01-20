# This bot is just a demo version made by Hasami Nagisa (S3n1ty) - old name: Asaki
# Contact: 
# Discord: isepipi8239

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import json
import os
from colored import Fore, Back, Style
import time
from accountManage import *
from urllib import parse
from seleniumwire.utils import decode
import undetected_chromedriver as uc
from seleniumwire.utils import decode
from menu import menu
from timer import *


def decode_network(request):
    return json.loads(decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity')))

def sessionLogin(**params):
    session_path = './sessions/' + params['session']

    with open(session_path, 'r') as f:
        session = json.load(f)

    for cookie in session:
        if 'sameSite' in cookie:
            if cookie['sameSite'] == 'None' or 'unspecified':
                cookie['sameSite'] = 'Strict'
        driver.add_cookie(cookie)




CONFIG_DIR = "./config"
SETTINGS_FILE = "settings.json"
SETTINGS_PATH = os.path.join(CONFIG_DIR, SETTINGS_FILE)


# def process_buttons(buttons, section_number):
#     print(f"\nSection {section_number}:")
#     for i, button in enumerate(buttons, 1):
#         aria_label = button.get('aria-label')
#         status = "Available" if button.get('aria-disabled') == "false" else "Sold out"
#         print(f"[{i}] Button: {aria_label} - Status: {status}")

# def mark_button_as_clicked(button):
#     # Add logic to simulate the "clicked" state
#     button['class'] = button.get('class', []) + ['T_6srb']
#     # Add a tick icon after the button text
#     button.div = button.new_tag('div', class_='NkXHv4')
#     img_tag = button.new_tag('img', alt='icon-tick-bold', class_='QX2JQy', src='https://deo.shopeemobile.com/shopee/shopee-pcmall-live-sg/productdetailspage/9057d6e718e722cde0e8.svg')
#     button.div.append(img_tag)
#     button.append(button.div)

# def choose_options(buttons_section1, buttons_section2=None):
#     process_buttons(buttons_section1, 1)

#     if buttons_section2:
#         process_buttons(buttons_section2, 2)

#     selected_options = {}

#     for section_number, buttons in [(1, buttons_section1), (2, buttons_section2)]:
#         if buttons:
#             input_prompt = f"\nInput for Section {section_number} (comma-separated numbers, leave empty if not applicable): "
#             input_str = input(input_prompt)
#             selected_buttons = [int(choice) for choice in input_str.split(",")] if input_str else []

#             print(f"\nSection {section_number}:")
#             for index in selected_buttons:
#                 if 0 < index <= len(buttons):
#                     button = buttons[index - 1]
#                     label = button.get('aria-label')
#                     status = "Available" if button.get('aria-disabled') == "false" else "Sold out"
#                     print(f"[{index}] Button: {label} - Status: {status}")

#                     # Simulate the click action
#                     mark_button_as_clicked(button)

#                     selected_options[section_number] = selected_options.get(section_number, []) + [(index, label, status)]
#                 else:
#                     print(f"Invalid index for Section {section_number}: {index}")

#     print("\nSelected options:")
#     for section_number, options in selected_options.items():
#         print(f"Section {section_number}:")
#         for index, label, status in options:
#             print(f"[{index}] Button: {label} - Status: {status}")




def wait_for_element_present(driver, xpath, timeout=10, max_attempts=15):
    """
    Wait for the presence of an element identified by xpath.
    If the timeout occurs, refresh the page and try again.

    :param driver: WebDriver instance
    :param xpath: XPath of the element to wait for
    :param timeout: Maximum time to wait for each attempt, in seconds (default is 10)
    :param max_attempts: Maximum number of attempts (default is 15)
    """
    attempts = 0
    while attempts < max_attempts:
        try:
            element_present = EC.presence_of_element_located((By.XPATH, xpath))
            WebDriverWait(driver, timeout).until(element_present)
            break  # Element found, exit the loop
        except TimeoutException:
            print(f"Attempt {attempts + 1}: Timed out waiting for element with xpath: {xpath}")
            attempts += 1
            if attempts < max_attempts:
                print("Refreshing the page and retrying...")
                driver.refresh()




def get_information_about_product():
    """
    Get infomation about product
        - Title, Price, Rate, Store/Valid quantity, Price
        - clasify
            - Location of Types / Options
    """
    global xpath_choice
    print("====================================================")
    productTitle = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div/div[2]/div[1]/div[1]/div/div/section[1]/section[2]/div/div[1]/span')
    productEvaluate = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div/div[2]/div[1]/div[1]/div/div/section[1]/section[2]/div/div[2]/button[2]/div[1]')
    productSold = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div/div[2]/div[1]/div[1]/div/div/section[1]/section[2]/div/div[2]/div/div[1]')
    productStore = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div/div[2]/div[1]/div[1]/div/div/section[1]/section[2]/div/div[4]/div/div/div/section[2]/div/div[2]')
    productPrice = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div/div[2]/div[1]/div[1]/div/div/section[1]/section[2]/div/div[3]/div/div/section/div/div/div')



    xpath = '//*[@id="main"]/div/div[2]/div[1]/div[1]/div/div/section[1]/section[2]/div/div[4]/div/div/div/section[1]/div'
    container_element = driver.find_element(by=By.XPATH, value=xpath)
    button_elements = container_element.find_elements(by=By.TAG_NAME, value='button')
    
    
    xpath_list = [f"{xpath}/button[{i}]" for i in range(1, len(button_elements) + 1)]

    """Print a list of buttons"""
    # print(xpath_list)
    print(f"{Fore.cyan}[+] Buttons founded:{Style.reset} {len(xpath_list)}")

    for i in range(len(xpath_list)):
        status = driver.find_element(by=By.XPATH, value=xpath_list[i]).get_attribute('aria-disabled')
    
        if status == 'true':
            print(f"{Fore.blue}[{i+1}] Classify: {Style.reset} {button_elements[i].text} | {Fore.blue}[+] Status: {Style.reset} {Fore.red}Not Available{Style.reset}")
        else:
            print(f"{Fore.blue}[{i+1}] Clasify: {Style.reset} {button_elements[i].text} | {Fore.blue}[+] Status: {Style.reset} {Fore.green}Available{Style.reset}")

    # Get status of product (Available / Not available)
    # print xpath_list attribute 
        # If aria-disabled = true > Not Available | else > Available

    # for xpath in xpath_list:    
    #     print(f"{Fore.yellow}[+]{Style.reset} {xpath}")
    
    # print(f"{Fore.cyan}[+] Select a button: {Style.reset}")
    # for i in range(len(xpath_list)):
    #     print(f"{Fore.red}[{i+1}]: {Style.reset} {xpath_list[i]}")

    
    # Get classify choice 
    while True:
        try:
            choice = int(input(f"{Fore.blue}[?] Classify Choice: {Style.reset}"))
            if choice in range(1, len(xpath_list) + 1):
                break
            else: print(f"{Fore.red}[!] Please enter a number between 1 and {len(xpath_list)}!{Style.reset}")
        except ValueError:
            print(f"{Fore.red}[!] Please enter a number!{Style.reset}")

    print("---------------------------------------------------")

    xpath_choice = xpath_list[choice - 1]
    # print(f"{Fore.green}[+] Location: {Style.reset}", xpath_choice)

    # Classify
    productClassify = driver.find_element(by=By.XPATH, value=xpath_choice)
    global classifyText
    classifyText = productClassify.text

    print(""""""
    f"{Fore.green}[+] Product Title:{Style.reset} {productTitle.text}\n"
    f"{Fore.green}[+] Product Evaluate:{Style.reset} {productEvaluate.text}\n"
    f"{Fore.green}[+] Product Sold:{Style.reset} {productSold.text}\n"
    f"{Fore.green}[+] Product Store:{Style.reset} {productStore.text}\n"
    f"{Fore.green}[+] Product Price:{Style.reset} {productPrice.text}\n"
    f"{Fore.green}[+] Product Classify:{Style.reset} {Fore.cyan}{productClassify.text}{Style.reset}\n"
    """""")

    print("---------------------------------------------------")

    if countdown_seconds is not None:
        execute_countdown(countdown_seconds)


    orderTo_cart()



# Describe: Order a product to cart
start_time = 0
end_time = 0
attempts = 0
settings = load_data_from_json(SETTINGS_PATH)

def orderTo_cart():
    global start_time, attempts
    max_attempts = int(settings['attempt'])
    start_time = time.time()

    is_ariaDisabled = driver.find_element(by=By.XPATH, value=xpath_choice).get_attribute('aria-disabled')
    if is_ariaDisabled == "true": # Sold out
        attempts += 1
        print("Product was sold out")
        print("Next check")
        
        if attempts >= max_attempts: # Attempt is running out
            print("Sorry, this product was sold out today. You can choose others instead")
            get_information_about_product()
        driver.refresh()
        # Check if xpath present
        wait_for_element_present(driver, xpath_choice)
        orderTo_cart()

    else: # Available
        print("Product is Available")
        variant_select = driver.find_element(by=By.XPATH, value=xpath_choice)
        driver.execute_script("arguments[0].scrollIntoView();", variant_select)
        variant_select.click()
        print("Button clicked")

        move_to_cart_Class = 'btn.btn-solid-primary.btn--l.YuENex'
        driver.find_element(by=By.CLASS_NAME, value=move_to_cart_Class).click()
        print("Carting...")




# Wait to check quantity and price
def cart():
    quantity = int(settings['quantity'])
    wait_for_element_present(driver, '//*[@id="main"]/div/div[2]/div/div/div[3]/section/div[7]/button[4]')
    # Checkbox
    check_box = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div/div[2]/div/div/div[3]/main/section[1]/section/div[1]/div/div[1]/label/input')
    is_ariaChecked = check_box.get_attribute('aria-checked')
    if is_ariaChecked == 'false':
        driver.execute_script("arguments[0].scrollIntoView();", check_box)
        check_box.click()
        print(f"aria-checked: {check_box.get_attribute('aria-checked')}")
    else:
        print("Box is already checked")
        print(f"aria-checked: {check_box.get_attribute('aria-checked')}")


    # Quantity
    quantity_box = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div/div[2]/div/div/div[3]/main/section[1]/section/div[1]/div/div[5]/div/input')
    value_str = quantity_box.get_attribute('aria-valuenow')
    wait_for_element_present(driver, '//*[@id="main"]/div/div[2]/div/div/div[3]/main/section[1]/section/div[1]/div/div[5]/div/input')
    value_int = None
    if value_str is not None:
        value_int = int(value_str)
        print("Quantity as integer:", value_int)
    else:
        print("Value is None. Handle this case accordingly.")

    if quantity != value_int:
        print('Value is not matched')
        quantity_box.click()
        quantity_box.send_keys(Keys.CONTROL, "a")
        quantity_box.send_keys(Keys.BACKSPACE)
        quantity_box.send_keys(quantity)
        driver.find_element(by=By.XPATH, value='//*[@id="main"]/div/div[2]/div/div/div[3]/main/div[2]/div[6]').click()
        print(f"{Fore.green}[*] Updated quantity to {Fore.blue}{value_str} {Style.reset}")
        

        # Wait for price update
        time.sleep(0.6)


    # Move to checkout
    driver.find_element(by=By.CLASS_NAME, value="shopee-button-solid.shopee-button-solid--primary").click()
    print("[>>>] Navigating to checkout")
    cur_url = driver.current_url
    print(f"Current url: {cur_url}")




# TODO: FIX PAYMENT METHOD
checkout = settings['order']
def check_out():
    global end_time
    change_payment_method_xpath = '//*[@id="main"]/div/div[2]/div/div[2]/div[4]/div[1]/div/button'
    cod_box_xpath = '//*[@id="main"]/div/div[2]/div/div[2]/div[4]/div[1]/div/div/div[1]/div[2]/div[1]/span[5]/button'
    check_out_btn_xpath = '//*[@id="main"]/div/div[2]/div/div[2]/div[4]/div[2]/div[4]/button'

    wait_for_element_present(driver, check_out_btn_xpath)
    # Check if the 'cod' button is checked


    # Check if 'cod' button valid
    try: 
        cod_box = driver.find_element(by=By.XPATH, value=cod_box_xpath)# valid

        
        isCod_checked = cod_box.get_attribute('aria-checked')
        if isCod_checked == "false":
            print("Cod is not checked")
            cod_box.click()

        else:
            print("Cod is checked")

        print(f"aria-checked: {cod_box.get_attribute('aria-checked')}")

    except NoSuchElementException: # Change payment btn valid ('Cod' btn is not valid)
        print("Cod button not found. Continuing")


    checkout_btn_class = "stardust-button.stardust-button--primary.stardust-button--large.LtH6tW"
    checkout_btn = driver.find_element(by=By.CLASS_NAME, value=checkout_btn_class)
    driver.execute_script("arguments[0].scrollIntoView();", checkout_btn)

    if checkout == "on":
        checkout_btn.click()
    
    print(f"{Fore.green}[+] Order successfully.{Style.reset}")

    end_time = time.time()






def order_block():
    get_information_about_product()
    cart()
    check_out()





if __name__ == "__main__":
    menu()

    driver = uc.Chrome(headless=False, use_subprocess=False)
    time.sleep(5)

    # LOAD SETTINGS.JSON
    settings = load_data_from_json(SETTINGS_PATH)
    # Get URL
    product_url = settings['url']
    driver.get(product_url)
    time.sleep(5)
    # Login 
    sessionLogin(session=f"{settings['session']}.json")
    driver.refresh()
    print("Loading...")
    
    time.sleep(3)
    countdown_seconds = get_countdown_duration()
    order_block()
    run_time = end_time - start_time
    print(f"Run time: {run_time} seconds")




    time.sleep(100)
    driver.quit()

