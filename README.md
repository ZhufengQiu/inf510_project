# inf510_project
inf551_final_project

In addition to the python standard library, this project also requires these packages:
  - numpy, pandas, selenium, BeautifulSoup, requests, basemap, folium, seaborn, matplotlib
 

After downloading the Python files and data files and putting them under the same directory, then we can execute them in command line like this way:

# Scrape and store data

# 1.Scrape data remotely

- python ZHUFENG_QIU_hw5.py -s remote

- python ZHUFENG_QIU_hw5.py --source=remote

    After invoking this code, the ZHUFENG_QIU_hw5.py (main file) will start to call the other four files to scrape data from Websites/API. Then, data will be written to disk first, and ZHUFENG_QIU_hw5.py will read these data files and combine them into a predefined database.

    The dataset contains data for April and May 2018.
# 2.Scrape data locally

- python ZHUFENG_QIU_hw5.py -s local

- python ZHUFENG_QIU_hw5.py --source=local

    After invoking this code, the ZHUFENG_QIU_hw5.py (main file) will read data files in disk directly and combine them into a predefined database.
# 3.Scrape test data

- python ZHUFENG_QIU_hw5.py -s test

- python ZHUFENG_QIU_hw5.py --source=test

    The same procedure as scraping data remotely and locally. The difference is that the dataset contains data from May 12, 2018 to May 18, 2018, which is smaller this time.
# Analysis Part

 This part is showen in zhufeng_qiu.ipynb
 


# ################

# The guide of selenium library's downloading
1. Download the Selenium Library.
   pip install selenium 
2. Download the Firefox browser.
3. Download geckodriver for Firefox browser.
   Firefox's geckodriver: https://github.com/mozilla/geckodriver/releases 
4. Place geckodriver in /usr/bin or /usr/local/bin to make sure it’s in your PATH. 
   Specially, for Mac OS users, geckodriver can be placed under this path: /Applications/Firefox.app/Contents/MacOS
5. Copy the address of the Firefox browser to the eighteenth line of ZHUFENG_QIU_dataset1.py
   Copy the address of the Firefox browser to the sixteenth line of ZHUFENG_QIU_dataset3.py
   Edit ZHUFENG_QIU_dataset1_test.py and ZHUFENG_QIU_dataset3_test.py as above
   For me, the address of my Firefox browser is '/Applications/Firefox.app/Contents/MacOS/firefox'


# ################
# The guide of basemap and folium library's downloading
Before runing zhufeng_qiu.ipynb, implement these codes in command line to download Basemap and folium library:

$ conda install -c anaconda basemap

$ conda install -c conda-forge folium

$ conda install -c conda-forge/label/gcc7 folium

$ conda install -c conda-forge/label/cf201901 folium
 
   
# ##############
# It seems that GitHub is not able to display a dynamic map, so the heatmap should be checked locally after clonning the zhufeng_qiu.ipynb.
