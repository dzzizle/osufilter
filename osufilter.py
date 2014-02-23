import os
import sys

def get_files(dir):
    return [name for name in os.listdir(dir)]

song_dir = sys.argv[1]
diffs = ["Easy", "Normal", "Beginner", "Standard", "Taiko", "Oni", "Muzukashii"];

#Change if you want to delete a certain types
del_maps = True
del_hitsounds = True
del_skins = False
del_bg = False

for dir in get_files(song_dir):
    if (not os.path.isdir(os.path.join(dir, song_dir))):
        continue

    dir_path = song_dir + dir + "/"
    for file in get_files(dir_path):
        if file.endswith(".osu") and del_maps: 
            difficulty = file.split("[")[1].replace("].osu", "") #for the rare occasion that the song name contains an difficulty name
            for diff in diffs:
                if diff in difficulty:
                    os.remove(dir_path + file)
                    print("Deleted " + dir_path + file)
                    break
        elif file.endswith(".wav") and del_hitsounds: #only hitsounds are .wav
            os.remove(dir_path + file)
            print("Deleted " + dir_path + file)
        elif file.endswith(".png") and del_skins: #backgrounds are USUALLY only .jpg. Use at own risk.
            os.remove(dir_path + file)
            print("Deleted " + dir_path + file)
        elif file.endswith(".jpg") and del_bg: 
            os.remove(dir_path + file)
            print("Deleted " + dir_path + file)

