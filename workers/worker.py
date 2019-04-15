from abc import ABC


class Worker(ABC):
    def __init__(self, file_path):
        self.file_path = file_path

    def get_str(self):
        pass
