import csv

def save_to_csv(file_path, data, header=None):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        if header:
            writer.writerow(header)
        writer.writerows(data)

def read_from_csv(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    return data
