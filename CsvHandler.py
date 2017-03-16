# -*- coding: utf-8 -*-
import csv

_csv_data_in = []
_csv_data_out = []
_original_length = 0

_STUDENT_NUM     = 0
_STUDENT_NAME    = 1
_TUTORIAL        = 2
_TASK_NUM        = 3 
_STUDENT_COMMENT = 4
_TUTOR_COMMENT   = 5
_STATUS          = 6
_NEW_GRADE       = 7
_NEW_QUALITY     = 8
_MAX_QUALITY     = 9
_NEW_COMMENT     = 10
                                     
def LoadCSV(path_csv):
    global _csv_data_in
    global _csv_data_out
    global _original_length
    with open(path_csv+"\\marks.csv", 'r') as file:
        # load data into in_array
        reader = csv.reader(file)
        _csv_data_in = list(reader)
        _original_length = len(_csv_data_in)-1
        # add csv headers to out_array
        _csv_data_out.append(_csv_data_in[0])

def _FindDesiredRowidx(stu_num, task_num):
    global _csv_data_in
    idx = 0
    for ele in _csv_data_in:
        if (ele[_STUDENT_NUM] == stu_num) and (task_num in ele[_TASK_NUM]):
            return idx
        idx += 1        

def PrintStudentInfo(stu_num, task_num):
    global _original_length
    idx = _FindDesiredRowidx(stu_num, task_num)
    row = _csv_data_in[idx]
    print("*************************************")
    print("Student#     : {0}".format(row[_STUDENT_NUM]))
    print("Student      : {0}".format(row[_STUDENT_NAME]))
    print("Task         : {0}".format(row[_TASK_NUM]))
    print("Their Comment: {0}".format(row[_STUDENT_COMMENT]))
    print("Your Comment : {0}".format(row[_TUTOR_COMMENT]))
    print("Status       : {0}".format(row[_STATUS]))
    print("**************  {0} of {1}  **************".format(len(_csv_data_out), _original_length))
    
def UpdateCsv(stu_num, task_num, new_status, new_comment):
    global _csv_data_in
    global _csv_data_out
    
    # find desired row to update
    idx = _FindDesiredRowidx(stu_num, task_num)
    temp_row = _csv_data_in[idx]
    # update row
    temp_row[_STATUS] = new_status
    temp_row[_NEW_COMMENT] = new_comment
    #add to csv_data_out
    _csv_data_out.append(temp_row)
    #remove from _csv_data_in
    del _csv_data_in[idx]

def Save(path_marked, path_to_mark):
    path_marked += "\\marks.csv"
    path_to_mark += "\\marks.csv"
    with open(path_marked, 'w', newline="\n") as csvFile:
        csvWriter = csv.writer(csvFile, delimiter=",")
        for row in _csv_data_out:
            csvWriter.writerow(row)
            
    with open(path_to_mark, 'w', newline="\n") as csvFile:
        csvWriter = csv.writer(csvFile, delimiter=",")
        for row in _csv_data_in:
            csvWriter.writerow(row)

def PrintCsvIn():
    for ele in _csv_data_in:
        print(ele)
        
def PrintCsvOut():
    for ele in _csv_data_out:
        print(ele)