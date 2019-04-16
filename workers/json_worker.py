import json
from workers.worker import Worker
from workers.common import sorting, check_for_bad_symbols


class JsonWorker(Worker):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.__json_file = open(self.file_path, 'r', encoding='UTF-8')
        self.__data = json.load(self.__json_file)['fields']
        self.columns = self.__data[0].keys()
        self.__json_file.close()

    def get_str(self):
        for d in self.__data:
            if check_for_bad_symbols(d):
                yield sorting(d)
            else:
                self.logger.write_message(d, self.file_path)
                yield None


if __name__ == '__main__':
    a = JsonWorker('json_data.json')
    for i in a.get_str():
        print(i)

