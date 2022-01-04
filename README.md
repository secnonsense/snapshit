# snapshit
Script to snapshot a directory and then compare it  

Snapshit makes a snapshot of the specified directory by creating an output file (called snapshit.txt by default) which is a list of filenames and hashes of the files. Ideally don't run snapshit from within the target directory or the snapshit file will impact the results. After creating an initial snapshit, the snapshit file can be compared to another snapshit file (using -c) , or a directory (by specifying the path). If a path is specified, the -c option generates a 2nd snapshit named cshit.txt in the current directoy. Always run snapshit from the same location so it can find the previous snapshit.txt file and to keep the paths for the files in the snapshit file consistent.  Differing paths will cause matches to fail. The compare function will find files missing in the destination or files that have been changed.  However it will not find files that have been added in the destination.  This can be accomplished by running an additional snapshit comparison reversing the source and destination as follows:  

**Compare destination to source (instead of the default source to destination):**  
python3 snapshit.py -c cshit.txt snapshit.txt  

Other Examples:  

**Make a snapshit of your directory.  Snapshit is saved in a file named snapshit.txt in the same directory:**  
python3 snapshit.py /mydirectory/directory  
  
**Make a snapshit with a custom name - mysnapshit.txt:**    
python3 snapshit.py -s mysnapshit.txt  /mydirectory/directory

**Compare the default snapshit.txt file to mydirectory:**  
python3 snapshit.py -c /mydirectory/directory

**Compare two snapshits:**  
python3 snapshit.py -c snapshit.txt mysnapshit.txt  
