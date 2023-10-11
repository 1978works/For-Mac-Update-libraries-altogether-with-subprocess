import subprocess
import sys

######################################
# def functions
######################################
# f1: Get OS info
def judge_os():
    if sys.platform == 'darwin':
        os_name = 'mac'
    elif sys.plattform == 'win32' or 'cygwin':
        os_name = 'windows'
    elif sys.plattform == 'linux':
        os_name = 'linux'
        
    return os_name

# f2: Make a Popen object by subprocess
def make_popen_obj():
    if os_name != 'windows':
        popen_obj = subprocess.Popen(["pip", "list", "-o"], text=True, stdout=subprocess.PIPE).communicate(input=None, timeout=30)
        popen_obj = popen_obj[0].split(" ")
        # remove the last element of popen_obj, 'wheel\n'
        del popen_obj[len(popen_obj)-1] 
        return popen_obj
        
    else:
        pass


# f3: Make a list of library names to be updated
def make_library_name_list():
        name_list = []
        
        for i in names:
            if i!= "":
                name_list.append(i)
        name_list = name_list[6:len(name_list)]
        # '-----\nasttokens' ==>> 'asttokens'
        name_list[0] = name_list[0].split('\n')[1]
    
        return name_list


# f4: remove "\n"　from the above f3
def modify_name_list():
    for i in range(0, len(name_list)-1):
        if i%3 == 0 and '\n' in name_list[i]:
            name_list[i] = name_list[i].split('\n')[1]
            
    return name_list


# test
# subprocess.Popen(["pip", "install", "-U", update_list[0]], text=True, stdout=subprocess.PIPE)

# update libraries
def update_lib():
    i = 0
    while i <len(update_list):
        if i%3 == 0:
            update_name = update_list[i]
            subprocess.Popen(["pip", "install", "-U", update_name], text=True, stdout=subprocess.PIPE)
        i += 1
    else:
        print('Done')
            
######################################
# execute funcitons
######################################
os_name = judge_os()
names =make_popen_obj()

#print(names)

if names != []:
    name_list = make_library_name_list()
    update_list = modify_name_list()
    #print(update_list)
    update_lib()     
else:
    print('No libraries to be updated')
