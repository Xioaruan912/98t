import shutil
import os
from  selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from loguru import logger
from selenium.webdriver.chrome.service import Service

def open_chorme():
    chrome_options = webdriver.ChromeOptions()
    # proxy_address = 'http://127.0.0.1:7897'
    # chrome_options.add_argument(f'--proxy-server={proxy_address}')

    #反反爬虫
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--start-maximized")  # 浏览器窗口最大化

    #禁用图形界面
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")

    #默认配置
    chrome_options.add_experimental_option("detach", True)  # 关键参数
    chrome_options.add_argument("--log-level=INFO")  # 设置日志级别为INFO
    chrome_options.add_argument("–disable-web-security")  # 禁用Web安全
    chrome_options.add_argument("–disable-extensions")  # 禁用扩展
    chrome_options.add_argument("–disable-notifications")  # 禁用通知
    chrome_options.add_argument("--disable-infobars")  # 隐藏"Chrome正受到自动测试软件的控制"的通知
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])  # 防止显示该信息
    chrome_options.add_experimental_option('useAutomationExtension', False)  # 不使用自动化扩展

    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")  # 设置user-agent

    #处理 chromedriver

    chrome_driver_path = r"""./Chorme_driver/"""
    chrome_driver = chrome_driver_path + 'chromedriver.exe'
    # chrome_driver = os.path.join(chrome_driver_path, 'chromedriver')  # Linux 下的文件名
    if not os.path.exists(chrome_driver):
        logger.info("下载Chromedriver")
        if not os.path.exists(chrome_driver_path):
            os.mkdir(chrome_driver_path)
        driver_path = ChromeDriverManager().install()
        logger.info("driver_path : " + driver_path)
        shutil.copy(driver_path, chrome_driver)
        logger.info("下载至:" + chrome_driver + "成功")
    service = Service(chrome_driver)   #自动配置Chrome爬虫环境 运用在第一次运行的电脑使用
    driver = webdriver.Chrome(options=chrome_options,service = service)  #service = service 上面的取消后要加入该配置
    return driver
