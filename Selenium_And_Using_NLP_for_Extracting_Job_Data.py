#import undetected_chromedriver as uc
#from selenium.webdriver.common.by import By

#*  pip install selenium undetected-chromedriver

#options = uc.ChromeOptions()
#options.headless = False
#driver = uc.Chrome(options=options)

#url = "https://javascript-heavy-website.com"

#driver.get(url)

#driver.implicitly_wait(10)

#print(driver.page_source)

#driver.quit





# ...requires chrome browser, or on ubuntu linux, install dependencies: apt-get install libappindicator1 fonts-liberation   ; and install the chrome stable version from chrome official, .deb





import cloudscraper
from bs4 import BeautifulSoup
import spacy

nlp = spacy.load("en_core_web_sm")

#* pip install cloudscraper
#* pip install spacy
#* python -m spacy download en_core_web_sm   OR, use large:
#* python -m spacy download en_core_web_lg


def scrape_url(url):
    scraper = cloudscraper.create_scraper()
    response = scraper.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        company_name = soup.select_one(".company_class")

        company_name = company_name.get_text(strip=True) if company_name else "Unknown"


        use = soup.get_text(strip=True)
        doc = nlp(use)

        extracted_data = {
            "company": company_name,
            "entities": []
        }

        for ent in doc.ents:
            extracted_data["entities"].append(({"text": ent.text, "label": ent.label_}))

        return extracted_data
    else:
        return {"error": "Failed to fetch page"}

job_url = "https://job-boards.eu.greenhouse.io/neptuneai/jobs/4533761101"
job_data = scrape_url(job_url)
print(job_data)