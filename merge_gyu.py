import os
import struct
from tqdm import tqdm

if os.path.exists("def.rld"):
    os.system("fixipgyu.exe def.rld")

if os.path.exists("gyu2bmp.exe"):
    os.system("for /r %i in (*.gyu) do gyu2bmp.exe %i")

for files in tqdm(os.listdir("./")):
    if os.path.isdir(files):
        '''
        for file in os.listdir(files):
            file=os.path.join(files,file)

            ext=file.split(".")[-1]
            if ext=="gyu":
                os.system("gyu2bmp.exe "+file)
        '''
        for file in os.listdir(files):
            file=os.path.join(files,file)

            ext=file.split(".")[-1]
            file_name=file.split(".")[0]+".bmp"
            if ext=="gyu":
                with open(file,"rb") as gyu:
                    data=gyu.read()

                    x,y=struct.unpack("<2I",data[16:24])
            
                    length=len(data)
                    num=length-1

                    while data[num]==0:
                        num=num-1
                    if length-num-1<=3:
                        continue
            
                    current_num=num
                    while data[current_num]!=0:
                        current_num=current_num-1

                    if  num+1-current_num>30:
                        continue

                    location=data[current_num:num+1].decode(encoding="utf8").split(",")
            
                    base_file=os.path.join(location[0][-4:-2],location[0][-4:]+".bmp")
                    size=str(x)+"x"+str(y)+"+"+location[1]+"+"+location[2]

                    os.system("magick "+base_file+" -compose over "+file_name+" -geometry "+size+" -composite "+file_name)
        '''
        for file in os.listdir(files):
            file=os.path.join(files,file)

            ext=file.split(".")[-1]
            if ext=="gyu":
                os.remove(file)
        '''

#os.system("for /r %i in (*.gyu) do del %i")