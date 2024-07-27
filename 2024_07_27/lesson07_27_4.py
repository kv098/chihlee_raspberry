import os
import os.path


current_path = os.path.abspath(__name__)#取得目前檔案路徑
print(current_path)
directory_name = os.path.dirname(current_path)#取得目前資料夾路徑
print(directory_name)
data_path = os.path.join(directory_name, 'data')#目前資料夾路徑加上data目錄
print(data_path)
os.path.isdir(data_path)

if not os.path.isdir(data_path):
    print("沒有DATA的目錄，手動建立目錄")
    os.mkdir(data_path)
else:
    print("目錄已建立")


log_path = os.path.join(data_path,'iot.log')
print(log_path)
os.path.isfile(log_path)



if not os.path.isfile(log_path):
    print('沒有iot.log檔，建立新檔')
    with open(log_path,mode='w',encoding='utf-8',newline='') as file:
        file.write('時間,濕度,溫度\n')
else:
    print("已經有log檔")


with open(log_path, mode='a', encoding='utf-8', newline='') as file:
    file.write('2024-07-27 15:30:25,70.5,29.5\n')


from datetime import datetime
print(datetime.now())
now = datetime.now()
print(now.year,'-',now.month, '-', now.day, now.hour,':', now.minute,':', now.second)
print(now.strftime('%Y-%m-%d %H:%M:%S'))
now_str = now.strftime('%Y-%m-%d %H:%M:%S')

import random
humidity = str(random.randint(330,820)/10)
temp = str(random.randint(50,400)/10)

with open(log_path, mode='a', encoding='utf-8', newline='') as file:
    file.write(now_str + ','+ humidity + ',' + temp + "\n")


