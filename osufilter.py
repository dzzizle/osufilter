import os
import sys

def get_files(dir):
    return [name for name in os.listdir(dir)]

songDir = sys.argv[1]
diffs = ["Easy", "Normal", "Beginner", "Standard", "Taiko", "Oni", "Muzukashii"];

for dir in get_files(songDir):
	if (not os.path.isdir(os.path.join(dir, songDir))):
		continue

	dirPath = songDir + dir + "/"
	for file in get_files(dirPath):
		if ".osu" in file: 
			difficulty = file.split("[")[1].replace("].osu", "") #for the rare occasion that the song name contains an difficulty name
			for diff in diffs:
				if diff in difficulty:
					os.remove(dirPath + file)
					print("Deleted " + file)
					break
