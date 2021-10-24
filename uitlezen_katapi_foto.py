import requests
import shutil
import pathlib
import os

reqresult = requests.get('https://api.thecatapi.com/v1/images/search')
kattenfeit = reqresult.json()
kattenfeit = kattenfeit[0]
urlimage = kattenfeit["url"]
filename = urlimage.split("/")[-1]
req2 = requests.get(urlimage, stream=True)

if req2.status_code == 200:
    req2.raw.decode_content = True
    file = open(filename,"wb")
    shutil.copyfileobj(req2.raw, file)
    file.close()


pwd = pathlib.Path().resolve()
filepath = str(pwd)+"/"+filename

#os.system(f"pcmanfm --set-wallpaper={filepath}")
print(filepath)