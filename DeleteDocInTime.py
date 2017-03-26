import datetime
import os

BASE_DIR = "D:\downloads"
DELETE_DAYS = 270
# days

# list documents in dir
dir_list = os.listdir(BASE_DIR)
doc_list = []
delete_list = []
for doc in dir_list:
    doc_path = os.path.join(BASE_DIR, doc)
    if os.path.isfile(doc_path):
        doc_list.append(doc_path)

# delete overtime files
now_time = datetime.date.today()
delta_day = datetime.timedelta(days=DELETE_DAYS)
delete_time = now_time - delta_day

all_num = len(doc_list)
delete_num = 0

for doc in doc_list:
    doc_date = datetime.date.fromtimestamp(os.path.getmtime(doc))
    # print doc, doc_date < delete_time
    if doc_date < delete_time:
        delete_list.append(doc)
        print "Delete: " + doc.decode("gbk")
        delete_num += 1
print delete_num, "files to be delete"

delete_num = 0
answer = raw_input("Delete all these files?")
if answer.upper() == "Y" or answer == "YES":
    for doc in delete_list:
        try:
            os.remove(doc)
            print "Deleted: " + doc.decode("gbk")
            delete_num += 1
        except:
            pass

print now_time
print "There are ", all_num, " files"
print "Deleted: ", delete_num, " files"
print "Left: ", all_num-delete_num, " files"
