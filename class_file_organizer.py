import os, shutil, json

def is_accessible(path, mode='r'):
    """
    Check if the file or directory at `path` can
    be accessed by the program using `mode` open flags.
    """
    try:
        f = open(path, mode)
        f.close()
    except IOError:
        return False
    return True

# check if a file ends with an extension from param extension list
def has_extension(f, ext_list):
    for ext in ext_list:
        if f.endswith(ext):
            return True
    return False

# check if a file has a keyword from param keywords list
def has_keyword(f, keyword_list):
    for keyword in keyword_list:
        if keyword in f:
            return True
    return False

# check if file has a number
def has_number(f):
    return any(char.isdigit() for char in f)

# checks if a directory exist, and if it doesn't, it makes it
def cmake_dir(dir):
    if not os.path.isdir(dir):
        try:
            os.mkdir(dir)
        except OSError:
            print ("Creation of the directory %s failed or the directory exists already" % dir)
        else:
            print ("Successfully created the directory %s " % dir)

# load up settings.json
if is_accessible("settings.json"):
    with open("settings.json") as f:
        settings = json.load(f)
else:
    print("Failed to load settings.json")
    raise SystemExit


# loop through sources
for source in settings["sources"]:
    os.chdir(source)
    for f in os.listdir(os.getcwd()):
        for param in settings["params"]:
            # check if file has extension in param
            if has_keyword(f, param["keywords"]) and has_extension(f, param["extensions"]):    
                # check if file has number parameter and if not do the rest of the logic
                if param["has_numbers"] == True:
                    if has_number(f) == False:
                        continue
                # make destination if it doesn't exist already
                cmake_dir(param["destination"])
                # move file to destination
                shutil.move(os.getcwd()+"/"+f, param["destination"])
                break

# list for power points to be put in
# ppt_list = []
# # list for word documents to be put in
# docx_list = []
# #list for java files to be put in
# java_list = []
# #list for pdf files to be put in
# pdf_list = []
# #list for sql files to be put in
# sql_list = []

# grab files in directory that have the ppt file extension
# for file in os.listdir(os.getcwd()):
#     if file.endswith(".ppt") or file.endswith(".pptx"):
#         ppt_list.append(file)
#     elif file.endswith(".doc") or file.endswith(".docx"):
#         docx_list.append(file)
#     elif file.endswith(".java"):
#         java_list.append(file)
#     elif file.endswith(".pdf"):
#         pdf_list.append(file)
#     elif file.endswith(".sql"):
#         sql_list.append(file)

# change working directory from downloads to file transfer destination
# os.chdir("/Users/tomato/Documents/College/Spring 2019")

# assign folder directories for classes
# directories = []
# directories.append(os.getcwd()+"/OS:File Organization/") # os class
# directories.append(os.getcwd()+"/Info Sec/") # information security
# directories.append(os.getcwd()+"/Data structures/") # Data structures
# directories.append(os.getcwd()+"/Databases/") # Databases
# directories.append(os.getcwd()+"/Networking and Communications/")
# directories.append(os.getcwd()+"/Computer Security/")
# directories.append(os.getcwd()+"/Programming Languages/")



#check if directories exist
#if they don't then make the directories
# for directory in directories:
#     cmake_dir(directory)

# make directories
# cmake_dir(directories[0]+"Inclass Activities")
# cmake_dir(directories[0]+"Homework")
# cmake_dir(directories[0]+"Slides")
# cmake_dir(directories[0]+"Answers")
# cmake_dir(directories[2]+"Slides")
# cmake_dir(directories[2]+"Java files")
# cmake_dir(directories[3]+"Homework")
# cmake_dir(directories[3]+"Labs")
# cmake_dir(directories[3]+"Labs/SQL")
# cmake_dir(directories[3]+"Final")

# move power points into specified directories
# for ppt in ppt_list:
#     #os_class
#     if ("ch" in ppt) and hasNumber(ppt) and ("_" not in ppt):
#         shutil.move(downloads+ppt, directories[0]+"Slides")
#     # info_sec
#     elif ("ch" in ppt) and ("_" in ppt) and hasNumber(ppt):
#         shutil.move(downloads+ppt, directories[1])
#     elif ("Ch" in ppt) and ("_pt" in ppt):
#         shutil.move(downloads+ppt, directories[2]+"Slides")


# move word documents to specified directories
# for docx in docx_list:
    #os_class
#     if "Inclass Activity" in docx:
#         shutil.move(downloads+docx, directories[0]+"Inclass Activities")
#     if ("Assignment " in docx) and hasNumber(docx):
#         shutil.move(downloads+docx, directories[0]+"Homework")
#     if ("CSCI 3410" in docx) or ("Databases" in docx) or ("Database" in docx):
#         if ("Lab" in docx) or ("Labs" in docx):
#             shutil.move(downloads+docx, directories[3]+"Labs")
        # if ("HW" in docx) or ("Homework" in docx):
        #     shutil.move(downloads+docx, directories[3]+"Homework")

# currently the java files are just going to be dumped into data structures because that is the only class that utilizes java as of now
# for java in java_list:
#     shutil.move(downloads+java, directories[2]+"/Java files")

# pdf files are vastly used by databases and maybe some of os
# for pdf in pdf_list:
#     if ("CSCI 3410" in pdf) or ("Databases" in pdf):
#         if ("Homework" in pdf):
#             shutil.move(downloads+pdf, directories[3]+"Homework")
#         elif ("Lab" in pdf) or ("Labs" in pdf):
#             shutil.move(downloads+pdf, directories[3]+"Labs")
#         elif ("Final" in pdf):
#             shutil.move(downloads+pdf, directories[3]+"Final")
#     if ("Assignment" in pdf) and ("Answers" in pdf):
#         shutil.move(downloads+pdf, directories[0]+"Answers")
# for sql in sql_list:
#     if ("CSCI 3410" in sql) or ("Databases" in sql) or ("Lab" in sql):
#         shutil.move(downloads+sql, directories[3]+"Labs/SQL")
