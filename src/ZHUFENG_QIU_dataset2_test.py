import csv
import requests

def open_data():
    data = {}
    i = 0
    with open('data_1_test.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        next(csvfile)
        for row in readCSV:
            row_coord = {}
            row_coord["incident_id"] = row[0]
            row_coord["lat"] = row[10]
            row_coord["lng"] = row[9]
            data[i] = row_coord
            i += 1
    return data

def switch_to_zip_code(lat, lng):
    url = f'https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lng}&key=AIzaSyDTcf4DiMftALWtHG3MKQ4gz5dZrTBQ0sU'
    r = requests.get(url)
    results = r.json()['results']
    for add_infos in results:
        add_info = add_infos["address_components"]
        for element in add_info:
            if element['types'] == ['postal_code']:
                zip_code = int(element["long_name"])
                break

    return zip_code

def switch_data(data):
    total_data = {}
    for id, info in data.items():
        id_data = {}
        lat = info["lat"]
        lng = info["lng"]

        zip_code = switch_to_zip_code(lat, lng)
        id_data.update(info)
        id_data["zip_code"] = zip_code
        total_data[id] = id_data
    return total_data

def main():
    data = open_data()
    total_data = switch_data(data)

    csv_columns = ['id', 'incident_number', 'lat', 'lng', 'zip_code']
    csv_file = "data_2_test.csv"
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


