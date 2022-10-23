class Logger:
    @staticmethod
    def write_to_file(event, file_name="logs.txt"):
        file = open(file_name, 'a')
        file.write(str(event) + '\n')
        file.close()

    @staticmethod
    def clean_file(file_name):
        open(file_name, 'w').close()
