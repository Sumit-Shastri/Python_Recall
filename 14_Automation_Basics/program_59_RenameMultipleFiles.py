# rename multiple files in folder

import os


def renameFiles(fold):
    for filename in os.listdir(fold):
        new_name = filename + ".txt"
        os.rename(
            os.path.join(fold, filename),
            os.path.join(fold, new_name)
        )


folder = "/home/sumit/Desktop/python_recall/14_Automation_Basics/program_59"
renameFiles(folder)

