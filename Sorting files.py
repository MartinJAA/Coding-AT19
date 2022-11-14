import shutil
import pandas as pd
import os
from distutils.dir_util import copy_tree

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
    return pdf_list


def find_folders(path):
    folders_list = next(os.walk('data'))[1]
    return folders_list


def copy_pdf(pdf_list):
    for items in pdf_list:
        shutil.copy2(f'data/{items}', 'Tutorials')
    return print("Pdf copied")


def copy_folders(folders_list):
    for items in folders_list:
        os.mkdir(f'Games/{items}')
        copy_tree(f'data/{items}', f'Games/{items}')
    return print("Folders copied")


create_folder(csv_to_list('Name'))
copy_pdf(find_pdf('data'))
copy_folders(find_folders('data'))