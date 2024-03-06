import csv

def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            data.append(row)
    return data

if __name__ == "__main__":
    csv_data = read_csv("roles_and_policies.csv")
    for row in csv_data:
        print(row)  # Or do any other processing you need
