import json

from data_define import Record
class FileReader:
    def read_data(self):
        pass

class TextFileReader(FileReader):
    def __init__(self, path):
        self.path = path
    def read_data(self):
        f=open(self.path,'r',encoding="utf-8")
        record_list = []
        for line in f.readlines():
            line=line.strip()
            data_list=line.split(",")
            record=Record(data_list[0],data_list[1],int(data_list[2]),data_list[3])
            record_list.append(record)
        f.close()
        return record_list

class JsonFileReader(FileReader):
    def __init__(self, path):
        self.path = path
    def read_data(self):
        f = open(self.path, 'r', encoding="utf-8")
        record_list = []
        for line in f.readlines():
            data_dict=json.loads(line)
            record=Record(data_dict["date"],data_dict["order_id"],int(data_dict["money"]),data_dict["province"])
            record_list.append(record)
        f.close()
        return record_list

if __name__ == '__main__':
    textFileReader=TextFileReader("data1.txt")
    for line in textFileReader.read_data():
        print(line)
    json_file_reader=JsonFileReader("data2.txt")
    for line in json_file_reader.read_data():
        print(line)