# Problem 2 - Finding files

First step is to check if the file path is valied. If it is, then 2 lists are used to save information regarding 1) directories  and 2)value of files including path. The while loop removed the first element of directories and gets all items in this folder. Next, it check if the item is a directory- if it is, it adds to the directories list, if it isn't it checks for the file with extension by suffix passed.

    
```
Time Complexity: O(n)
Space Complexity: O(n)
```


