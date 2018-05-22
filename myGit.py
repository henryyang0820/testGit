from git import Repo
repo = Repo('E:\inquiryFund')
print(repo.bare)
print(repo.is_dirty())
print(repo.active_branch)