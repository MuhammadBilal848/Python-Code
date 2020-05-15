import os,shutil
audio_ext = ("mp3","wav","pcm","m4a","Music")
doc_ext = ("pdf","txt","doc","Documents")
img_ext = ("jpg","png","gif","jpeg","Pictures")
vid_ext = ("mp4","mkv","m4v","f4v","f4a","m4b","m4r","f4b","mov","wmv","3gp","webm","flv","avi","hdv","Videos")
compressed_ext = ("7z","arj","deb","rar","rpm","z","zip","apk","tar","bz2","tz","zipx","cab","taz","gz","Compressed Files")
disc_ext = ("iso","bin","dmg","toast","Disc Files")
data_ext = ("csv","json","dat","db","dbf","mbd","sav","sql","xml","Data Files")
email_ext = ("email","eml","emlx","msg","oft","ost","pst","vcf","Emails")
programming_ext = ("py","js","java","html","htm","css","php","c","cpp","cs","pl","swift","Programming Files")
software_ext = ("exe","Software Files")
torrent_ext = ("torrent","btapp","btkey","btsearch","btskin","loaded","magnet","utpart","zed","!ut","Torrent Files")
bundle_ext = (audio_ext,doc_ext,img_ext,vid_ext,compressed_ext,disc_ext,data_ext,email_ext,programming_ext,software_ext,torrent_ext)
combo_ext = list()
combo_file_name = []
aud_file_path = list()
aud_file_ext = list()
doc_file_path = list()
doc_file_ext = list()
img_file_path = list()
img_file_ext = list()
vid_file_path = list()
vid_file_ext = list()
compressed_file_path = list()
compressed_file_ext = list()
disc_file_path = list()
disc_file_ext = list()
data_file_path = list()
data_file_ext = list()
email_file_path = list()
email_file_ext = list()
programming_file_path = list()
programming_file_ext = list()
software_file_path = list()
software_file_ext = list()
torrent_file_path = list()
torrent_file_ext = list()
rm_dir = list()


# print(os.getcwd())
path = input("Enter directory path: ")
os.chdir(path)
# print(os.getcwd())
# print(os.listdir(os.getcwd()))

# for c_path,c_folder,c_file in os.walk(os.getcwd()):
#     # print(f"current path : {c_path}")
#     # print(f"current folder : {c_folder}")
#     # print(f"current file : {c_file} , and Path is {c_path}")
#     rm_dir.append(c_path)
#     for fn in c_file:
#         name,ext = fn.split(".")
#         # print(fn)
#         combo_ext.append(ext)
#         combo_file_name.append(fn)

# del rm_dir[0]

# print(combo_ext)
# print(combo_file_name)
# print(rm_dir)

# ['mp3', 'jpg', 'txt', 'txt', 'exe', 'jpg', 'torrent', 'py', 'torrent', 'mp3', 'mp3', 'mkv', 'png', 'jpg', 'pdf', 'pdf', 'exe', 'exe', 'py', 'jpg', 'png', 'py', 'mkv', 'pdf', 'txt', 'txt', 'mp3', 'csv', 'json']
# ['1917 Theme Track.mp3', 'Cat1.jpg', 'file4.txt', 'file5.txt', 'Git 223064(bit).exe', 'Problem1.jpg', 'realtime apps with reactjs golang rethinkdb FreeTutorials Us zip .torrent', 'built_in_functions.py', 'FreeCourseSite com-Udemy - Django Core A Reference Guide to Core Django Concepts (1).torrent', 'Imagine Dragons - Bad Liar .mp3', 'NoreAzal.mp3', 'Oggy and the cockroaches .mkv', 'Problem2.png', 'Problem3.jpg', 'Python For Data  Analysis (II-E).pdf', 'Version Control System With GIT.pdf', 'idman633build2.exe', 'uTorrent 313.exe', 'Built_in_strmethods.py', 'Cat2.jpg', 'Cat3.png', 'closures_func.py', 'Courage the cowardly dog .mkv', 'Deep Learning with Python.pdf', 'file2.txt', 'file3.txt', 'Heading Home.mp3', 'four.csv', 'j_one.json']
# ['C:\\Test Case for Project\\new folder', 'C:\\Test Case for Project\\new folder\\New data', 'C:\\Test Case for Project\\new folder\\New folder', 'C:\\Test Case for Project\\new folder\\New folder\\Special Files']




# print(f"{os.getcwd()}\Music")


