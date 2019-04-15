import csv
from workers.worker import Worker
from workers.common import sorting


class CSVWorker(Worker):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.__csv_file = open(self.file_path, 'r', newline='')
        self.__reader = csv.reader(self.__csv_file, delimiter=',')
        self.columns = next(self.__reader)

    def get_str(self):
        for s in self.__reader:
            result = {}
            for col_number in range(len(self.columns)):
                result[self.columns[col_number]] = s[col_number]

            yield sorting(result)
        self.__csv_file.close()


if __name__ == '__main__':
    a = CSVWorker('csv_data_2.csv')
    for i in a.get_str():
        print(i)