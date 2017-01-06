import os
import glob

PATH = os.path.expanduser('~/Desktop/')


class FileExplorer():
    """used to manipulate the files on the desktop"""

    def __init__(self, path):
        self.files = []
        self.path = path

    def __warning__(self):
        for file in self.files:
            print(file)
        print()
        print('Would you like to delete these files? [y/n]')
        userinput = input()
        if(userinput == 'y' or userinput == 'yes'):
            self.__deletef__()

    def __deletef__(self):
        print()
        for file in self.files:
            print('deleting ' + file)
            os.remove(file)
        print('All done! Now exiting program!')

    def find(self):
        os.chdir(PATH)
        for file in glob.glob('*.*', recursive=True):
            if file != 'clear_desktop.py':
                self.files.append(file)
        self.__warning__()


desktop = FileExplorer(PATH)
desktop.find()
