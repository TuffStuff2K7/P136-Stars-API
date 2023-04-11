import csv

with open('D:\Code\WhJr\Python\P136\Environment\data.csv', newline = "") as f:
    csvImport = list(csv.reader(f))

headers = csvImport[0]
star_data = csvImport[1:]

data = []

for i, line in enumerate(star_data):
    data.append({
        "Index": i,
        headers[0]: line[0],
        headers[1]: float(line[1]),
        headers[2]: float(line[2]),
        headers[3]: float(line[3]),
        headers[4]: float(line[4]),
    })
