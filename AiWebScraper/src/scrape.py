import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup
import os


def scrape_website(url):
    print("launching chrome browser")

    chrome_driver_path = os.path.abspath("./chromedriver.exe")
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        driver.get(url)
        print("Page title:", driver.title)
        page_source = driver.page_source  # Store the page source before quitting
        print("Page source:", page_source)
        time.sleep(10)
        return page_source
    finally:
        driver.quit()


def extract_body(url):
    soup = BeautifulSoup(url, 'html.parser')
    body_content = soup.body
    if body_content:
        return str(body_content)
    else:
        return None


def clean_content(content):
    soup = BeautifulSoup(content, 'html.parser')

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())
    return cleaned_content


def split_content(content, max_length=6000):
    return [
        content[i:i + max_length] for i in range(0, len(content), max_length)
    ]
