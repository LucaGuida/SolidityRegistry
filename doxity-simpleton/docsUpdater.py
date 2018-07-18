import shutil
import os.path
from distutils.dir_util import copy_tree



# Remove /docs folder from repo path, if existing
cwd = os.path.dirname(os.path.realpath(__file__))
parentCwd = os.path.abspath(os.path.join(cwd, os.pardir))

if os.path.exists(parentCwd + "/docs"):
  shutil.rmtree(parentCwd + "/docs")
os.makedirs(parentCwd + "/docs")



fromDirectory = os.path.dirname(os.path.abspath(__file__)) + "/docs"
toDirectory = parentCwd + "/docs"

copy_tree(fromDirectory, toDirectory)

print ("\nDocs folder updated!\n")

