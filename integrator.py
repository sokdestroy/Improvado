import csv
from workers.common import sorting


class Integrator:
    def __init__(self):
        self.result_table = []
        self.result_columns = []
        self.workers = []

    def add_worker(self, worker):
        self.workers.append(worker)

    def set_result_columns(self):
        self.result_columns = self.workers[0].columns
        for worker in self.workers:
            if len(worker.columns) < len(self.result_columns):
                self.result_columns = worker.columns
        self.result_columns = sorting(self.result_columns)

    def make_table(self):
        self.result_table.append(self.result_columns)
        for worker in self.workers:
            for data in worker.get_str():
                result_str = []
                for column in self.result_columns:
                    result_str.append(data[column])
                self.result_table.append(result_str)

    def basic_solution(self):
        pre_res = [self.result_table[0]]
        pre_res.extend(sorted(self.result_table[1:], key=lambda elem: elem[0]))
        with open('out/basic_solution.tsv', 'w', encoding='UTF-8') as out_file:
            writer = csv.writer(out_file, delimiter='\t')

            for row in pre_res:
                writer.writerow(row)
        print()
