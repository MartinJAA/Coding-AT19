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


def find_pdf(path):
    pdf_list = []
    read_files = os.listdir(path)
    for items in read_files:
        if items.endswith(".pdf"):
            pdf_list.append(items)
    print(pdf_list)


def find_folders(path):
    # folder_list = []
    read_folders = next(os.walk('data'))[1]
    return read_folders



