from proxy.txt_reader import TxtReader


class TxtProxyWriterReader:
    def __init__(self, file_path):
        self.__result = ''
        self.__is_actual = False
        self.__txt_reader = TxtReader(file_path)

    def read_file(self):
        if self.__is_actual:
            return self.__result
        else:
            self.__result = self.__txt_reader.read()
            self.__is_actual = True
            return self.__result


if __name__ == '__main__':
    proxy_reader = TxtProxyWriterReader('my_file.txt')

    print(proxy_reader.read_file())
    print('\n')
    print(proxy_reader.read_file())
