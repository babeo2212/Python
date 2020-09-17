import os
from datetime import datetime
# print(os.getcwd()) # get Current Working Directory

os.chdir('C:\\Users\\PREDATOR\\Desktop') # Change Directory

# os.mkdir('New-Folder-1') # Make a new folder w/o sub-folder
# os.makedirs('New-Folder-2\\Sub-Folder') # Make a new folder with a sub-folder

# os.rmdir('New-Folder-1')
# os.removedirs('New-Folder-2\\Sub-Folder')

# os.rename('New-Folder-2', 'New-Folder-3')

# print(os.stat('Visual Studio Code.lnk'))
# mod_time = os.stat('Visual Studio Code.lnk').st_mtime # st_mtime is modification time
# print(datetime.fromtimestamp(mod_time))

# for dirpath, dirname, filename in os.walk('C:\\Users\\PREDATOR\\Desktop'): # yield 3 value tuples with a pathname, directories and file within
#     print('Current path:', dirpath)
#     print('Directories:', dirname)
#     print('Files:', filename)
#     print()

# print(os.environ.get('HOMEPATH'))
# print(os.listdir()) # list of files/folders in cwd 

# file_path = os.path.join(os.environ.get('HOMEPATH'), 'test.txt') # create a path to make a file in THAT path
# print(file_path)
# with open(file_path, 'w') as wf:
#     wf.write('My name is Mike.')

# test the path if it's exist
print(os.path.exists('d:/Hung')) # True
print(os.path.isdir('d:/Hung')) # True, it is a directory
print(os.path.isfile('d:/Hung')) # False, its not a file

print(os.path.splitext('D:/Hung/G Excel 2013/E13 Train 3/MoreToys.csv')) # -> ('D:/Hung/G Excel 2013/E13 Train 3/MoreToys', '.csv'), split path name w/o file extension
