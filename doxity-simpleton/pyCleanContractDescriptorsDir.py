import shutil
import os.path
from distutils.dir_util import copy_tree



# Clean /contract-descriptor-files folder from repo path
cwd = os.path.dirname(os.path.realpath(__file__))

if os.path.exists(cwd + "/contract-descriptor-files"):
  shutil.rmtree(cwd + "/contract-descriptor-files")
os.makedirs(cwd + "/contract-descriptor-files")


print ("\ncontract-descriptor-files folder cleaned!\n")
