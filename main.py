import re
import os
from collections import OrderedDict
from datetime import datetime



date_pattern = r"\b\d{2}/\d{2}/\d{4} \d{2}\b"
number_pattern = r"\b\d{1,3}\.\d{1,2}\b"
time_list = dict()

def validation(data):
    lines = data.splitlines(True)

    for line in lines:
        date_line = re.search(date_pattern,line)
        date_line_num = re.findall(number_pattern,line)
        
        if date_line_num:
            num = float(date_line_num[0])
            date_str = date_line.group(0)

            if date_str in time_list.keys():
                a,b = time_list[date_str]
                if isinstance(a, (int)):
                    a = a + 1
                    b = b + num
                else:
                    b = b + 1 
                    a = a + num
                time_list[date_str] = {b,a}
            else:
                time_list[date_str] = {num,1}
    

def readFile(file_path):
    chunk_size = 10240
    file = open(file_path, "r")
    print("read file")
    while True:
        data = file.read()
        if not data:
            print("empty")
            break
        validation(data) 
        break
    

def printfile():
    for key,value in time_list.items():
        if key == "17/06/2025 06":
            print(f"start time: {key}:00:00, average: {value}")

        a,b = value
        if isinstance(a, (int)):
            ave = b / a
        else:
            ave = a / b

        print(f"start time: {key}:00:00, average: {ave}")



def main():
    file_path = r"C:\Users\User\Desktop\first question\targilB\time_series.txt"
    if os.path.exists(file_path):
        print("File found!")
    else:
        print("File not found. Please check the path.")
        return
    
    readFile(file_path)
    printfile()


if __name__ == "__main__":
    main()
