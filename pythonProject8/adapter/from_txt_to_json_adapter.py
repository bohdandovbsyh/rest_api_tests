class FromTxtToJsonAdapter:
    def __init__(self, file_path):
        self.__file_path = file_path

    def from_txt_to_json(self):
        with open(self.__file_path, 'r') as file:
            lines = file.readlines()
        headers = lines[0].replace('\n', '').split(',')

        data = [item.replace('\n', '').split(',') for item in lines[1:]]
        result = []
        for user_data in data:
            result.append(dict(zip(headers, user_data)))
        return result


if __name__ == '__main__':
    json = FromTxtToJsonAdapter('users.txt').from_txt_to_json()
    print(json)
