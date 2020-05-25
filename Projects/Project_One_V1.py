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


# promts user for directory path 
path = input("Enter directory path: ")


# use to get into working directory ( where this script needs to be run )
os.chdir(path)


# helps to append data in data structures
for c_path,c_folder,c_file in os.walk(os.getcwd()):
    rm_dir.append(c_path) # appending directory path that later can be removed
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



# help in zipping two data structures and making dirs as well as move data into these dirs
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


for a in rm_dir[::-1]:
    shutil.rmtree(a)