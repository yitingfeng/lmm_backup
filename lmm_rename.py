import os
from os.path import exists

f = open("lmm_audio.xml", "r")
fw = open("out.txt", "w")
myline = f.readline()
while myline:
    loc = myline.find(".mp3")
    if loc != -1 and myline.find("[重发]") == -1:
        start = myline.rfind("/", 0, loc) + 1
        cur_name = myline[start:loc] + '.mp3'


        cdata_start = myline.find("CDATA[") + 7
        cdata_end = myline.find("]", cdata_start) - 1
        new_name = myline[cdata_start:cdata_end] + '.mp3'
        new_name = new_name.replace("/", "|")

        if exists(cur_name):
            os.rename(cur_name, new_name)
            print("Success: ", cur_name, " renamed to " + new_name)

    myline = f.readline()