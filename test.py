import os

path = "/home/tarena/音乐/"
files = os.listdir(path)
print(files)
for i in files:
    name_list_negtive = i[::-1].split(".", 1)
    name_list = [item[::-1] for item in name_list_negtive]
    file_format = name_list[0]
    if name_list[1][-1] == ")" and name_list[1][-3] == "(":
        file_name = name_list[1][:-4]
    else:
        file_name = name_list[1]
    name_result = file_name + "." + file_format
    print(name_result)
    os.rename(path + i, path + name_result)
