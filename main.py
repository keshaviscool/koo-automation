from time import time
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
import os
import pandas
import time

USERNAME = 'kesha'

def get_driver():
    optons = webdriver.ChromeOptions()
    optons.add_argument(f'user-data-dir=C:\\Users\\{USERNAME}\\AppData\\Local\\Google\\Chrome\\User Data')
    optons.add_argument('--profile-directory=Profile 1')

    driver = webdriver.Chrome('./chromedriver', options=optons)
    return driver

driver = get_driver()
df = pandas.read_csv('data.csv')


# get each row
for index, row in df.iterrows():
    is_done = row['done']
    if str(is_done).lower().strip() == 'nan':
        is_done = False
    else:
        is_done = True

    if is_done:
        continue

    caption = row['caption']
    img_name = row['image']
    driver.get('https://www.kooapp.com/create')
    file_name = os.path.join(os.getcwd(), "media", img_name)

    input = driver.find_element_by_id('dp')
    input.send_keys(file_name)

    textarea = driver.find_element_by_xpath('//*[@id="CreateTextArea"]/textarea')
    # type in text
    textarea.send_keys(caption)

    post_btn = driver.find_element_by_id('PostButton')
    post_btn.click()

    try:
        not_now_btn = driver.find_element_by_xpath('//*[@id="childSectionLayout"]/div/div/div/div[2]/div/div[3]/button[1]')
        not_now_btn.click()
    except ElementClickInterceptedException:
        pass
    # update done column for this row
    df.at[index, 'done'] = 1
    df.to_csv('data.csv', index=False)
    time.sleep(2)
