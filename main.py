# Relative paths
import os

from src.inputs import chooseFile, chooseFunction
from src.chats import getChats
from src.counter import countMessages


def main():
    directory = os.path.dirname(os.path.abspath(__file__))
    txtFiles = getChats(directory)
    file = chooseFile(txtFiles)
    function = chooseFunction()
    path = os.path.join(txtFiles[file-1][0], txtFiles[file-1][1])

    countMessages(path, *function)
    input("\nPress ENTER to exit")


if __name__ == '__main__':
    main()
