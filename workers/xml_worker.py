import xml.etree.ElementTree as etree
from workers.worker import Worker
from workers.common import sorting, check_for_bad_symbols


class XMLWorker(Worker):
    def __init__(self, file_path):
        super().__init__(file_path)

        self.__root = etree.parse(self.file_path).getroot()
        self.columns = []

        for objects in self.__root:
            for object in objects:
                self.columns.extend(object.attrib.values())
        self.columns = self.columns

    def get_str(self):
        for objects in self.__root:
            res = {}
            for object in objects:
                try:
                    value = int(object.find('value').text)
                except ValueError:
                    value = object.find('value').text
                res[list(object.attrib.values())[0]] = value

            if check_for_bad_symbols(res):
                yield sorting(res)
            else:
                self.logger.write_message(res, self.file_path)
                yield None


if __name__ == '__main__':
    a = XMLWorker('xml_data.xml')
    for i in a.get_str():
        print(i)