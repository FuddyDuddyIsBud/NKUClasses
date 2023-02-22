import requests
import csv

url = "http://studenthome.hh.nku.edu/~poet2/Migrated_Servers_01092022.txt"
column_names = ['Name', 'OS', 'IP Address', 'Size', 'convert time']

response = requests.get(url)
with open("Migrated_Servers.csv", "w", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=column_names)
    writer.writeheader()
    writer.writerows(csv.DictReader(response.text.splitlines(), delimiter='\t', fieldnames=column_names))

print("File downloaded and saved as Migrated_Servers.csv")
