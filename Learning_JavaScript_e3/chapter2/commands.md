
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

### unstage all from git
$ git reset

### ls hidden files powershell
ls -Force




## eslint

### install eslint in dev
$ npm install --save-dev eslint

### or install eslint in g
$ npm i -g eslint u

### to initializatio eslit
$ npx eslint --init

### to check specific file
$ npx eslint yourfile.js

### to check all files is directory and sub-directories
$ npx eslint  **/*.js 

### to fix check and fix file or files
$ npx eslint --fix yourfile.js     or     $ npx eslint --fix **/*.js 



### cloning a git repository OVER SSH:
$ git clone ssh://git@bitbucket.org:teamsinspace/documentation-tests.git

### GIT to removing multiple commits (remove the last two commits)
$ reset --hard HEAD~2 


### running a new ubuntu server

$ sudo apt update

$ sudo apt upgrade

$ sudo apt install apache2

##### display apache commands
$ sudo service apachi2 

##### display apache status
$ sudo service apachi2 status

## apache directory 
$ cd /etc/apache2/
$ ls -l

## sites-available dirc
$ cd /etc/apache2/sites-available/

#### http  file : 000-default.conf
#### https file : default-ssl.conf
$ nano 000-default.conf

### DocumentRoot
/var/www/html

### check which binary git is:
$ which git

### check git version:
$ git --version

### to install git:
$ sudo install git

### git clone in to a folder (example to html)
$ git clone https://github.com/robertbunch/jquery-todo.git html

### switch to super user
$ sudo su

### end su
$ exit

### change file or folder ownershipp
$ sudo chown -R newUser folderName/
