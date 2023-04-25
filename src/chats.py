# Traverse directories
import os


def getChats(root):
    txtFiles = []
    for path, _, files in os.walk(root):
        for file in files:
            if file.endswith(".txt"):
                txtFiles.append([path, file])

    return txtFiles
