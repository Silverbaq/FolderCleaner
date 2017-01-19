#!/bin/python
import os

min_size = 10
folders = {}

def folder_size(path):
    total = 0
    for entry in os.scandir(path):
        if entry.is_file():
            total += entry.stat().st_size
        elif entry.is_dir():
            total += folder_size(entry.path)
    return total  # in bytes


def scan_folder(path='.'):
    for entry in os.scandir(path):
        if entry.is_dir():
            size = folder_size(entry.path) / (1024 * 1024)  # in megabytes
            if size < min_size:
                folders[entry.path] = entry.name
                print('{} : {} Mb'.format(entry.path, round(size, 2)))


def move_folders(path='.'):
    folder_path = path+'/clean_up_folder'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    [os.rename(key, folder_path+'/'+value) for key, value in folders.items()]


if __name__ == "__main__":
    path = '.'
    scan_folder(path)
    move_folders(path)
