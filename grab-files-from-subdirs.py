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
import os

###############################################################################
### excludeList is an array containing files that should be ignored
### Todo: allow wildcards
###############################################################################
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
### Todo: check if target file already exists
###############################################################################
def copy_files_to_dir(fileList, targetFolder):
	for file in fileList:
		print("source file: " + str(file))
		length = len(file.parts)
		index = length - 1

		targetFile = Path(targetFolder)
		targetFile = targetFile / file.parts[index]
		print("target file: " + str(targetFile))
		if os.path.isfile(targetFile) == True:
			print("WARNING: target file already existing and will be ignored.")
		else:
			#print("copying")
			shutil.copy2(file, targetFolder)


###############################################################################
### move files by list to targetFolder
### Todo: check if target file already exists
###############################################################################
def move_files_to_dir(fileList, targetFolder):
	for file in fileList:
		print("source file: " + str(file))
		length = len(file.parts)
		index = length - 1

		targetFile = Path(targetFolder)
		targetFile = targetFile / file.parts[index]
		print("target file: " + str(targetFile))
		if os.path.isfile(targetFile) == True:
			print("WARNING: target file already existing and will be ignored.")
		else:
			print("TODO: moving")
			#shutil.move(file, targetFolder)



###############################################################################
### Directly Executed Script starts here
###############################################################################
print(sys.version_info);
print("Parameters:")
print("Use parameter -d <search-dir> to specify the search and target directory")
print("Use parameter -l to list the file that were found")
print("Use parameter - c to copy the files to the search/target dir. Without specifying this parameter nothing will be changed")


# parse arguments
# -d targetfolder is mapped to variable targetFolder or defaulted to the current folder
# -l to list the found files
# -c copy to targetFolder
print(sys.argv)




# search for -d argument
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


# search for -h (help)
showHelp = False
if "-h" in sys.argv:
	showHelp = True

# search for -l (list files)
listFiles = False
if "-l" in sys.argv:
	listFiles = True


# search for -c (copy files)
copyFiles = False
if "-c" in sys.argv:
	copyFiles = True

# search for -m (move files)
moveFiles = False
if "-m" in sys.argv:
	moveFiles = True

# show help if requested
if showHelp == True:
	print("-d <directory> - specifies <directory> as the search and target directory.")
	print("-l             - lists all file which are found in the search dir and its subdirs. This can be used to check what will happen when -c or -m is used.")
	print("-c             - copies all the files to the target dir.")
	print("-m             - moves all the files to the target dir.")
	sys.exit(0)


# if -m and -c is used together then abort with an error message
if copyFiles == True and moveFiles == True:
	sys.exit("ERROR: Please use only -c (copy) and -m (move).")


#get the current path (for testing we use testordner)
#targetPath = Path("./testordner")
targetPath = Path(targetFolder)

#get all the files of all subdirs
files = get_files_recursive(targetPath)
#print(files)


# print all entries if requested
if listFiles == True:
	for entry in files:
		print(entry)

print(str(len(files)) + " files found")
print("target folder for all found files: " + str(targetPath))


# if copyFiles is requested then call the copy function
if copyFiles == True:
	copy_files_to_dir(files, targetFolder)

# if moveFiles is requested call the move function
if moveFiles == True:
	move_files_to_dir(files, targetFolder)


