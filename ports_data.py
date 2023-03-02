import csv


class bNET_data:
    _VERSION_ = "1.0"

    def __init__(self):
        self.data = {}

    def read_data(self):
        with open('ports.csv', mode='r') as file:
            data = csv.reader(file)
            next(data)
            for row in data:
                self.data[row[0]] = row[1]
