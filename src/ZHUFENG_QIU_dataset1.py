from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import time

def str_to_date(str):
    date = datetime.strptime(str , '%m/%d/%Y').date()
    return date

def open_driver():
    caps = webdriver.DesiredCapabilities().FIREFOX
    caps['marionette'] = True
    binary = FirefoxBinary(r'/Applications/Firefox.app/Contents/MacOS/firefox')
    driver = webdriver.Firefox(firefox_binary = binary, capabilities = caps)
    return driver

def jump_to_data_table(driver, url):
    driver.get(url)
    element_table = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'View Data')))
    driver.execute_script("arguments[0].click();", element_table)

    return driver

def scrape(driver, scrape_year, scrape_month, scrape_day):
    data = []
    element_next = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="pager-button-next"]')))
    element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '(//td[@data-cell-render-type="text"])[26]')))

    soup = BeautifulSoup(driver.page_source, 'lxml')
    main_table = soup.findAll('table')
    main_body = main_table[0].find('tbody')
    main_row = main_body.findAll('tr')
    page_data, date = page_record(main_row)
    data.extend(page_data)

    while True:
        element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '(//td[@data-cell-render-type="text"])[13]')))
        element_next = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="pager-button-next"]')))
        driver.execute_script("arguments[0].click();", element_next)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        main_table = soup.findAll('table')
        main_body = main_table[0].find('tbody')
        main_row = main_body.findAll('tr')
        page_data, date = page_record(main_row)
        data.extend(page_data)
        year = date.year
        month = date.month
        day = date.day
        if year == scrape_year:
            if month == scrape_month:
                if day == scrape_day:
                    break
        #element_stale = driver.find_element_by_xpath('//button[@class="pager-button-next"]')
        WebDriverWait(driver, 30).until(EC.staleness_of(element))
    return data


def page_record(main_row):
    rows_info = []
    for row in main_row:
        row_info = {}
        td = row.findAll('td')
        incidnt_num = td[0].find('div').get_text().strip()
        category = td[1].find('div').get_text().strip()
        descript = td[2].find('div').get_text().strip()
        day_of_week = td[3].find('div').get_text().strip()
        date = td[4].find('div').get_text().strip()
        time = td[5].find('div').get_text().strip()
        pd_district = td[6].find('div').get_text().strip()
        resolution = td[7].find('div').get_text().strip()
        address = td[8].find('div').get_text().strip()
        X = td[9].find('div').get_text().strip()
        Y = td[10].find('div').get_text().strip()
        location = td[11].find('div').get_text().strip()
        pd_id = td[12].find('div').get_text().strip()

        row_info["IncidntNum"] = incidnt_num
        row_info["Category"] = category
        row_info["Descript"] = descript
        row_info["DayOfWeek"] = day_of_week
        row_info["Date"] = date
        row_info["Time"] = time
        row_info["PdDistrict"] = pd_district
        row_info["Resolution"] = resolution
        row_info["Address"] = address
        row_info["X"] = X
        row_info["Y"] = Y
        row_info["Location"] = location
        row_info["PdId"] = pd_id

        rows_info.append(row_info)
    date = str_to_date(date)

    return rows_info, date



def main():
    url = "https://data.sfgov.org/Public-Safety/Police-Department-Incident-Reports-Historical-2003/tmnf-yvry"
    driver = open_driver()
    jump_to_data_table(driver, url)
    #Choose the start day to scrape data from the website
    data = scrape(driver, 2018, 4, 12)

    driver.close()
    csv_columns = ['IncidntNum','Category','Descript','DayOfWeek','Date','Time','PdDistrict','Resolution','Address','X','Y','Location','PdId']
    csv_file = "data_1.csv"
    i = 0
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
                i += 1
                if i > 9000:
                    break
    except IOError:
        print("File write error!")


if __name__ == "__main__":
    main()