# print(set(combo_ext)) 
# print(combo_file_name) 

# C:\Test Case for Project

# print(f"{os.getcwd()}\{audio_ext[-1]}")

# bundle_ext = (audio_ext,doc_ext,img_ext,vid_ext,compressed_ext,disc_ext,data_ext,email_ext,programming_ext,
# software_ext,torrent_ext)


for c_path,c_folder,c_file in os.walk(os.getcwd()):
    rm_dir.append(c_path)
    for fn in c_file:
        name,ext = fn.split(".")
        combo_ext.append(ext)
        combo_file_name.append(fn)
        if ext in audio_ext:
            aud_file_path.append(c_path)
            aud_file_ext.append(fn)
        if ext in doc_ext:
            doc_file_path.append(c_path)
            doc_file_ext.append(fn)
        if ext in img_ext:
            img_file_path.append(c_path)
            img_file_ext.append(fn)
        if ext in vid_ext:
            vid_file_path.append(c_path)
            vid_file_ext.append(fn)
        if ext in compressed_ext:
            compressed_file_path.append(c_path)
            compressed_file_ext.append(fn)
        if ext in disc_ext:
            disc_file_path.append(c_path)
            disc_file_ext.append(fn)
        if ext in data_ext:
            data_file_path.append(c_path)
            data_file_ext.append(fn)
        if ext in email_ext:
            email_file_path.append(c_path)
            email_file_ext.append(fn)
        if ext in programming_ext:
            programming_file_path.append(c_path)
            programming_file_ext.append(fn)
        if ext in software_ext:
            software_file_path.append(c_path)
            software_file_ext.append(fn)
        if ext in torrent_ext:
            torrent_file_path.append(c_path)
            torrent_file_ext.append(fn)

del rm_dir[0]

# print(combo_ext)
# print(combo_file_name)
# print(rm_dir)





# print(aud_file_path)
# print(doc_file_path)
# print(img_file_path)
# print(rm_dir)

# print(combo_file_name)
# print(aud_file_ext)
# print(torrent_file_ext)
# print(combo_ext in audio_ext)
# print(set(combo_ext))
# `C:\Test Case for Project
# for a in combo_ext:
#     if a in audio_ext:
#         print('yess')
# print(combo_ext in vid_ext) 

# ['mp3', 'jpg', 'txt', 'exe', 'jpg', 'torrent', 'py', 'mp3', 'mkv', 'png', 'jpg', 'pdf','exe', 'jpg', 'png', 'py', 'mkv', 'pdf', 'txt', 'txt', 'mp3', 'csv', 'json']

