#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os
from git import Repo

base_path = os.path.dirname(os.path.abspath(__file__))
excel_path = os.path.abspath(base_path+'\myfundStatistics')

print(excel_path)
repo = Repo('E:/testGit')
print(repo.is_dirty())
index = repo.index
index.add(['myGit.py'])
index.add(['myfundStatistics.xlsx'])
index.commit('update statistics by excel')
remote = repo.remote()
print(remote.name)
remote.push()