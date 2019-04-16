import csv
from workers.common import sorting
from logger import Logger

class Integrator:
    def __init__(self):
        self.result_table = []
        self.result_columns = []
        self.workers = []
        self.logger = Logger()

    def add_worker(self, worker):
        worker.set_logger(self.logger)
        self.workers.append(worker)

    def set_result_columns(self):
        self.result_columns = self.workers[0].columns
        for worker in self.workers:
            if len(worker.columns) < len(self.result_columns):
                self.result_columns = worker.columns
        self.result_columns = sorting(self.result_columns)

    def make_table(self):
        log_file = open('out/logfile.log', 'w', encoding='UTF-8')

        self.result_table.append(self.result_columns)
        for worker in self.workers:
            for data in worker.get_str():
                if data is None:
                    continue
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

    def __comapare_row(self, row1, row2):
        # возвращает True, если строки равны
        result = True
        if len(row2) == 0 or len(row1) == 0:
            return not result
        for col_number in range(len(self.result_columns)):
            if self.result_columns[col_number][0] != 'D':
                return result

            if row1[col_number] != row2[col_number]:
                return not result
        return result

    def __sum_m_col(self, row1, row2):
        result_row = []
        for i in self.result_columns:
            if i[0] == 'D':
                result_row.append(row1[self.result_columns.index(i)])
            elif i[0] == 'M':
                result_row.append(int(row1[self.result_columns.index(i)]) + int(row2[self.result_columns.index(i)]))
        return result_row

    def advanced_solution(self):
        result_table = []
        repeating_rows = []
        for row1 in self.result_table:
            result_row = []
            for row2 in self.result_table[self.result_table.index(row1)+1:]:
                if self.__comapare_row(row1, row2):
                    repeating_rows.append(row2)
                    if self.__comapare_row(row2, result_row):
                        result_row = self.__sum_m_col(result_row, row2)
                    else:
                        result_row = self.__sum_m_col(row1, row2)
            if len(result_row) != 0:
                result_table.append(result_row)
            else:
                if row1 not in repeating_rows:
                    result_table.append(row1)

            char_elems = [i for i in self.result_columns if i[0] == 'D']

            result_table = sorted(result_table, key=lambda elem: [elem[i] for i in range(len(char_elems))])

            result_table[0] = [i[0] + 'S' + i[1:] if i[0] == 'M' else i for i in self.result_columns]

        with open('out/advanced_solution.tsv', 'w', encoding='UTF-8') as out_file:
            writer = csv.writer(out_file, delimiter='\t')

            for row in result_table:
                writer.writerow(row)
