# -*- coding: utf-8 -*-
import os
import csv

def create_dirs(dirs):
    """
    Create dirs. (recurrent)
    :param dirs: a list directory path.
    :return: None
    """
    for path in dirs:
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=False)
    return None


def write2txt(content, file_path):
    """
    Write array to .txt file.
    :param content: array.
    :param file_path: destination file path.
    :return: None.
    """
    try:
        file_name = file_path.split('/')[-1]
        dir_path = file_path.replace(file_name, '')
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        with open(file_path, 'w+') as f:
            for item in content:
                f.write(' '.join([str(i) for i in item]) + '\n')

        print("write over!")
    except IOError:
        print("fail to open file!")

    return None


def write2csv(content, file_path):
    """
    Write array to .csv file.
    :param content: array.
    :param file_path: destination file path.
    :return: None.
    """
    try:
        temp = file_path.split('/')[-1]
        temp = file_path.replace(temp, '')
        if not os.path.exists(temp):
            os.makedirs(temp)

        with open(file_path, 'w+', newline='') as f:
            csv_writer = csv.writer(f, dialect='excel')
            for item in content:
                csv_writer.writerow(item)

        print("write over!")
    except IOError:
        print("fail to open file!")

    return None