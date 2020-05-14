import os,shutil

audio_ext = ("mp3","WAV","PCM","m4a","3ga","aa","aa3","aac","ac3","acm","act","aif","avr","awb")
doc_ext = ("pdf","txt","doc","ppt","pptx","docx","xlx","xlsx","csv","json","html","htm","odx")
img_ext = ("jpg","png","gif","jpeg","psd","eps","ai","bmp","raw","indd","tiff","svg" )
combo_ext = []
combo_file_name = []
aud_file_path = list()
aud_file_ext = list()
doc_file_path = list()
doc_file_ext = list()
img_file_path = list()
img_file_ext = list()
rm_dir = list()



# use to get into working directory ( where this script needs to be run )
os.chdir("C:\First Demo Project")


# use to push values in data structures 
for c_path,c_folder,c_file in os.walk(os.getcwd()):
    rm_dir.append(c_path)
    for fn in c_file:
        name,ext = fn.split(".")
        combo_ext.append(ext)
        combo_file_name.append(fn)

del rm_dir[0]

# use to create directory where all the audio files needs to push
music_dir_path = f"{os.getcwd()}\Music"
for check_aud_ext in set(combo_ext):
    if check_aud_ext in audio_ext:
        os.mkdir(music_dir_path)
        break # helps in avoiding multiple checking of extentions


doc_dir_path = f"{os.getcwd()}\Documents"
for check_doc_ext in set(combo_ext):
    if check_doc_ext in doc_ext:
        os.mkdir(doc_dir_path)
        break # helps in avoiding multiple checking of extentions


img_dir_path = f"{os.getcwd()}\Pictures"
for check_img_ext in set(combo_ext):
    if check_img_ext in img_ext:
        os.mkdir(img_dir_path)
        break # helps in avoiding multiple checking of extentions


# consider this as a filter that filters audio files , integral part  , also push data in data structures
for c_path,c_folder,c_file in os.walk(os.getcwd()):
    for fn in c_file:
        name,ext = fn.split(".")
        if ext in audio_ext:
            aud_file_path.append(c_path)
            aud_file_ext.append(fn)
        if ext in doc_ext:
            doc_file_path.append(c_path)
            doc_file_ext.append(fn)
        if ext in img_ext:
            img_file_path.append(c_path)
            img_file_ext.append(fn)


# help in ziping two data structures related to audio files
for zipping_mus_file in zip(aud_file_path,aud_file_ext):
    shutil.move(f"{zipping_mus_file[0]}\{zipping_mus_file[1]}","C:\First Demo Project\Music")


# help in ziping two data structures related to doc files
for zipping_doc_file in zip(doc_file_path,doc_file_ext):
    shutil.move(f"{zipping_doc_file[0]}\{zipping_doc_file[1]}",doc_dir_path)


# help in ziping two data structures related to img  files
for zipping_img_file in zip(img_file_path,img_file_ext):
    shutil.move(f"{zipping_img_file[0]}\{zipping_img_file[1]}",img_dir_path)

# help in removing empty directory
for c_f_p in rm_dir[::-1]:
    os.rmdir(c_f_p)