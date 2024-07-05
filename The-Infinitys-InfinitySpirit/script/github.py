import os


def renew():
    os.system("git config user.name github-actions")
    os.system("git config user.email github-actions@github.com")
    os.system("git add .")
    os.system('git commit -m "made with Infinity Style Static Site Generator"')
    os.system("git push")
