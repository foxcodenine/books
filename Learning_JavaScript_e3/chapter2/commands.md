
### to initialization , --yes to accept all defaults:
$ npm init --yes

### to install babel command-line and babel prest env:
#### i is for install 
#### --save-dev to save these as a development dependency
$ npm i --save-dev babel-cli babel-preset-env
<!-- $ npm i --save-dev babel-cli -->
<!-- $ npm i --save-dev babel-preset-env -->

### npm-run-script 
### update the package.json script

{
  "name": "chapter2",
  "version": "1.0.0",
  "description": "= Learning JavaScript, 3rd Edition  == Chapter 2: JavaScript Development Tools",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "babelnode": "babel es6 -d dist",  <--
    "babelbrowser": "babel public\\es6 -d public\\dist", <--
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "babel-cli": "^6.26.0",
    "babel-preset-env": "^1.7.0"
  }
}

### execute script from CLI
$ npm run buildnode
or/and
$ npm run babelbrowser

t
#### list global packages
$ npm list -g --depth 0