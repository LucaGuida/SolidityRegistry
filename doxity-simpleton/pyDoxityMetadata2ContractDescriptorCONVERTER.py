import os
import json
import shutil
from distutils.dir_util import copy_tree



def convertDoxityMetadata2ContractDescriptor (contractMetadataFile):

  file=open('doxity-metadata-files/' + contractMetadataFile).read()
  data = json.loads(file)

  metadata_field = json.loads(data['metadata'])

  
  # DESCRIPTOR
  descriptor = {}
  descriptor['name'] = list(metadata_field['settings']['compilationTarget'].values())[0]

  descriptor['author'] = 'Unknown' # DEFAULT VALUE
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
  endpoint['address'] = '0x314159265dd8dbb310642f98f50c066173c1259b'  # DEFAULT VALUE
  endpoint['networkID'] = 1  # DEFAULT VALUE
  endpoint['chainID'] = 1  # DEFAULT VALUE


  # DEV
  dev = {}
  dev['devdoc'] = data['devdoc']
  dev['sources'] = metadata_field['sources']
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



for contractMetadataFile in os.listdir('doxity-metadata-files'): # filenames with extension
  if contractMetadataFile!=".DS_Store":
    with open('contract-descriptor-files/' + contractMetadataFile, 'w') as outfile:
      json.dump(convertDoxityMetadata2ContractDescriptor(contractMetadataFile), outfile)


print ("\nAll the metadata files in the doxity_metadata_files folder were converter to contract descriptors and were stored in the contract-descriptor-files folder!\n")
print("\n")

