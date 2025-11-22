import os
import shutil
PATH = r'type your path here'
EXCLUDE = ['Images', 'PDFs', 'GIFs', 'Installers','Others', 'All Folders', "Mini Project Repo", "Audios", "Videos"]

#r means it is raw string
for filename in os.listdir(PATH): # for each foldername in path list directory
    location = os.path.join(PATH, filename)
    #sticks file name and path
    #then i will check if it is a folder, if yes skips it


    #new function: making 'all folders' folder to collect all.
    if os.path.isdir(location):
        if filename in EXCLUDE:
            continue
        newfolder = os.path.join(PATH, "All Folders")
        if not os.path.exists(newfolder):
            os.makedirs(newfolder)
        shutil.move(location, os.path.join(newfolder, filename))
        print(f"{filename} Moved to {newfolder}")
        continue
    if filename.endswith(".png") or filename.endswith('.jpeg') or filename.endswith('.jpg') or filename.endswith('.tiff') or filename.endswith('.bmp'):
        newfolder = os.path.join(PATH, "Images")
        if not os.path.exists(newfolder):
            os.makedirs(newfolder)
        shutil.move(location, os.path.join(newfolder, filename))
        print(f"{filename} Moved to {newfolder}")
    elif filename.endswith(".pdf"):
        newfolder = os.path.join(PATH, "PDFs")
        if not os.path.exists(newfolder):
            os.makedirs(newfolder)
        shutil.move(location, os.path.join(newfolder, filename))
        print(f"{filename} Moved to {newfolder}")
    elif filename.endswith(".gif"):
        newfolder = os.path.join(PATH, "GIFs")
        if not os.path.exists(newfolder):
            os.makedirs(newfolder)
        shutil.move(location, os.path.join(newfolder, filename))
        print(f"{filename} Moved to {newfolder}")
    elif filename.endswith(".exe") or filename.endswith('.msi'):
        newfolder = os.path.join(PATH, "Installers")
        if not os.path.exists(newfolder):
            os.makedirs(newfolder)
        shutil.move(location, os.path.join(newfolder, filename))
        print(f"{filename} Moved to {newfolder}")
    elif filename.endswith(".mp3") or filename.endswith('.wav') or filename.endswith('.m4a') or filename.endswith('.wma'):
        newfolder = os.path.join(PATH, "Audios")
        if not os.path.exists(newfolder):
            os.makedirs(newfolder)
        shutil.move(location, os.path.join(newfolder, filename))
        print(f"{filename} Moved to {newfolder}")
    elif filename.endswith(".mp4") or filename.endswith('.mov') or filename.endswith('.avi') or filename.endswith('.wmv'):
        newfolder = os.path.join(PATH, "Videos")
        if not os.path.exists(newfolder):
            os.makedirs(newfolder)
        shutil.move(location, os.path.join(newfolder, filename))
        print(f"{filename} Moved to {newfolder}")
    else:
        newfolder = os.path.join(PATH, "Others")
        if not os.path.exists(newfolder):
            os.makedirs(newfolder)
        shutil.move(location, os.path.join(newfolder, filename))
print("All operations has done!")