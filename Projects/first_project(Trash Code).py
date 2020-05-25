import os,shutil
audio_ext = ("mp3","WAV","PCM","m4a","Music")
doc_ext = ("pdf","txt","doc","Documents")
img_ext = ("jpg","png","gif","jpeg","Pictures")
vid_ext = ("mp4","MKV","m4a","m4v","f4v","f4a","m4b","m4r","f4b","mov","wmv","3gp","WEBM","flv","avi","hdv","Videos")
compressed_ext = ("7z","arj","deb","rar","rpm","z","zip","apk","tar","BZ2","TZ","Zipx","CAB","TAZ","GZ","Compressed Files")
disc_ext = ("iso","bin","dmg","toast","Disc Files")
data_ext = ("csv","dat","db","dbf","mbd","sav","sql","xml","json","Data Files")
email_ext = ("email","eml","emlx","msg","oft","ost","pst","vcf","Emails")
programming_ext = ("py","js","java","html","htm","css","php","c","cpp","cs","pl","swift","Programming Files")
software_ext = ("exe","Software Files")
torrent_ext = ("torrent","btapp","btkey","btsearch","btskin","loaded","magnet","utpart","zed","!ut","Torrent Files")
combo_ext = []
combo_file_name = []
aud_file_path = list()
aud_file_ext = list()
doc_file_path = list()
doc_file_ext = list()
img_file_path = list()
img_file_ext = list()
rm_dir = list()




# print(os.getcwd())
os.chdir("C:\First Demo Project")
# print(os.getcwd())
# print(os.listdir(os.getcwd()))

for c_path,c_folder,c_file in os.walk(os.getcwd()):
    # print(f"current path : {c_path}")
    # print(f"current folder : {c_folder}")
    # print(f"current file : {c_file} , and Path is {c_path}")
    rm_dir.append(c_path)
    for fn in c_file:
        name,ext = fn.split(".")
        # print(fn)
        combo_ext.append(ext)
        combo_file_name.append(fn)

del rm_dir[0]
print(rm_dir)

# print(f"{os.getcwd()}\Music")


# print(set(combo_ext)) # {'png', 'pdf', 'mp3', 'txt', 'jpg'}
# print(combo_file_name) # ['Cat1.jpg', 'file4.txt', 'file5.txt', 'Heading Home.mp3', 'Problem1.jpg',
# '1917 Theme Track.mp3', 'Problem2.png', 'Problem3.jpg', 'Python For Data  Analysis (II-E).pdf', 
# 'Version Control System With GIT.pdf', 'Cat2.jpg', 'Cat3.png', 'Deep Learning with Python.pdf', 'file2.txt', 
# 'file3.txt', 'Imagine Dragons  Bad Liar .mp3']

# # # directory for music files
# music_dir_path = f"{os.getcwd()}\Music"
# for a in set(combo_ext):
#     if a in audio_ext:
#         os.mkdir(music_dir_path)
#         break # helps in avoiding multiple checking of extentions


# doc_dir_path = f"{os.getcwd()}\Documents"
# for b in set(combo_ext):
#     if b in doc_ext:
#         os.mkdir(doc_dir_path)
#         break


# img_dir_path = f"{os.getcwd()}\Pictures"
# for c in set(combo_ext):
#     if c in img_ext:
#         os.mkdir(img_dir_path)
#         break


# for a in c_file:
#     print(a)


# # # consider this a filter , that filters mp3 files 
# for c_path,c_folder,c_file in os.walk(os.getcwd()):
#     for fn in c_file:
#         name,ext = fn.split(".")
#         if ext in audio_ext:
#             aud_file_path.append(c_path)
#             aud_file_ext.append(fn)
#         if ext in doc_ext:
#             doc_file_path.append(c_path)
#             doc_file_ext.append(fn)
#         if ext in img_ext:
#             img_file_path.append(c_path)
#             img_file_ext.append(fn)
#             # print(ext)
#             # print(f"{c_path}\{fn}")
#             # os.chdir(c_path)
#             # print(os.getcwd())
#             #  shutil.move(f"{c_path}\{fn}","C:\First Demo Project\Music")
#             # break
#             # print(f"{c_path}\{fn}")
# print(aud_file_path)
# print(aud_file_ext)
# print(doc_file_path)
# print(doc_file_ext)
# print(img_file_path)
# print(img_file_ext)



# for a in zip(aud_file_path,aud_file_ext):
# #     # print(list(a))
# #      # print(f"{a[0]}\{a[1]}")
#     shutil.move(f"{a[0]}\{a[1]}",music_dir_path)


# for b in zip(doc_file_path,doc_file_ext):
#     shutil.move(f"{b[0]}\{b[1]}",doc_dir_path)

# for c in zip(img_file_path,img_file_ext):
#     shutil.move(f"{c[0]}\{c[1]}",img_dir_path)


for a in rm_dir[::-1]:
    shutil.rmtree(a)