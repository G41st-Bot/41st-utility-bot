import os
import sys
import git_pull

sys.path.insert(0, f'{os.getcwd()}/41st-bot')

import launcher

git_pull.download1("merit.txt")
git_pull.download2("demerit.txt")
git_pull.download3("registry.txt")
git_pull.download4("reports.txt")


def start():
    launch()


start()