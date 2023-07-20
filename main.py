import pymysql
import config
import my_osu_file_check

conf = config.config("config.ini")

if conf.default:
    print("\n\nNot found config.ini")
    print("making config.ini ...\n\n")

if not conf.checkConfig():
    print("\n\nconfig ERROR remove config.ini\n\n")

host = conf.config["db"]["host"]
user = conf.config["db"]["username"]
password = conf.config["db"]["password"]
db = conf.config["db"]["database"]

db = pymysql.connect(host=host, user=user, password=password, db=db, charset="utf8")
cur = db.cursor()

cur.execute("SELECT DISTINCT beatmapset_id FROM beatmaps WHERE rankedby = 1000")
result = cur.fetchall()

f = open('C:/Users/skchqhdpdy/Downloads/a/dl.bat', 'w')
f.write(f'@echo off\n')

num = 0
for i in result:
    if str(i[0]) == my_osu_file_check.search(str(i[0])):
        # 파일에 텍스트 쓰기
        f.write(f'start osu://s/{i[0]}\n')
        num += 1
    print(i[0])

f.write('pause')
# 파일 닫기
f.close()

print(f"\nlen(result) = {len(result)} --> {num} (filterd)\n")