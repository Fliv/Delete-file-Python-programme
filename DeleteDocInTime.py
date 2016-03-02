import os,datetime

BASE_DIR = "F:/1"
DELETE_DAYS = 300
#days

#list documents in dir
dir_list = os.listdir(BASE_DIR)
doc_list = []
for doc in dir_list:
	doc_path = os.path.join(BASE_DIR,doc)
	if os.path.isfile(doc_path):
		doc_list.append(doc_path)


#delete overtime files
now_time = datetime.date.today()
delta_day = datetime.timedelta(days=DELETE_DAYS)
delete_time = now_time - delta_day

all_num = len(doc_list)
delete_num = 0
rest_num = 0
for doc in doc_list:
	doc_date = datetime.date.fromtimestamp(os.path.getmtime(doc))
	#print doc, doc_date < delete_time
	if doc_date < delete_time:
		print "Delete: " + doc 
		delete_num += 1
rest_num = all_num - delete_num


print now_time
print "There are ", all_num, " files"
print "delete: ", delete_num, " files"
print "left: ", rest_num, " files"