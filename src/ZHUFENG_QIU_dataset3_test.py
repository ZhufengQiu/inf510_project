from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import ZHUFENG_QIU_scrape
import time
import re
import csv
import os

def open_driver():
    caps = webdriver.DesiredCapabilities().FIREFOX
    caps['marionette'] = True
    binary = FirefoxBinary(r'/Applications/Firefox.app/Contents/MacOS/firefox')
    driver = webdriver.Firefox(firefox_binary = binary, capabilities = caps)

    #browser_driver = driver.get(url)
    return driver

'''def record_education(data):
    edu_info = {}
    main_table = data.findAll('table', {"id" : "data"})[0]
    main_body = main_table.find('tbody')
    main_row = main_body.findAll('tr')

    #Population 18 to 24 years
    #Total
    popu_18_24_total = main_row[0].findAll('td')[0].get_text()
    #Less than high school graduate
    popu_18_24_lthsg = main_row[1].findAll('td')[0].get_text()
    #High school graduate (includes equivalency)
    popu_18_24_hsg = main_row[2].findAll('td')[0].get_text()
    #Some college or associate's degree
    popu_18_24_scoad = main_row[3].findAll('td')[0].get_text()
    #Bachelor's degree or higher
    popu_18_24_bdoh = main_row[4].findAll('td')[0].get_text()

    #Population 25 years and over
    #Total
    popu_25_total = main_row[6].findAll('td')[0].get_text()
    #Less than 9th grade
    popu_25_lt9g = main_row[7].findAll('td')[0].get_text()
    #9th to 12th grade, no diploma
    popu_25_9to12 = main_row[8].findAll('td')[0].get_text()
    #High school graduate (includes equivalency)
    popu_25_hsg = main_row[9].findAll('td')[0].get_text()
    #Some college, no degree
    popu_25_sc = main_row[10].findAll('td')[0].get_text()
    #Associate's degree
    popu_25_ad = main_row[11].findAll('td')[0].get_text()
    #Bachelor's degree
    popu_25_bd = main_row[12].findAll('td')[0].get_text()
    #Graduate or professional degree
    popu_25_gopd = main_row[13].findAll('td')[0].get_text()

    edu_info["18-24 Total"] = str_to_number(popu_18_24_total)
    edu_info["18-24 Less than high school graduate"] = str_to_number(popu_18_24_lthsg)
    edu_info["18-24 High school graduate"] = str_to_number(popu_18_24_hsg)
    edu_info["18-24 Some college or associate's degree"] = str_to_number(popu_18_24_scoad)
    edu_info["18-24 Bachelor's degree or higher"] = str_to_number(popu_18_24_bdoh)

    edu_info["25 Total"] = str_to_number(popu_25_total)
    edu_info["25 Less than 9th grade"] = str_to_number(popu_25_lt9g)
    edu_info["25 9th to 12th grade"] = str_to_number(popu_25_9to12)
    edu_info["25 High school graduate"] = str_to_number(popu_25_hsg)
    edu_info["25 Some college, no degree"] = str_to_number(popu_25_sc)
    edu_info["25 Associate's degree"] = str_to_number(popu_25_ad)
    edu_info["25 Bachelor's degree"] = str_to_number(popu_25_bd)
    edu_info["25 Graduate or professional degree"] = str_to_number(popu_25_gopd)

    return edu_info'''


def loop_scrape_education(edu_data, driver, zip_codes):

    for zip in zip_codes:
        try:
            ZHUFENG_QIU_scrape.scrape_edu_by_zip(driver, edu_data, zip)
        except IndexError:
            driver.back()
            continue
        except:
            continue
        '''edu_info = {}

        element_search = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, "GO")))
        driver.find_element_by_id("cfsearchtextbox").send_keys(zip)
        #element_search = driver.find_element_by_link_text("GO")
        driver.execute_script("arguments[0].click();", element_search)

        #driver.implicitly_wait(10)
        #element_education = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, "Education")))

        element_education = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='leftnav']/a[4]")))
        driver.execute_script("arguments[0].click();", element_education)

        driver.implicitly_wait(10)

        element_attainment = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='cf-content']/div[@class='ng-scope']/div[@class='links-container']/div/div[1]/ul/li[1]/div/a")))
        driver.execute_script("arguments[0].click();", element_attainment)
        #element_attainment_stale = driver.find_element_by_link_text("Educational Attainment (High School, Bachelor's, Advanced Degree, ...)")
        #WebDriverWait(driver, 10).until(EC.staleness_of(element_attainment))

        element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "r1")))
        soup = BeautifulSoup(driver.page_source, 'lxml')
        edu_info = record_education(soup)
        data[zip] = edu_info

        #element_search_stale = driver.find_element_by_link_text("GO")
        #WebDriverWait(driver, 10).until(EC.staleness_of(element_search_stale))'''
        driver.back()

    return edu_data

