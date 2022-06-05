## 游戏引擎

ExHIBIT引擎

## 主要使用厂商

Skyfish社及其子社，Moonstone社及其子社

## 游戏文件结构

```
├──fonts
├──res
│  ├──c
│  ├──g
│  │  ├──ch
│  │  ├──ev
│  │  ├──gn
│  │  └──sy
│  └──s
│     ├──e
│     └──m
├──rld
└──userdata
```

### fonts

fonts文件夹中存放字体文件。

### rld

rld文件夹中存放格式为.rld的剧本文件。

### userdata

userdata文件夹中存放存档。

### res

res文件夹中存放游戏资源。

#### c

c文件夹下存放格式为.rnf的游戏脚本文件

#### g

g文件夹下存放格式为.gyu的游戏图片文件，分为四个文件夹。

##### ch

存放游戏立绘。

##### ev

存放游戏CG。

##### gn

存放效果图片。

##### sy

存放游戏界面所需的系统图片

#### s

s文件下存放游戏的声音文件，分为两个文件夹。

##### e

存放格式为.wav的游戏配音文件

##### m

存放格式为.ogg的游戏BGM

## 解包方法

游戏的CG以.gyu格式存放在res\g\ev文件夹中。通常ev文件夹下分为多个文件夹，通常每个文件夹为游戏的一组包含差分的CG，此外也有文件夹中保存背景图片。

### Garbro

下载地址：[morkt/GARbro: Visual Novels resource browser (github.com)](https://github.com/morkt/GARbro)

Garbro是一个非常方便的解包软件，可以直接查看.gyu文件并提取。

### Asmodean: gyu2bmp

下载地址：[asmodean's reverse engineering page - gyu2bmp](http://asmodean.reverse.net/pages/gyu2bmp.html)

Asmodean开发了大量针对性的工具，此处为用于将.gyu转换为.bmp格式的图片，使用方法如下：

1、新建一个文件夹，将上述res\g\ev文件夹拷贝到该文件夹中，并将rld文件夹中def.rld也复制到里面

2、修复CG文件的key：运行下面的bat文件。

```bash
fixipgyu.exe def.rld
```

3、提取CG：运行下面的bat文件

```bash
for /r %%i in (*.gyu) do gyu2bmp.exe %%i
```

### 后记

部分ExHIBIT引擎制作的游戏，存在一张大图配合多张小块差分CG的情况，图像大小信息存储在原始gyu的第5和第6两个字节，坐标信息保存在原始gyu文件的末尾，其中5050代表底图的文件名，384和80代表差分应该覆盖区域的左上角坐标。

![gyu](https://raw.githubusercontent.com/JamesYuuu/Picbed/main/1.png)

写了如下python代码进行处理，需要安装python和ImageMagick，并且将原gyu和bmp放在同一个文件夹下。

```python
import os
import struct

for files in os.listdir("./"):
    if os.path.isdir(files):

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

```

