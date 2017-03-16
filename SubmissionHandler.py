import os
import subprocess
import shutil

TASK_GRADES = ['P', 'C', 'D', 'H']
_sorted_pdfs = []
_task_idx    = 0

_TASK_NUM    = 0
_PDF_NAME    = 1
_PATH        = 2
current_task = []

def __WalkToMarkDir(root_path):
    file_arr = []
    for (path, loc, names) in os.walk(root_path):
        for n in names:
            file_arr.append((__GetTaskNum(n), n, path))            
    return file_arr
        
def __GetTaskNum(file_name):
    file_name = file_name.replace("_", ".")
    num_str = ""
    num = -1
    for e in file_name:
        if any(e==g for g in TASK_GRADES):
            break
        num_str += e
    try:
        num = float(num_str)
    except:
        num = -1
    return num

def __SortByTaskNumber(task_list):
   task_list.sort(key=lambda x:x[0]) 
   #remove csv headers
   task_list = [x for x in task_list if x[0] >= 0]
   return task_list

def GetCurrentStudentNumAndTaskNum():
    global _task_idx
    #extract student number from path
    temp = _sorted_pdfs[_task_idx][_PATH].split("\\")
    stu_num = temp[len(temp)-1]
    return (stu_num, str(_sorted_pdfs[_task_idx][_TASK_NUM]))

def LoadAndSortFileData(path_to_walk):
    global _sorted_pdfs
    _sorted_pdfs = __SortByTaskNumber(__WalkToMarkDir(path_to_walk))
    
def OpenNextSubmissionPdf():
    global _task_idx
    pdf_path = _sorted_pdfs[_task_idx][_PATH]+"\\"+_sorted_pdfs[_task_idx][_PDF_NAME]
    subprocess.Popen(pdf_path,shell=True)

def IteratePdfIdx():
    global _task_idx
    _task_idx += 1
    
def MoveMarkedPdfs(new_path):    
    pdf_path = _sorted_pdfs[_task_idx][_PATH]+"\\"+_sorted_pdfs[_task_idx][_PDF_NAME]
    new_path += "\\"+_sorted_pdfs[_task_idx][_PDF_NAME]
    shutil.move(pdf_path, new_path)

