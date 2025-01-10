import csv

with open('csv_file.csv', 'w', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter = "#")
    csv_writer.writerow(['Name', 'Surname', 'Age', 'languages'])
    csv_writer.writerow(['G', 'M', '36', 'Python'])
    csv_writer.writerow(['D', 'M', '17', 'PsInt'])
    csv_writer.writerow(['D', 'G', '17', 'Java'])
    csv_writer.writerow(['F', 'D', '18', 'Negro unga unga'])
    