'''def record_income(data):
    income_info = {}
    main_table = data.findAll('table', {"id" : "data"})[0]
    main_body = main_table.find('tbody')
    main_row = main_body.findAll('tr')

    #Employment status
    #Population 16 years and over
    popu_16 = main_row[1].findAll('td')[0].get_text()
    #In labor force
    popu_16_ilf = main_row[2].findAll('td')[0].get_text()
    #Civilian labor force
    popu_16_clf = main_row[3].findAll('td')[0].get_text()
    #Employed
    popu_16_e = main_row[4].findAll('td')[0].get_text()
    #Unemployed
    popu_16_u = main_row[5].findAll('td')[0].get_text()
    #Armed Forces
    popu_16_af = main_row[6].findAll('td')[0].get_text()
    #Not in labor force
    popu_16_nilf = main_row[7].findAll('td')[0].get_text()

    #Median household income (dollars)
    med_household_income = main_row[77].findAll('td')[0].get_text()
    #Mean household income (dollars)
    mean_household_income = main_row[78].findAll('td')[0].get_text()

    #Median family income (dollars)
    median_family_income = main_row[104].findAll('td')[0].get_text()
    #Mean family income (dollars)
    mean_family_income = main_row[105].findAll('td')[0].get_text()
    #Per capita income (dollars)
    per_capita_income = main_row[107].findAll('td')[0].get_text()

    #Median nonfamily income (dollars)
    median_nonfamily_income = main_row[110].findAll('td')[0].get_text()
    #Mean nonfamily income (dollars)
    mean_nonfamily_income = main_row[111].findAll('td')[0].get_text()
    #Median earnings for workers (dollars)
    median_earnings_for_workers = main_row[113].findAll('td')[0].get_text()

    #Civilian noninstitutionalized population
    civ_popu = main_row[118].findAll('td')[0].get_text()
    #With health insurance coverage
    health_insurance = main_row[119].findAll('td')[0].get_text()
    #No health insurance coverage
    no_health_insurance = main_row[122].findAll('td')[0].get_text()


    income_info["Population 16 years and over"] = str_to_number(popu_16)
    income_info["In labor force"] = str_to_number(popu_16_ilf)
    income_info["Civilian labor force"] = str_to_number(popu_16_clf)
    income_info["Employed"] = str_to_number(popu_16_e)
    income_info["Unemployed"] = str_to_number(popu_16_u)
    income_info["Armed Forces"] = str_to_number(popu_16_af)
    income_info["Not in labor force"] = str_to_number(popu_16_nilf)

    income_info["Median household income"] = str_to_number(med_household_income)
    income_info["Mean household income"] = str_to_number(mean_household_income)

    income_info["Median family income"] = str_to_number(median_family_income)
    income_info["Mean family income"] = str_to_number(mean_family_income)
    income_info["Per capita income"] = str_to_number(per_capita_income)

    income_info["Median nonfamily income"] = str_to_number(median_nonfamily_income)
    income_info["Mean nonfamily income"] = str_to_number(mean_nonfamily_income)
    income_info["Median earnings for workers"] = str_to_number(median_earnings_for_workers)

    income_info["Civilian noninstitutionalized population"] = str_to_number(civ_popu)
    income_info["With health insurance coverage"] = str_to_number(health_insurance)
    income_info["No health insurance coverage"] = str_to_number(no_health_insurance)

    return income_info'''

