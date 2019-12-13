import ZHUFENG_QIU_dataset1
import ZHUFENG_QIU_dataset2
import ZHUFENG_QIU_dataset3
import ZHUFENG_QIU_dataset1_test
import ZHUFENG_QIU_dataset2_test
import ZHUFENG_QIU_dataset3_test
import os
import csv
import numpy as np
import pandas as pd
import sys
import getopt

def read_data(file_path):
    #-source=remote
    #when the data file is not existed in the directory, scrape function is used to get data
    if not os.path.isfile(file_path):
        if file_path == 'data_1.csv':
            ZHUFENG_QIU_dataset1.main()
        elif file_path == 'data_2.csv':
            ZHUFENG_QIU_dataset2.main()
        elif file_path == 'data_3.csv':
            ZHUFENG_QIU_dataset3.main()
    #when the data file is invalid, scrape function is used to get data
    else:
        with open(file_path,"r") as f:
            reader = csv.reader(f,delimiter = ",")
            data = list(reader)
            row_count = len(data)
        if row_count == 1:
            if file_path == 'data_1.csv':
                ZHUFENG_QIU_dataset1.main()
            elif file_path == 'data_2.csv':
                ZHUFENG_QIU_dataset2.main()
            elif file_path == 'data_3.csv':
                ZHUFENG_QIU_dataset3.main()
    #-source=local
    #get data from local directory
    file_data = pd.read_csv(file_path)
    return file_data

def read_data_test(file_path):
    #when the data file is not existed in the directory, scrape function is used to get data
    if not os.path.isfile(file_path):
        if file_path == 'data_1_test.csv':
            ZHUFENG_QIU_dataset1_test.main()
        elif file_path == 'data_2_test.csv':
            ZHUFENG_QIU_dataset2_test.main()
        elif file_path == 'data_3_test.csv':
            ZHUFENG_QIU_dataset3_test.main()
    #when the data file is invalid, scrape function is used to get data
    else:
        with open(file_path,"r") as f:
            reader = csv.reader(f,delimiter = ",")
            data = list(reader)
            row_count = len(data)
        if row_count == 1:
            if file_path == 'data_1_test.csv':
                ZHUFENG_QIU_dataset1_test.main()
            elif file_path == 'data_2_test.csv':
                ZHUFENG_QIU_dataset2_test.main()
            elif file_path == 'data_3_test.csv':
                ZHUFENG_QIU_dataset3_test.main()
    #get data from local directory
    file_data = pd.read_csv(file_path)
    return file_data

def main(argv):
    source_flag = ""
    opts, args = getopt.getopt(argv, "s:", ["source="])
    for opt, arg in opts:
        if opt in ("-s", "--source"):
            source_flag = arg

    if (source_flag == "remote") or (source_flag == "local"):
        #1.Pull data from the three data sources
        print("Scrape data set 1......")
        data1 = read_data('data_1.csv')
        print("Scrape data set 2......")
        data2 = read_data('data_2.csv')
        print("Scrape data set 3......")
        data3 = read_data('data_3.csv')

        #2.Clean and pre-process the data
        #2.1 rename columns
        data1 = data1.rename(columns={'X':'lng'})
        data1 = data1.rename(columns={'Y':'lat'})
        data2 = data2.rename(columns={'incident_number':'IncidntNum'})

        data2.drop(['id'],axis=1,inplace=True)

        #2.2 merge data1 and data2, and then delete the duplicate records
        data_1_2 = pd.merge(data1, data2, on=['IncidntNum','lat', 'lng'])
        data_1_2.drop_duplicates(subset=None, keep='first', inplace=True)

        #2.3 merge data1, 2 & 3
        #This command line will remove locations that are not in San Francisco implicitly
        total_data = pd.merge(data_1_2, data3, on=['zip_code'])

        #2.4 clean invalid geographical data
        total_data.lat = total_data["lat"].replace(-1,np.nan)
        total_data.lng = total_data["lng"].replace(-1,np.nan)


        #2.5 show the final data
        print("Number of record:")
        print(total_data.shape[0])
        print()
        print("Colums' Information:")
        print(total_data.columns)
        print()
        print("Data's information:")
        print(total_data.info())
        print()
        print("Data's description:")
        print(total_data.describe())


        #3.Store the data (switch DataFrame into CSV file)
        total_data.to_csv(r'total_data.csv')

        #Bonus data source
        '''
        4.Analyze the data
        4.1 analyze crime by category
        4.2 count and visualize crime by time (week/hour)
        4.3 analyze by district
        4.4 analyze crime by edcation attainment
        4.5 analyze crime by income level
        4.6 visualization
        4.6.1 visualize all crimes on the map by using latitude, longtitude, zip code, and ArcGIS server
        4.6.2 visualize individual types of crime on the map
        4.6.3 heatmap
    
        '''
    elif source_flag == "test":
        #1.Pull data from the three data sources
        print("Scrape test data set 1......")
        data1_test = read_data_test('data_1_test.csv')
        print("Scrape test data set 2......")
        data2_test = read_data_test('data_2_test.csv')
        print("Scrape test data set 3......")
        data3_test = read_data_test('data_3_test.csv')

        #2.Clean and pre-process the data
        #2.1 rename columns
        data1_test = data1_test.rename(columns={'X':'lng'})
        data1_test = data1_test.rename(columns={'Y':'lat'})
        data2_test = data2_test.rename(columns={'incident_number':'IncidntNum'})

        data2_test.drop(['id'],axis=1,inplace=True)

        #2.2 merge data1 and data2, and then delete the duplicate records
        data_1_2_test = pd.merge(data1_test, data2_test, on=['IncidntNum','lat', 'lng'])
        data_1_2_test.drop_duplicates(subset=None, keep='first', inplace=True)

        #2.3 merge data1, 2 & 3
        #This command line will remove locations that are not in San Francisco implicitly
        total_data_test = pd.merge(data_1_2_test, data3_test, on=['zip_code'])

        #2.4 clean invalid geographical data
        total_data_test.lat = total_data_test["lat"].replace(-1,np.nan)
        total_data_test.lng = total_data_test["lng"].replace(-1,np.nan)


        #2.5 show the final data
        print("Number of record:")
        print(total_data_test.shape[0])
        print()
        print("Colums' Information:")
        print(total_data_test.columns)
        print()
        print("Data's information:")
        print(total_data_test.info())
        print()
        print("Data's description:")
        print(total_data_test.describe())


        #3.Store the data (switch DataFrame into CSV file)
        total_data_test.to_csv(r'total_data_test.csv')

if __name__ == "__main__":
    main(sys.argv[1:])