for check_ext in set(combo_ext):
    if check_ext in audio_ext:
        if os.path.exists(f"{os.getcwd()}\{audio_ext[-1]}"):
            pass        
        else:
            os.mkdir(f"{os.getcwd()}\{audio_ext[-1]}")
            for zipping_mus_file in zip(aud_file_path,aud_file_ext):
                shutil.move(f"{zipping_mus_file[0]}\{zipping_mus_file[1]}",f"{os.getcwd()}\{audio_ext[-1]}")

    if check_ext in doc_ext:
        if os.path.exists(f"{os.getcwd()}\{doc_ext[-1]}"):
            pass        
        else:
            os.mkdir(f"{os.getcwd()}\{doc_ext[-1]}")
            for zipping_doc_file in zip(doc_file_path,doc_file_ext):
                shutil.move(f"{zipping_doc_file[0]}\{zipping_doc_file[1]}",f"{os.getcwd()}\{doc_ext[-1]}")
    if check_ext in img_ext:
        if os.path.exists(f"{os.getcwd()}\{img_ext[-1]}"):
            pass        
        else:
            os.mkdir(f"{os.getcwd()}\{img_ext[-1]}")
            for zipping_img_file in zip(img_file_path,img_file_ext):
                shutil.move(f"{zipping_img_file[0]}\{zipping_img_file[1]}",f"{os.getcwd()}\{img_ext[-1]}")
    if check_ext in vid_ext:
        if os.path.exists(f"{os.getcwd()}\{vid_ext[-1]}"):
            pass        
        else:
            os.mkdir(f"{os.getcwd()}\{vid_ext[-1]}")
            for zipping_vid_file in zip(vid_file_path,vid_file_ext):
                shutil.move(f"{zipping_vid_file[0]}\{zipping_vid_file[1]}",f"{os.getcwd()}\{vid_ext[-1]}")
    if check_ext in compressed_ext:
        if os.path.exists(f"{os.getcwd()}\{compressed_ext[-1]}"):
            pass        
        else:
            os.mkdir(f"{os.getcwd()}\{compressed_ext[-1]}")
            for zipping_compressed_file in zip(compressed_file_path,compressed_file_ext):
                shutil.move(f"{zipping_compressed_file[0]}\{zipping_compressed_file[1]}",f"{os.getcwd()}\{compressed_ext[-1]}")
    if check_ext in disc_ext:
        if os.path.exists(f"{os.getcwd()}\{disc_ext[-1]}"):
            pass        
        else:
            os.mkdir(f"{os.getcwd()}\{disc_ext[-1]}")
            for zipping_disc_file in zip(disc_file_path,disc_file_ext):
                shutil.move(f"{zipping_disc_file[0]}\{zipping_disc_file[1]}",f"{os.getcwd()}\{disc_ext[-1]}")
    if check_ext in data_ext:
        if os.path.exists(f"{os.getcwd()}\{data_ext[-1]}"):
            pass        
        else:
            os.mkdir(f"{os.getcwd()}\{data_ext[-1]}")
            for zipping_data_file in zip(data_file_path,data_file_ext):
                shutil.move(f"{zipping_data_file[0]}\{zipping_data_file[1]}",f"{os.getcwd()}\{data_ext[-1]}")
    if check_ext in email_ext:
        if os.path.exists(f"{os.getcwd()}\{email_ext[-1]}"):
            pass        
        else:
            os.mkdir(f"{os.getcwd()}\{email_ext[-1]}")
            for zipping_email_file in zip(email_file_path,email_file_ext):
                shutil.move(f"{zipping_email_file[0]}\{zipping_email_file[1]}",f"{os.getcwd()}\{email_ext[-1]}")
    if check_ext in programming_ext:
        if os.path.exists(f"{os.getcwd()}\{programming_ext[-1]}"):
            pass        
        else:
            os.mkdir(f"{os.getcwd()}\{programming_ext[-1]}")
            for zipping_programming_file in zip(programming_file_path,programming_file_ext):
                shutil.move(f"{zipping_programming_file[0]}\{zipping_programming_file[1]}",f"{os.getcwd()}\{programming_ext[-1]}")

    if check_ext in software_ext:
        if os.path.exists(f"{os.getcwd()}\{software_ext[-1]}"):
            pass        
        else:
            os.mkdir(f"{os.getcwd()}\{software_ext[-1]}")
            for zipping_software_file in zip(software_file_path,software_file_ext):
                shutil.move(f"{zipping_software_file[0]}\{zipping_software_file[1]}",f"{os.getcwd()}\{software_ext[-1]}")

    if check_ext in torrent_ext:
        if os.path.exists(f"{os.getcwd()}\{torrent_ext[-1]}"):
            pass        
        else:
            os.mkdir(f"{os.getcwd()}\{torrent_ext[-1]}")
            for zipping_torrent_file in zip(torrent_file_path,torrent_file_ext):
                shutil.move(f"{zipping_torrent_file[0]}\{zipping_torrent_file[1]}",f"{os.getcwd()}\{torrent_ext[-1]}")

    
######################################################################################
# for check_aud_ext in set(combo_ext):
#     if check_aud_ext in audio_ext:
#         os.mkdir(f"{os.getcwd()}\{audio_ext[-1]}")
#         break # helps in avoiding multiple checking of extentions

# for check_vid_ext in set(combo_ext):
#     if check_vid_ext in vid_ext:
#         os.mkdir(f"{os.getcwd()}\{vid_ext[-1]}")
#         break # helps in avoiding multiple checking of extentions

# for check_softw_ext in set(combo_ext):
#     if check_softw_ext in software_ext:
#         os.mkdir(f"{os.getcwd()}\{software_ext[-1]}")
#         break # helps in avoiding multiple checking of extentions
#######################################################################################






# for one_by_one in bundle_ext:
#     for aud in one_by_one:
#         if aud in set(combo_ext):
#             print('yes')
#     # for audio in one_by_one:
    #     if audio in set(combo_ext):
    #         os.mkdir(f"{os.getcwd()}\{audio_ext[-1]}")
    #         print(audio in set(combo_ext))
    #         break
    # for video in one_by_one:
    #     if video in set(combo_ext):
    #         os.mkdir(f"{os.getcwd()}\{vid_ext[-1]}")
    #         print(video in set(combo_ext))
    #         break
    # for software in one_by_one:
    #     if software in set(combo_ext):
    #         os.mkdir(f"{os.getcwd()}\{software_ext[-1]}")
    #         print(software in set(combo_ext))
    #         break
    







