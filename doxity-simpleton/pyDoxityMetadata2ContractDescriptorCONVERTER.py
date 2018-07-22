import os
import json
import shutil
from distutils.dir_util import copy_tree



def convertDoxityMetadata2ContractDescriptor (contractMetadataFile):

  file=open('doxity-metadata-files/' + contractMetadataFile).read()
  data = json.loads(file)

  metadata_field = json.loads(data['metadata'])

  contract = {}
  contract['name'] = list(metadata_field['settings']['compilationTarget'].values())[0]

  contract['author'] = 'Unknown' # DEFAULT VALUE
  if 'author' in data['devdoc']:
    contract['author'] = data['devdoc']['author']

  contract['version'] = '1.0' # DEFAULT VALUE
  contract['language'] = metadata_field['language']
  contract['contract_type'] = 'generic_contract'  # DEFAULT VALUE
  contract['abi'] = data['abi']
  contract['devdoc'] = data['devdoc']
  contract['userdoc'] = data['userdoc']
  contract['sources'] = metadata_field['sources']
  contract['libraries'] = metadata_field['settings']['libraries']

  deployment_information = {}
  deployment_information['address'] = '0x314159265dd8dbb310642f98f50c066173c1259b'  # DEFAULT VALUE
  deployment_information['networkID'] = 1  # DEFAULT VALUE
  deployment_information['chainID'] = 1  # DEFAULT VALUE

  compiler = {}
  compiler['version'] = metadata_field['compiler']['version']
  compiler['evmVersion'] = metadata_field['settings']['evmVersion']

  descriptor = {}
  descriptor['version'] = '1.0'  # DEFAULT VALUE


  contractDescriptor = {}
  contractDescriptor['contract'] = contract
  contractDescriptor['deployment_information'] = deployment_information
  contractDescriptor['compiler'] = compiler
  contractDescriptor['descriptor'] = descriptor

  return contractDescriptor



for contractMetadataFile in os.listdir('doxity-metadata-files'): # filenames with extension
  if contractMetadataFile!=".DS_Store":
    with open('contract-descriptor-files/' + contractMetadataFile, 'w') as outfile:
      json.dump(convertDoxityMetadata2ContractDescriptor(contractMetadataFile), outfile)


print ("\nAll the metadata files in the doxity_metadata_files folder were converter to contract descriptors and were stored in the contract-descriptor-files folder!\n")
print("\n")

