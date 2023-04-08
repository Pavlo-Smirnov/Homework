import logging

class CustomFile:
    def __init__(self, filename, mode):
        self.file = open(filename, mode)
        self.counter = 0
        self.logger = logging.getLogger('CustomFile')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        if exc_type is not None:
            self.logger.error(f'An error occurred: {exc_type}, {exc_value}, {traceback}')
        else:
            self.logger.info(f'The file {self.file.name} was closed successfully')
        return False

    def write(self, text):
        self.counter += 1
        self.file.write(text)

    def read(self):
        return self.file.read()

