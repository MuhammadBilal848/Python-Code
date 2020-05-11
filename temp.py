import os,shutil
print(os.getcwd())
# os.chdir("C:\First Demo Project")
# print(os.getcwd())
# "C:\First Demo Project\file4.txt","C:\\"
# shutil.move("C:\First Demo Project\file5.txt","D:\file5.txt     ")
# os.chdir('C:\First Demo Project')
# print(os.getcwd())

# os.chdir("C:\First Demo Project\new folder\New folder")
# print(os.getcwd())


# shutil.move(r"C:\First Demo Project\Heading Home.mp3","C:\First Demo Project\Music")
# shutil.move(r"C:\First Dem`o Project\new folder\NoreAzal.mp3","C:\First Demo Project\Music\\")
# shutil.move(r"C:\First Dem`o Project\new folder\New folder\Imagine Dragons Bad Liar.mp3","C:\First Demo Project\Music")
 
# d = { "BSSE-SEC-A":["bilal","abuzar","usama","zaigham"] , "BSSE-SEC-B":["bilal1","abuzar2","usama3","zaigham4"] }
# print(d["BSSE-SEC-A"][::-1])

audio_ext = ("mp3","WAV","PCM","m4a")


combo_ext = {'png', 'pdf', 'mp3', 'txt', 'jpg','png',  'jpg','pdf', 'mp3', 'txt'}
# # directory for music files
for a in set(combo_ext):
    if a in audio_ext:
        os.mkdir("C:\First Demo Project\Music")
        break