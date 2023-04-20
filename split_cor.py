import json
import os.path
import shutil
with open('/home/bigdata_user2/faceforensics/test.json') as f:
   test_data = json.load(f)
with open('/home/bigdata_user2/faceforensics/train.json') as g:
    train_data = json.load(g)
with open('/home/bigdata_user2/faceforensics/val.json') as h:
    val_data = json.load(h)


# with open('/home/system7-user2/Downloads/FaceForensics-master/dataset/splits/test.json') as f:
#    test_data = json.load(f)
# with open('/home/system7-user2/Downloads/FaceForensics-master/dataset/splits/train.json') as g:
#     train_data = json.load(g)
# with open('/home/system7-user2/Downloads/FaceForensics-master/dataset/splits/val.json') as h:
#     val_data = json.load(h)


test_data1 = []
train_data1 = []
val_data1 = []
# test_data2 = []
# train_data2 = []
# val_data2 = []

# for a in test_data:
#     test_data2.append(a[0])
#     test_data2.append(a[1])
# for a in train_data:
#     train_data2.append(a[0])
#     train_data2.append(a[1])
# for a in val_data:
#     val_data2.append(a[0])
#     val_data2.append(a[1])


for i in test_data:
    string1 = ""
    string1 += str(i[0])+"_"+str(i[1])
    test_data1.append(string1)
for i in train_data:
    string1 = ""
    string1 += str(i[0])+"_"+str(i[1])
    train_data1.append(string1)
for i in val_data:
    string1 = ""
    string1 += str(i[0])+"_"+str(i[1])
    val_data1.append(string1)



test_dir = []
for paths, directories, files in os.walk('/home/bigdata_user2/Storage/ankit/actual_data/Data/train'):
    for x in files:
        y = os.path.join(paths, x)
        test_dir.append(y)

i=0
for loc in test_dir:
    p = loc.split('/')[-2]
    if p in test_data1:
        b = loc.split('/')[-1]
        b = str(i)
        i+=1
        newName = os.path.join("/home/bigdata_user2/Storage/ankit/final_data/test/class1",b )
        shutil.copy(loc, newName)
    # else:
    #     if p in test_data2:
    #         b = loc.split('/')[-1]
    #         b = str(i) + b
    #         i+=1
    #         newName = os.path.join("/home/bigdata_user2/Storage/ankit/actual_split/test/class2",b )
    #         shutil.copy(loc, newName)


i=0
for loc in test_dir:
    p = loc.split('/')[-2]
    if p in train_data1:
        b = loc.split('/')[-1]
        b = str(i) 
        i+=1
        newName = os.path.join("/home/bigdata_user2/Storage/ankit/final_data/train/class1",b )
        shutil.copy(loc, newName)
    # else:
    #     if p in train_data2:
    #         b = loc.split('/')[-1]
    #         b = str(i) + b
    #         i+=1
    #         newName = os.path.join("/home/bigdata_user2/Storage/ankit/actual_split/train/class2",b )
    #         shutil.copy(loc, newName)


i=0
for loc in test_dir:
    p = loc.split('/')[-2]
    if p in val_data1:
        b = loc.split('/')[-1]
        b = str(i)
        i+=1
        newName = os.path.join("/home/bigdata_user2/Storage/ankit/final_data/val/class1",b )
        shutil.copy(loc, newName)
    # else:
    #     if p in val_data2:
    #         b = loc.split('/')[-1]
    #         b = str(i) + b
    #         i+=1
    #         newName = os.path.join("/home/bigdata_user2/Storage/ankit/actual_split/val/class2",b )
    #         shutil.copy(loc, newName)


