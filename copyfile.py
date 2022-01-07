import shutil
import os
import string
import random

def random_char():
    result=""
    base_string = string.ascii_letters
    for i in range(0, 5):
        result += base_string[random.randint(0, 26)]
    return result
def split_file(name):
    index = name.index(".")
    return name[0:index], name[index+1:len(name)]
flist = os.listdir(r"C:\Users\Boss Shiimiing\Desktop\Howls'\[Kiera] Template")
for folder in flist:
    path = r"C:\Users\Boss Shiimiing\Desktop\Howls'\[Kiera] Template\{}".format(folder)
    if os.path.isdir(path):
        files = os.listdir(path)
        for file in files:
            filename = r"C:\Users\Boss Shiimiing\Desktop\Howls'\[Kiera] Template\{}\{}".format(folder, file)
            splited = split_file(file)
            new_name = splited[0]+random_char()+"."+splited[1]
            filedes = r"C:\Users\Boss Shiimiing\Desktop\Howls'\[Kiera] Template\{}".format(new_name)
            try:
                shutil.move(filename, filedes)
            except:
                pass
            print("Done{}".format(file))