# for one_by_one in bundle_ext:
#     for a in one_by_one:
#         if a in set(combo_ext):
#             os.mkdir(f"{os.getcwd()}\{audio_ext[-1]}")
#             break
#     for a1 in one_by_one:
#         if a1 in set(combo_ext):
#             os.mkdir(f"{os.getcwd()}\{doc_ext[-1]}")
#             break
    # for a3 in one_by_one:
    #     if a3 in software_ext:
    #         os.mkdir(f"{os.getcwd()}\{software_ext[-1]}")
    #         break

# # # directory for music files
# music_dir_path = f"{os.getcwd()}\Music"
# for a in set(combo_ext):
#     if a in audio_ext:
#         os.mkdir(f"{os.getcwd()}\{audio_ext[-1]}")
#         break # helps in avoiding multiple checking of extentions


# doc_dir_path = f"{os.getcwd()}\Documents"
# for a in set(combo_ext):
#     if a in :
#         os.mkdir(f"{os.getcwd()}\{audio_ext[-1]}")
#         break # helps in avoiding multiple checking of extentions


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




# help in ziping two data structures related to audio files

# for zipping_mus_file in zip(aud_file_path,aud_file_ext):
#     shutil.move(f"{zipping_mus_file[0]}\{zipping_mus_file[1]}",f"{os.getcwd()}\{audio_ext[-1]}")

# for zipping_doc_file in zip(doc_file_path,doc_file_ext):
#     shutil.move(f"{zipping_doc_file[0]}\{zipping_doc_file[1]}",f"{os.getcwd()}\{doc_ext[-1]}")

# for zipping_img_file in zip(img_file_path,img_file_ext):
#     shutil.move(f"{zipping_img_file[0]}\{zipping_img_file[1]}",f"{os.getcwd()}\{img_ext[-1]}")

# for zipping_vid_file in zip(vid_file_path,vid_file_ext):
#     shutil.move(f"{zipping_vid_file[0]}\{zipping_vid_file[1]}",f"{os.getcwd()}\{vid_ext[-1]}")

# for zipping_compressed_file in zip(compressed_file_path,compressed_file_ext):
#     shutil.move(f"{zipping_compressed_file[0]}\{zipping_compressed_file[1]}",f"{os.getcwd()}\{compressed_ext[-1]}")
    
# for zipping_disc_file in zip(disc_file_path,disc_file_ext):
#     shutil.move(f"{zipping_disc_file[0]}\{zipping_disc_file[1]}",f"{os.getcwd()}\{disc_ext[-1]}")
    
# for zipping_data_file in zip(data_file_path,data_file_ext):
#     shutil.move(f"{zipping_data_file[0]}\{zipping_data_file[1]}",f"{os.getcwd()}\{data_ext[-1]}")
    
# for zipping_email_file in zip(email_file_path,email_file_ext):
#     shutil.move(f"{zipping_email_file[0]}\{zipping_email_file[1]}",f"{os.getcwd()}\{email_ext[-1]}")
    
# for zipping_programming_file in zip(programming_file_path,programming_file_ext):
#     shutil.move(f"{zipping_programming_file[0]}\{zipping_programming_file[1]}",f"{os.getcwd()}\{programming_ext[-1]}")
    
# for zipping_software_file in zip(software_file_path,software_file_ext):
#     shutil.move(f"{zipping_software_file[0]}\{zipping_software_file[1]}",f"{os.getcwd()}\{software_ext[-1]}")
        
# for zipping_torrent_file in zip(torrent_file_path,torrent_file_ext):
#     shutil.move(f"{zipping_torrent_file[0]}\{zipping_torrent_file[1]}",f"{os.getcwd()}\{torrent_ext[-1]}")






# help in ziping two data structures related to doc files
# for zipping_doc_file in zip(doc_file_path,doc_file_ext):
#     shutil.move(f"{zipping_doc_file[0]}\{zipping_doc_file[1]}",doc_dir_path)


# # help in ziping two data structures related to img  files
# for zipping_img_file in zip(img_file_path,img_file_ext):
#     shutil.move(f"{zipping_img_file[0]}\{zipping_img_file[1]}",img_dir_path)






















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