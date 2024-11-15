import json, csv

class Data:
    def __init__(self, data_path:str, data_types:str):
        self.data_path:str = data_path
        self.type:str = data_types
        self.data_ = self.read()
        self.column_names = self.__get_columns()
        self.counter = len(self.data_)


    def __read_json(self):
        data_:list = []

        with open(self.data_path, 'r') as file:
            data_ = json.load(file)

        return data_


    def __read_csv(self): 
        data_:list = []
        
        with open(self.data_path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                data_.append(row)

        return data_
    

    def read(self):
        data_:list = []

        if self.type == 'json':
            data_ = self.__read_json()

        elif self.type == 'csv':
            data_ = self.__read_csv()

        elif self.type == 'list':
            data_ = self.data_path
            self.data_path = 'memory list'

        return data_
       
        
    def __get_columns(self):
        return list(self.data_[-1].keys())


    def rename_columns(self, key_mapping:dict):
        new_data:list = []

        for old in self.data_:
            temp_dict:dict = {}
            for old_k, v in old.items():
                temp_dict[key_mapping[old_k]] = v
            new_data.append(temp_dict)

        self.data_ = new_data
        self.column_names = self.__get_columns()


    def join(A, B):
        combined_list:list = []
        combined_list.extend(A.data_)
        combined_list.extend(B.data_)

        return Data(combined_list, 'list')
    

    def __making_a_csv_file(self):
        combined_table:list = [self.column_names]

        for row in self.data_:
            line:list = []
            for coll in self.column_names:
                line.append(row.get(coll, 'Indisponivel'))

            combined_table.append(line)

        return combined_table
    

    def saving_data(self, path):
        combined_table = self.__making_a_csv_file()

        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(combined_table)