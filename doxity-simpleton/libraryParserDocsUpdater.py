import os
import json
import shutil
import os.path
from distutils.dir_util import copy_tree


def extractMethods (contractName):
	methods = []
	file=open('doxity/pages/docs/' + contractName + '.json').read()
	data = json.loads(file)

	for method in data['abi']:
		if method['type']=='function': 
			methods.append(method['name'])
		if method['type']=='constructor':
			methods.append(contractName)
	return methods

def pretty(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         print('\t' * (indent+1) + str(value))


librariesMethodsMap = {}

for element in os.listdir("docs/docs"):
    #if element.endswith(".txt"):
    if element!=".DS_Store":
    	librariesMethodsMap[element] = extractMethods(element)


with open('librariesList.json', 'w') as outfile:
    json.dump(librariesMethodsMap, outfile)

print ("\nThe following libraries and functions are ready to be imported into Blockly Solidity!\n")
pretty(librariesMethodsMap)
print("\n")




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

