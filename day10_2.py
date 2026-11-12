from file_define import TextFileReader,JsonFileReader
from data_define import Record

text_file_reader=TextFileReader("data1.txt")
json_file_reader=JsonFileReader("data2.txt")
jan_data=text_file_reader.read_data()
feb_data=json_file_reader.read_data()
all_data=jan_data+feb_data
data_dict={}
for record in all_data:
    if record.date in data_dict.keys():
        data_dict[record.date]+=record.money
    else:
        data_dict[record.date]=record.money
print(data_dict)