from utilities.data_reader_util import read_json_data, read_csv_data, read_excel_data

# Read JSON data
json_data = read_json_data("../testdata/logindata.json")

# Read CSV data
csv_data = read_csv_data("../testdata/logindata.csv")

# Read Excel data
excel_data = read_excel_data("../testdata/logindata.xlsx")

print(json_data)
print(csv_data)
print(excel_data)
