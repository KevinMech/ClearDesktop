#!/usr/bin/env python3

import os
import glob

PATH = os.path.expanduser('~/Desktop/')


class FileRemover():
    """used to remove the files on the desktop"""

    def __init__(self, path):
        self.files = []
        self.path = path

    def find(self):
        """Finds all files in folder and prompts user for removal"""
        os.chdir(self.path)
        for file in glob.glob('*.*'):
            # prevents file from deleting itself
            if file != 'clear_desktop.py':
                self.files.append(file)
        self._warning()

    def _warning(self):
        if len(self.files) > 0:
            for file in self.files:
                print(file)
            print()
            print('Would you like to delete these files? [y/n]')
            userinput = input()
            if(userinput == 'y' or userinput == 'yes'):
                self._deletef()
        else:
            print('No files found in ' + self.path)
        print()
        print('Now exiting program...')

    def _deletef(self):
        print()
        for file in self.files:
            print('deleting ' + file)
            os.remove(file)
        print('All done!')


desktop = FileRemover(PATH)
desktop.find()
