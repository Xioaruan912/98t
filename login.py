#login.py

import time
from get_url import get_target_url
from selenium.webdriver.common.by import By
from config import ACC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pinlun import pinlun
from sign_in import sign_in
from open_chrome import open_chorme


def input_main(acc):
    #主要输入表单
    url = get_target_url()
    driver = open_chorme()
    driver.get(url=url)
    driver.find_element(By.XPATH,"""/html/body/div[3]/div/div[2]/div[2]/div[2]/span""").click()
    driver.find_element(By.XPATH,"""/html/body/a[1]""").click()
    url = driver.current_url
    driver.find_element(By.XPATH,"""//*[@id="ls_username"]""").send_keys(acc.username)
    driver.find_element(By.XPATH,"""//*[@id="ls_password"]""").send_keys(acc.password)
    driver.find_element(By.XPATH,"""//*[@id="lsform"]/div/div/table/tbody/tr[2]/td[3]/button/em""").click()
    select_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "questionid"))
    )
    dropdown = Select(select_element)
    dropdown.select_by_value("3")
    input_box = driver.find_element(By.NAME, "answer")
    input_box.send_keys(acc.question)
    driver.find_element(By.NAME, "loginsubmit").click()
    time.sleep(4)
    for i in range(3):
        pinlun(driver=driver, url=url, acc=acc)
    mess = sign_in(driver=driver, url=url)
    return mess