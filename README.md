Installation
------------
install the python 3.6 or higher

Usage
-----
1. Download the json file from the website.
2. Put the json file with the python script.
3. Change the fmdl.py's playlist variable same as the json file.
4. Run the script by `python fmdl.py`


### Output sample

- File is ready. 
```
>>>>>>>>>> abc\004.mp3 is downloading.... 4/259 <<<<<<<<<< 

1954 [00:04, 475.40/s]                            

==========abc\004.mp3 is ready ==========
```
- File is still downloading.
```
  0%|          | 0/1652 [00:00<?, ?/s]>>>>>>>>>> =abc\005.mp3 is downloading.... 5/259 <<<<<<<<<< 

 83%|████████▎ | 1377/1652 [00:02<00:00, 592.22/s]  
```

### Note
1. It will create a new folder by the album name and save all files to the it.
2. The download status bar's bit rate is just for reference to make sure it's still downloading.
3. The file size is also a reference, not the really file size.
4. This scripts is 