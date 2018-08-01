# SoliditySmartContractRegistry


## Installation instructions


### Registry (documentation generator)

```
cd /Users/Guida/GitHub/SoliditySmartContractRegistry
git clone https://www.github.com/ryanhendricks/doxity-simpleton.git
```

Edit the following files to match your Github Repo to use Github Pages

- /doxity-simpleton/package.json: the fields must match your Github Repo to use Github Pages
- /doxity-simpleton/doxity/config.toml: "linkPrefix = "/doxity-simpleton"" must match your Github Repo


```
cd /Users/Guida/GitHub/SoliditySmartContractRegistry/doxity-simpleton/doxity
yarn
```

```
cd /Users/Guida/GitHub/SoliditySmartContractRegistry/doxity-simpleton
yarn
```

NB: Repeat the two "yarn" commands if you change the directory location!!!



### REST API

```
npm install -g json-server
```
Creare the db.json and put it in cd /Users/Guida/GitHub/SoliditySmartContractRegistry/REST_API

(https://medium.com/codingthesmartway-com-blog/create-a-rest-api-with-json-server-36da8680136d)



## Usage instructions


Copy solidity contracts to the contracts folder, then build the docs:

```
cd /Users/Guida/GitHub/SoliditySmartContractRegistry/doxity-simpleton

python pyCleanContractDescriptorsDir.py
npm run docs
python pyDocsUpdater.py
python pyDoxityMetadata2Descriptor_API.py
```


### To visualize the docs:

```
cd /Users/Guida/GitHub/SoliditySmartContractRegistry/docs/docs/
python -m http.server
```

To start the REST API

```
cd /Users/Guida/GitHub/SoliditySmartContractRegistry/REST_API
json-server --watch metadataDB.json
```

Examples of GET queries (may be tested with POSTMAN):
```
http://localhost:3000/contracts?contract_type=generic_contract
http://localhost:3000/contracts?name=Set
```

### To fully access the docs, publish them on GitHub pages:

1) commit the /docs folder to a GitHub repository
2) Visit the repository’s settings tab and select master branch /docs folder as the GitHub Pages source. 
3) Click save, and check the link to the GitHub page: after a few minutes, the website will be online.




