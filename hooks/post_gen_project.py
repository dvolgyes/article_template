#!/usr/bin/env python3
import sys
import wget
import os
from pathlib import Path
from collections import defaultdict


def wget_as(url, filename, save_url=False):
    tempfile = Path(wget.download(url))
    if tempfile.exists():
        tempfile.rename(filename)
    else:
        sys.exit(1)
    if save_url:
        with open(filename + ".url", "wt") as f:
            f.write(url)
            f.write("\n")


if "{{cookiecutter.online_gitignore}}".lower() == "y":
    wget_as(
        "https://github.com/github/gitignore/blob/master/TeX.gitignore", ".gitignore"
    )

# templates:
templates = {
    "arxiv": "https://raw.githubusercontent.com/kourgeorge/arxiv-style/master/arxiv.sty",
    "nips_2018": "https://media.nips.cc/Conferences/NIPS2018/Styles/nips_2018.sty",
}

style = "{{cookiecutter.style}}"
if style in templates:
    filename = wget.download(templates[style])
    with open(filename + ".url", "wt") as f:
        f.write(templates[style])
        f.write("\n")

os.system("git init .")
os.system("git add .")
os.system('git commit . -m "Initial commit."')
git_backend = "{{cookiecutter.git_backend}}".lower()
if git_backend != "none":
    git_server = None
    if git_backend == "github":
        git_server = "github.com"
    elif git_backend == "bitbucket":
        git_server = "bitbucket.org"
    elif git_backend == "gitlab":
        git_server = "gitlab.com"
    elif git_backend == "uio":
        git_server = "github.uio.no"
    else:
        git_server = git_backend
    os.system(
        "git remote add origin git@{git_server}:{{cookiecutter.username}}/{{cookiecutter.project_slug}}"
    )
