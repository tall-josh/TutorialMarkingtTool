
f_marked = r".\marked"
f_to_mark = r".\to_mark"
_f_name_to_mark = r"\marks.csv"
_f_name_marked = r"\marks.csv"

_csv_header = ['Username',
               'Name',
               'Tutorial',
               'Task',
               "Student's Last Comment",
               'Your Last Comment',
               'Status',
               'New Grade',
               'New Quality',
               'Max Quality',
               'New Comment']

def GetSavePath():
    return f_marked + _f_name_marked
    

def GetToMarkPath():
    return f_to_mark + _f_name_to_mark

def SetMarkedFileName(newName):
    global _f_name_marked
    _f_name_marked = "\\" + newName + ".csv"

valid_status_inputs = {'quit': ['-q', '-quit'],
                       'skip': ['-sk', '-skip'],
                       'help': ['-h', '-help'],
                       'status':['d', 'demo', 'fix', 'redo'],
                       'canned' : [ '1', '2', '3']}

canned_responce = [{'status': 'demo', 'comment' : 'good'},
                   {'status': 'fix', 'comment' : 'please see me in the tute or helpdesk'},
                   {'status': 'redo', 'comment' : 'please see me in the tute or helpdesk'}]

TASK_GRADES = ['P', 'C', 'D', 'H']


_write_modes = {'append' : 'a', 
                'write'  : 'w'}