def loop_scrape_income(inc_data, driver, zip_codes):
    for zip in zip_codes:
        try:
            ZHUFENG_QIU_scrape.scrape_inc_by_zip(driver, inc_data, zip)
        except IndexError:
            driver.back()
            continue
        except:
            continue
        '''income_info = {}

        element_search = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, "GO")))
        driver.find_element_by_id("cfsearchtextbox").send_keys(zip)
        #element_search = driver.find_element_by_link_text("GO")
        driver.execute_script("arguments[0].click();", element_search)

        driver.implicitly_wait(10)
        element_income = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='leftnav']/a[7]")))
        #element_income = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, "Income")))
        #element_income = driver.find_element_by_xpath("//div[@id='leftnav']/a[7]")
        driver.execute_script("arguments[0].click();", element_income)
        #WebDriverWait(driver, 10).until(EC.staleness_of(element_income))

        #WebDriverWait(driver, 10).until(EC.staleness_of(element_search))
        #WebDriverWait(driver, 10).until(EC.staleness_of(element_income))

        #time.sleep(1)

        element_economic = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='cf-content']/div[@class='ng-scope']/div[@class='links-container']/div/div[1]/ul/li[1]/div/a")))
        driver.execute_script("arguments[0].click();", element_economic)

        element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "r1")))
        soup = BeautifulSoup(driver.page_source, 'lxml')
        income_info = record_income(soup)
        data[zip] = income_info'''

        driver.back()

        #WebDriverWait(driver, 10).until(EC.staleness_of(element_economic))

    return inc_data

'''def str_to_number(string):
    string =  re.findall(r"\d+\.?\d*", string)
    new_string = ''
    for element in string:
        new_string = new_string + element
    if '.' in new_string:
        number = float(new_string)
    elif new_string == '':
        number = 0
    else:
        number = int(new_string)
    return number'''

def main():
    url = 'https://factfinder.census.gov/faces/nav/jsf/pages/community_facts.xhtml?src=bkmk'
    zip_codes = [94127, 94105, 94123, 94130, 94131, 94114, 94129, 94116, 94117, 94121, 94118, 94107, 94122, 94112, 94111, 94132, 94115, 94134, 94110, 94109, 94133, 94124, 94108, 94103, 94102, 94104, 94128]
    #zip_codes = [94127, 94105]


    driver = open_driver()
    driver.get(url)
    edu_data = {}
    income_data = {}
    edu_data = loop_scrape_education(edu_data, driver, zip_codes)
    driver.close()
    for zip in zip_codes:
        if zip not in list(edu_data.keys()):
            driver = open_driver()
            driver.get(url)
            try:
                ZHUFENG_QIU_scrape.scrape_edu_by_zip(driver, edu_data, zip)
                driver.close()
            except IndexError:
                driver.close()
                continue
            except:
                driver.close()
                continue

    driver = open_driver()
    driver.get(url)
    income_data = loop_scrape_income(income_data, driver, zip_codes)
    driver.close()
    for zip in zip_codes:
        if zip not in list(income_data.keys()):
            driver = open_driver()
            driver.get(url)
            try:
                ZHUFENG_QIU_scrape.scrape_inc_by_zip(driver, income_data, zip)
                driver.close()
            except IndexError:
                driver.close()
                continue
            except:
                driver.close()
                continue

    total_data = {}

    for key, value in edu_data.items():
        element = {}
        element.update(value)
        if key in income_data.keys():
            element.update(income_data[key])
        total_data[key] = element

    csv_columns = ["zip_code", "18-24 Total", "18-24 Less than high school graduate", "18-24 High school graduate", "18-24 Some college or associate's degree", "18-24 Bachelor's degree or higher", "25 Total", "25 Less than 9th grade", "25 9th to 12th grade", "25 High school graduate", "25 Some college, no degree", "25 Associate's degree", "25 Bachelor's degree", "25 Graduate or professional degree", "Population 16 years and over", 'In labor force', 'Civilian labor force', 'Employed', 'Unemployed', 'Armed Forces', 'Not in labor force', 'Median household income', 'Mean household income', 'Median family income', 'Mean family income', 'Per capita income', 'Median nonfamily income', 'Mean nonfamily income', 'Median earnings for workers', 'Civilian noninstitutionalized population', 'With health insurance coverage', 'No health insurance coverage']
    csv_file = "data_3_test.csv"
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(csv_columns)
            for key, value in total_data.items():
                row = [key]
                row.extend(list(total_data[key].values()))
                writer.writerow(row)
    except IOError:
        print("File write error!")

if __name__ == "__main__":
    main()
