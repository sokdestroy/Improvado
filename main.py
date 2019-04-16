import os

from workers.csv_worker import CSVWorker
from workers.json_worker import JsonWorker
from workers.xml_worker import XMLWorker
from integrator import Integrator


if __name__ == '__main__':
    resource_dir = 'resources'

    files = os.listdir(resource_dir)

    integrator = Integrator()

    for file in files:
        postfix = file.split('.')[1]
        path = resource_dir + '/' + file
        if postfix == 'csv':
            integrator.add_worker(CSVWorker(path))
        elif postfix == 'json':
            integrator.add_worker(JsonWorker(path))
        elif postfix == 'xml':
            integrator.add_worker(XMLWorker(path))

    integrator.set_result_columns()
    integrator.make_table()
    integrator.basic_solution()
    integrator.advanced_solution()
    print()