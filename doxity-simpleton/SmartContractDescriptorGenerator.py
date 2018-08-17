import os
import json
import shutil
from distutils.dir_util import copy_tree



def convertDoxityMetadata2ContractDescriptor (contractMetadataFile):

  file=open('doxity-metadata-files/' + contractMetadataFile).read()
  data = json.loads(file)

  fileAddressMap=open('contractAddressesList.json').read()
  dataAddressMap = json.loads(fileAddressMap)
  metadata_field = json.loads(data['metadata'])

  
  # DESCRIPTOR
  descriptor = {}
  descriptor['name'] = list(metadata_field['settings']['compilationTarget'].values())[0]

  descriptor['author'] = '' # DEFAULT VALUE
  if 'author' in data['devdoc']:
    descriptor['author'] = data['devdoc']['author']

  descriptor['language'] = metadata_field['language']

  descriptor['contract_type'] = 'generic_contract'  # DEFAULT VALUE
  fileContract=open('contracts/' + contractMetadataFile.replace('.json','.sol')).read()
  substring = "library " + contractMetadataFile.replace('.json','') + " {"
  if substring in fileContract:
    descriptor['contract_type'] = 'library'

  descriptor['contract_version'] = '1.0' # DEFAULT VALUE
  descriptor['descriptor_version'] = '1.0'  # DEFAULT VALUE

  descriptor['abi'] = data['abi']
  descriptor['userdoc'] = data['userdoc']


  # ENDPOINT
  endpoint = {}
  if descriptor['name'] in dataAddressMap:
  	endpoint['address'] = dataAddressMap[descriptor['name']]['address']
  	endpoint['networkID'] = dataAddressMap[descriptor['name']]['networkID']
  	endpoint['chainID'] =dataAddressMap[descriptor['name']]['chainID']


  # DEV
  dev = {}
  dev['devdoc'] = data['devdoc']
  dev['sources'] = {}
  dev['sources']['keccak256'] = list(metadata_field['sources'].values())[0]['keccak256']
  dev['sources']['swarm_URL'] = list(metadata_field['sources'].values())[0]['urls'][0]
  dev['libraries'] = metadata_field['settings']['libraries']

  compiler = {}
  compiler['version'] = metadata_field['compiler']['version']
  compiler['evmVersion'] = metadata_field['settings']['evmVersion']
  dev['compiler'] = compiler


  # CONTRACT
  contractDescriptor = {}
  contractDescriptor['contract'] = {}
  contractDescriptor['contract']['descriptor'] = descriptor
  contractDescriptor['contract']['endpoint'] = endpoint
  contractDescriptor['contract']['dev'] = dev

  return contractDescriptor




JSONfileForAPI = {}
JSONfileForAPIarray = []

for contractMetadataFile in os.listdir('doxity-metadata-files'): # filenames with extension
  if contractMetadataFile!=".DS_Store":
    contractDescriptorJSON = convertDoxityMetadata2ContractDescriptor(contractMetadataFile)
    with open('contract-descriptor-files/' + contractMetadataFile, 'w') as outfile:
      json.dump(contractDescriptorJSON, outfile)

# Generation of the DB file for the API server      
    sourceCode = open('contracts/' + contractMetadataFile.replace('.json','.sol')).read()

    contractDescriptorJSONforAPI = {}
    contractDescriptorJSONforAPI['name'] = contractDescriptorJSON['contract']['descriptor']['name']
    contractDescriptorJSONforAPI['contract_type'] = contractDescriptorJSON['contract']['descriptor']['contract_type']
    contractDescriptorJSONforAPI['JSON'] = contractDescriptorJSON
    contractDescriptorJSONforAPI['code'] = sourceCode
    JSONfileForAPIarray.append(contractDescriptorJSONforAPI)

JSONfileForAPI['contracts'] = JSONfileForAPIarray;

cwd = os.path.dirname(os.path.realpath(__file__))
parentCwd = os.path.abspath(os.path.join(cwd, os.pardir))
with open(parentCwd + '/REST_API/smartContractDescriptorsAPI-DB.json', 'w') as outfile:
  json.dump(JSONfileForAPI, outfile)



print ("\nAll the metadata files in the doxity_metadata_files folder were converter to contract descriptors and were stored in the contract-descriptor-files folder!\n")

print ("All the contract descriptors were merged and stored in the REST_API folder!\n\n")

