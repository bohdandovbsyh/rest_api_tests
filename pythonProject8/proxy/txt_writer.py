from proxy.writer import Writer


class TxtWriter(Writer):

    def __init__(self, file_path):
        self.file_path = file_path

    def write(self, new_data):
        with open(self.file_path) as file:
            text = file.write(new_data)
        return text
