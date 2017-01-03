# grab-files-from-subfolders
Get all files from sub folders and have them copied to a target folder

## Requirements
Python 3.6

## Usage
To show the target folder and the counter of files call without any arguments
```
$python3.6 grab-files-from-subdirs.py
```

To list all files that would be copied use -l
```
$python3.6 grab-files-from-subdirs.py -l
```

To specify a different target folder use the -d argument
```
$python3.6 grab-files-from-subdirs.py -d myTargetFolder
```

To copy all the files found to the target folder use the -c argument
```
$python3.6 grab-files-from-subdirs.py -c
```

You can also combine the arguments.

## Todos:
	- print help page when called without parameters
	- check if file already exists at target dir
	- add move option so that source files are removed after copying