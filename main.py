# -*- coding: utf-8 -*-
import CsvHandler as CsvHand
import SubmissionHandler as SubHand

f_marked = r".\marked"
f_to_mark = r".\to_mark"

valid_status_inputs = {'quit': ['-q', '-quit'],
                       'skip': ['-sk', '-skip'],
                       'help': ['-h', '-help'],
                       'status':['d', 'demo', 'fix', 'redo'],
                       'canned' : [ '1', '2', '3']}

canned_responce = [{'status': 'demo', 'comment' : 'good'},
                   {'status': 'fix', 'comment' : 'please see me in the tute or helpdesk'},
                   {'status': 'redo', 'comment' : 'please see me in the tute or helpdesk'}]

def GetCannedResponce(responce):
    stat = canned_responce[int(responce)]['status']
    comm = canned_responce[int(responce)]['comment']
    return stat, comm

def ValidateUserInput(to_check):
    for v in valid_status_inputs:
        if any(val == to_check for val in valid_status_inputs[v]):
            return True
    return False

def GetUserInput():
    valid = False
    status  = ""
    comment = ""
    while not valid:
        status = input("Enter status: ")
        valid = ValidateUserInput(status)
        if not valid:
            print("ERROR: Please enter valid input. ('-h' for help)")
            
    # insert canned responce
    if any(canned == status for canned in valid_status_inputs['canned']):
        status, comment = GetCannedResponce(status)
    else:        
        comment = input("Enter comment: ")
    return (status, comment)

def Help():
    print("*************************")
    print("-quit: quit program")
    print("-skip: move to next task")
    print("-------------------------")
    print("Valid status inputs:")
    print("\td    : discuss")
    print("\tdemo : demonstrate")
    print("\tfix  : fix and resubmit")
    print("\tredo : start again")
    print("*************************")
    input("HIT ENTER TO CONTINUE!")
    

SubHand.LoadAndSortFileData(f_to_mark)
CsvHand.LoadCSV(f_to_mark)
command = ""

while '-quit'not in command and SubHand._task_idx < len(SubHand._sorted_pdfs):
    SubHand.OpenNextSubmissionPdf()
    stu_num_and_task = SubHand.GetCurrentStudentNumAndTaskNum()
    CsvHand.PrintStudentInfo(stu_num_and_task[0], stu_num_and_task[1])
    
    status, comment = GetUserInput()
    
    if any(com == status for com in ['-quit', '-q']):
        break
    elif any(com == status for com in ['-skip', '-sk']):
        SubHand.IteratePdfIdx()    
        print("skip")
    elif any(com == status for com in ['-help', '-h']):
        Help()
    else:
        CsvHand.UpdateCsv(stu_num_and_task[0], stu_num_and_task[1], status, comment)
        SubHand.MoveMarkedPdfs(f_marked)
        CsvHand.Save(f_marked, f_to_mark)
        SubHand.IteratePdfIdx()


