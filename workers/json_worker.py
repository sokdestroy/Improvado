import json
from workers.worker import Worker
from workers.common import sorting


class JsonWorker(Worker):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.__json_file = open(self.file_path, 'r', encoding='UTF-8')
        self.__data = json.load(self.__json_file)['fields']
        self.columns = self.__data[0].keys()
        self.__json_file.close()

    def get_str(self):
        for d in self.__data:
            yield sorting(d)


if __name__ == '__main__':
    a = JsonWorker('json_data.json')
    for i in a.get_str():
        print(i)

