#! python3

# Run this script from the target folder or specify the target directory.
# to execute use:
# python3 grab-files-from-subdirs.py
#
#
# This script was developed for python 3.6
#


import sys
from pathlib import Path
import shutil

excludeList = [".DS_Store"]

###############################################################################
### Function is_excluded
###############################################################################
def is_excluded(file, excludeList):
	isExcluded = False
	for excludedFile in excludeList:
		excludedFileString = str(excludedFile)
		fileString = str(file)
		if fileString.endswith(excludedFileString):
			isExcluded = True

	return isExcluded


###############################################################################
### Function get_files_recursive
### this function returns a list that contains all files of the given directory and all its subdirectories
###############################################################################
def get_files_recursive(p):
	list = []
	for x in p.iterdir():
		if x.is_dir():
			#print(x)
			list2 = get_files_recursive(x)
			list.extend(list2)
		else:
			#print(x)
			currFilename = str(x)
			if is_excluded(x, excludeList) == False:
				list.append(x)

	return list


###############################################################################
### copy files by list to targetFolder
###############################################################################
def copy_files_to_dir(fileList, targetFolder):
	for file in fileList:
		print("file: " + str(file))
		shutil.copy2(file, targetFolder)




###############################################################################
### Directly Executed Script starts here
###############################################################################
print(sys.version_info);
print("Hello World")

# parse arguments
# -d targetfolder is mapped to variable targetFolder or defaulted to the current folder
# -l to list the found files
# -c copy to targetFolder
print(sys.argv)




# search for -d
targetFolder = ""

if "-d" in sys.argv:
	print("-d argument found")
	dIndex = 0
	targetFolderIndex = 0
	for index, arg in enumerate(sys.argv):
		print("arg: " + arg)
		print("index: " + str(index))
		if arg == "-d":
			dIndex = index
			print("dIndex: " + str(dIndex))

	if dIndex != 0:
		targetFolderIndex = dIndex + 1

	if dIndex != 0 and targetFolder != 0:
		targetFolder = sys.argv[targetFolderIndex]
	
# fallback for targetFolder is . (which is the current folder)
if targetFolder == "":
	targetFolder = "."

print("targetFolder: " + targetFolder)


# search for -l (list files)
listFiles = False
if "-l" in sys.argv:
	listFiles = True


# search for -c (copy files)
copyFiles = False
if "-c" in sys.argv:
	copyFiles = True


#get the current path (for testing we use testordner)
#targetPath = Path("./testordner")
targetPath = Path(targetFolder)

#get all the files of all subdirs
files = get_files_recursive(targetPath)
#print(files)


# print all entries
if listFiles == True:
	for entry in files:
		print(entry)

print(str(len(files)) + " files found")
print("target folder for all found files: " + str(targetPath))


if copyFiles == True:
	copy_files_to_dir(files, targetFolder)




