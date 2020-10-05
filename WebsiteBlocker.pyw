from datetime import datetime as dt
import time
host_temp = "hosts"
host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list=["www.astroyogi.com","astroyogi.com"]
print(website_list)
while True:
    print("Working")
    with open(host_path,'r+') as file:
        content=file.read()
        for website in website_list:
            if website in content:
                pass
            else:
                file.write(redirect+" "+website+"\n")
    time.sleep(6)
    
    
    
    
'''    else:
    
       print("Working else part")
       time.sleep(5)
       with open(host_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                        file.write(line)
                file.truncate()
'''