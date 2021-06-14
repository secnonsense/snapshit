# snapshit
Script to snapshot a directory and then compare it  

#Make a snapshit of your directory.  Snapshit is saved in a file named snapshit.txt in the same directory  
python3 snapshit.py /mydirectory/directory  
  
#Make a snapshit with a custom name - mysnapshit.txt    
python3 snapshit.py -s mysnapshit.txt  /mydirectory/directory

#Compare the default snapshit.txt file to mydirectory  
python3 snapshit.py -c /mydirectory/directory

#Compare two snapshits  
python3 snapshit.py -c snapshit.txt mysnapshit.txt  
