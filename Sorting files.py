import pandas as pd
import os

def csv_to_list(column_name):
    csv_reader = pd.read_csv('students.csv')
    column = list(csv_reader[column_name])
    return column


def create_folder(list_name):
    for items in list_name:
        os.mkdir(items)
    return print("Folders created")


