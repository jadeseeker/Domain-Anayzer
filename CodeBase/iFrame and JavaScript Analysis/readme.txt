=================== File List ======================
main.py
scoreItem.py

=================== How To Run =====================

1) run BlackThread to crawl URLs and get frame.db and Script.db as results
use the following commands:

scrapy crawl getScript -a filename=Lists/small_list_Malicious.txt -a db_name=script.db
scrapy crawl getFrames -a filename=Lists/small_list_Malicious.txt -a db_name=frames.db

2) type ‘python main.py’ in the CMD
 
3) system will return a percentage value of malicious website
(For a single URL input, 0% means benign and 100% means malicious




