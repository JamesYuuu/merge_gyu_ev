# merge_gyu_ev

## 简介

部分ExHIBIT引擎制作的游戏，存在一张大图配合多张小块差分CG的情况。

图像大小信息存储在原始gyu的第5和第6两个字节。

坐标信息保存在原始gyu文件的末尾，其中5050代表底图的文件名，384和80代表差分应该覆盖区域的左上角坐标。

![gyu](https://raw.githubusercontent.com/JamesYuuu/Picbed/main/1.png)

## 用法

需要安装python和 ImageMagick。

将仓库中的gyu2bmp.exe，fixipgyu.exe，merge_gyu.py以及游戏目录 /rld/def.rld 放到游戏目录/res/g/ev文件夹下。

```markdown
usage: python merge_gyu.py [-d] [-g] [-m] [-del]
-d: 获取gyu文件密钥,如果不添加这个参数可以正常解包则不用添加
-g: 把gyu文件转化为bmp, 如果已经使用Garbro等办法自行提取，请把bmp和原gyu文件放在一个文件夹中
-m: 根据gyu中的坐标合成差分CG
-del: 转换完成后删除原gyu文件
```





