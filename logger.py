class Logger:
    def __init__(self):
        self.log_file = open('out/logfile.log', 'w', encoding='UTF-8')

    def __del__(self):
        self.log_file.close()

    def write_message(self, some_dict, path):
        self.log_file.write('Bad row in file "' + path + '"\n')
        self.log_file.write('ROW: ' + str(some_dict) + '\n\n')
