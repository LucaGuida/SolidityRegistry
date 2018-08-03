import os.path
import shutil
from distutils.dir_util import copy_tree
from subprocess import call



# Clean /contract-descriptor-files folder from repo path
cwd = os.path.dirname(os.path.realpath(__file__))
if os.path.exists(cwd + "/contract-descriptor-files"):
  shutil.rmtree(cwd + "/contract-descriptor-files")
os.makedirs(cwd + "/contract-descriptor-files")
print ("\ncontract-descriptor-files folder cleaned!")


# Clean /doxity-metadata-files folder from repo path
cwd = os.path.dirname(os.path.realpath(__file__))
if os.path.exists(cwd + "/doxity-metadata-files"):
  shutil.rmtree(cwd + "/doxity-metadata-files")
os.makedirs(cwd + "/doxity-metadata-files")
print ("\ndoxity-metadata-files folder cleaned!")


print ("\nReady to start the Documentation generator...\n")
call(["npm", "run", "docs"])


# Clean /docs folder, then copy new version of /docs folder
print ("\nDocumentation generation completed. Ready to update /docs folder....")
cwd = os.path.dirname(os.path.realpath(__file__))
parentCwd = os.path.abspath(os.path.join(cwd, os.pardir))
if os.path.exists(parentCwd + "/docs"):
  shutil.rmtree(parentCwd + "/docs")
os.makedirs(parentCwd + "/docs")

fromDirectory = os.path.dirname(os.path.abspath(__file__)) + "/docs"
toDirectory = parentCwd + "/docs"
copy_tree(fromDirectory, toDirectory)
print ("\n/docs folder updated!\n")
