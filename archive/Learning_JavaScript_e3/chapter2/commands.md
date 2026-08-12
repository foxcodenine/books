
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







### add https to website:

https://letsencrypt.org/
https://certbot.eff.org/

on certbot select the Software and System: 

My HTTP website is running 'Software' on 'System'

1. SSH into the server 
From the terminal connect to the server 

2.Add Certbot PPA 
Enter the commands given, currenty:
   $ sudo apt-get update
   $ sudo apt-get install software-properties-common
   $ sudo add-apt-repository universe
   $ sudo add-apt-repository ppa:certbot/certbot
   $ sudo apt-get update

3.Install Certbot
Run this command on the command line on the machine to install Certbot.
   $ sudo apt-get install certbot python-certbot-apache

#.Before going to next step, currently 4. you need to do the following.

  $ cd /etc/apache2/sites-available
  $ ls -l 

  create a file with nano with the site name with .conf 
  and insert the following:
  and update the DocumentRoot, ServerName & <Directory "****">
  as required:

  $ sudo nano foxhost9.com.conf

<VirtualHost *:80>
    DocumentRoot /var/www/foxhost9
    ServerName foxhost9.com 
    <Directory "/var/www/foxhost9">
        allow from all 
        AllowOverride All 
        Order allow,deny 
        Options +Indexes
    </Directory>
</VirtualHost>

  $ cd /var/www
  $ sudo mv html foxhost9

  $ cd /etc/apache2/sites-available
  $ ls

  enter the following command modify as required:

  $ sudo a2ensite foxhost9.com.conf
  $ sudo service apache2 reload  or $ sudo systemctl reload apache2


4.Choose how you'd like to run Certbot
  $ sudo certbot --apache

  or better or if doesn't work:

  $ sudo certbot --authenticator standalone --installer apache -d foxhost9.com --pre-hook "systemctl stop apache2" --post-hook "systemctl start apache2"

  #and select accordingly:

5. On AWS or your webhost go to inbound rules and open  post 443 (for https traffic).

  $ cd /etc/apache2/sites-available
  $ ls
  
  #and see that a new file is create in this case foxhost9.com-le-ssl.conf


### to redirect www.foxhost9.com to foxhost9.com 
  
  1. add another A type record with the www example: www.foxhost9.com 
  pointing to your IPv4 Public IP.

  2. edit with nano your .conf file example: foxhost9.com.conf and add 
  the following VirtualHost before your VirtualHost:  


<VirtualHost *:80>
    ServerName www.foxhost9.com
    Redirect permanent / http://foxhost9.com/
</VirtualHost>
<VirtualHost *:80>
  Docume........
  ................
  ....
</VirtualHost>

$ sudo service apache2 restart
