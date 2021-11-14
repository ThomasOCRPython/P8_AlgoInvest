import csv

def read_csv(filename):
    with open(filename) as f:
        file_data=csv.reader(f)
        headers=next(file_data)
        return [dict(zip(headers,i)) for i in file_data]

# tab_action_2 = read_csv('../data/dataset2_Python+P7.csv')
# print (tab_action_2)