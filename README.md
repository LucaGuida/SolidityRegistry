# SolidityRegistry


## Installation instructions


### Documentation and website generator

```
cd ~/GitHub/SolidityRegistry
git clone https://www.github.com/ryanhendricks/doxity-simpleton.git
```

Edit the following files to match your Github Repo to use Github Pages

- /doxity-simpleton/package.json: the fields must match your Github Repo to use Github Pages
- /doxity-simpleton/doxity/config.toml: "linkPrefix = "/doxity-simpleton"" must match your Github Repo


```
cd ~/GitHub/SolidityRegistry/doxity-simpleton/doxity
yarn
```

```
cd ~/GitHub/SolidityRegistry/doxity-simpleton
yarn
```

NB: Repeat the two "yarn" commands if you change the directory location!!!


Now rename the doxity-simpleton folder into documentationGenerator.


### REST API

```
npm install -g json-server
```



## Usage instructions


Copy Solidity contracts to the /contracts folder, then build the docs:

```
cd ~/GitHub/SolidityRegistry/documentationGenerator
python DocumentationGenerator.py
python SmartContractDescriptorGenerator.py
```


### To start the REST API

```
cd ~/GitHub/SolidityRegistry/REST_API
json-server --watch smartContractDescriptorsAPI-DB.json
```

Examples of GET queries (may be tested with POSTMAN):
```
http://localhost:3000/contracts?contract_type=generic_contract
http://localhost:3000/contracts?name=Set
```

### To deploy the docs on GitHub pages:

1) commit the /docs folder to a GitHub repository
2) Visit the repository’s settings tab and select master branch /docs folder as the GitHub Pages source. 
3) Click save, and check the link to the GitHub page: after a few minutes, the website will be online.



This project was implemented starting from some pre-existing modules:
* Doxity (http://github.com/DigixGlobal/doxity - BSD-3-Clause license) and its variant Doxity Simpleton (http://github.com/RyanHendricks/doxity-simpleton)

