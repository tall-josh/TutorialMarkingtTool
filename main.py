# -*- coding: utf-8 -*-
import CsvHandler as CsvHand
import SubmissionHandler as SubHand
import UtilityVars as Utils
import os.path

def GetCannedResponce(responce):
    stat = Utils.canned_responce[int(responce)]['status']
    comm = Utils.canned_responce[int(responce)]['comment']
    return stat, comm

def ValidateUserInput(to_check):
    for v in Utils.valid_status_inputs:
        if any(val == to_check for val in Utils.valid_status_inputs[v]):
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
    if any(canned == status for canned in Utils.valid_status_inputs['canned']):
        status, comment = GetCannedResponce(status)
    else:        
        comment = input("Enter comment: ")
    return (status, comment)

def CheckIfFileExists(pth_to_check):
    global _write_mode
    
    if os.path.isfile(pth_to_check):
        print("Default file name --> ", pth_to_check, ", already exists.")
        print("   Enter option: ")
        print("   'write (w)'            : to OVERWRITE file")
        print("   'append (a)'           : to APPEND file")
        print("   new_file_name: to create NEW file")
        user_in = input("--> ").lower()
                        
        if (any(val == user_in.lower() for val in Utils._write_modes.keys())) or any(val == user_in.lower() for val in Utils._write_modes.values()):
            if user_in == 'a' or user_in == 'append': CsvHand.SetSaveMode('append')
            
            if user_in == 'w' or user_in == 'write': 
                CsvHand.SetSaveMode('write')
                CsvHand.StartNewFile()                                                             
        else:
            #create new file given name
            Utils.SetMarkedFileName(user_in)
            while os.path.isfile(Utils.GetSavePath()):
                print("The file: " + Utils.GetSavePath() + " already exists.")
                Utils.SetMarkedFileName(input("Enter new file name: "))
            CsvHand.StartNewFile()
                
    else:
        CsvHand.StartNewFile()
                
    print("--> Marked files will be stored at location: " + (Utils.GetSavePath()))
    input("--> Press ENTER key")

        
    
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
    

SubHand.LoadAndSortFileData(Utils.f_to_mark)
CsvHand.LoadCSV(Utils.f_to_mark)
command = ""

CheckIfFileExists(Utils.f_marked + Utils._f_name_marked)

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
        SubHand.MoveMarkedPdfs(Utils.f_marked)
        CsvHand.Save()
        SubHand.IteratePdfIdx()


            