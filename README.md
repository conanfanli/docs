Everything
==========

Postgres
--------
- SELECT * FROM "pg_user" 
- DROP USER someone
 

Django & uWsgi & nginx
----------------------
- Create conf file under /etc/nginx/mysite.conf

```
# the upstream component nginx needs to connect to
upstream django {
    server unix://tmp/mysite.sock; # for a web port socket (we'll use this first)
}

# configuration of the server
server {
    # the port your site will be served on
    listen      80;
    # the domain name it will serve for
    server_name localhost; # substitute your machine's IP address or FQDN
    charset     utf-8;

    # max upload size
    client_max_body_size 75M;   # adjust to taste

    # Django media
    location /media  {
        alias /www/nectar/media;  # your Django project's media files - amend as required
    }

    location /static {
        alias /www/nectar/static; # your Django project's static files - amend as required
    }

    # Finally, send all non-media requests to the Django server.
    location / {
        uwsgi_pass  django;
        include     /etc/nginx/uwsgi_params; # the uwsgi_params file you installed
    }
}
```

Git
---
```
git config --global color.ui true    # Turn on color

# Configure user name and email
git config --global user.name "John Doe" 
git config --global user.email johndoe@example.com

# To revert last commit that is NOT pushed to remote
git reset --hard HEAD^

# Made some changes in master branch and want to apply those to the dev branch
git co dev
git rebase master

# Delete a branch both locally and remotely
git branch -d mybranch # locally
git push origin :mybranch # remote
 
# When you get error path '...' is unmerged and you want to undo local changes
git reset foo/bar.txt
git checkout foo/bar.txt

# diff last commit
git diff HEAD^ HEAD
```

Virtual Box resize drive
------------------------
`VBoxManage modifyhd Win 7.vdi --resize 200000`

Django
------
#### South
- If you accidentally dropped a table:
  - python manage.py migrate app zero --fake
  - python manage.py migrate app


Shell Commands
--------------
#### sed
```
#the "-n" option will not print anything unless an explicit request to print is found
# use /p to only print the lines that match instead of the whole file
sed -n 's/pattern/repl/p' file   

# Use -i to modify the file in place
sed  -i 's/transaction_rest_api/transaction_api/' templates/finance/model_table.html templates/finance/transaction_list.html
```
#### Change all new line characters to commas. sed will not really work
> cat file | tr '\n' ','`


Markdown
--------
See this [gist](https://gist.github.com/conanfanli/6546498).

Vim
---

#### Compiling Vim with Python

`./configure --with-x --with-features=huge --enable-pythoninterp --with-python-config-dir=/usr/local/lib/python2.7/config  --enable-cscope --enable-gnome-check`

`make `

`sudo make install`

#### Vim commands:
- Show the mapping of a certain key: ``` :verbose imap <tab>```

Heroku
------
#### Procfile:

> web: python manage.py collectstatic --noinput --settings=barbarian.settings.prod; python manage.py run_gunicorn --pythonpath=/app/ --settings=barbarian.settings.prod 
 

see http://stackoverflow.com/questions/10527512/configuring-gunicorn-for-django-on-heroku.
If you don't use --settings, you may get an annoying import error. If you don do collectstatic, your static files won't be served. And you must do this in the Procfile instead of using "heroku run ..."

AngularJS
---------
- Get object keys in a loop: http://stackoverflow.com/questions/11985863/how-to-use-ng-repeat-for-dictionaries-in-angularjs
- handling $resource delete: Transaction.delete({transactionId: '123'}, success, failaure)

SSH
-----------
#### Generate keys 
```
# ssh
sh-keygen -t rsa #Generating public/private rsa key pair. 
#You can hit enter all the way
#Your identification has been saved in /home/jurn/.ssh/id_rsa Your public key has been saved in /home/jurn/.ssh/id_rsa.pub 
cd ~/.ssh
cat id_rsa.pub >> authorized_keys  
chmod 600 authorized_keys`
 
#now copy id_rsa to your client (your GUI box)
scp ./id_rsa hub@<GUI box ip>:       #do not forget the colon
 
#now log out from you devbox and use your GUI box
cd ~/.ssh
chmod 600 id_rsa    
#you should be able to ssh to your devbox without entering password now

###############################################################################################

# Redirect stderr to stdout and append output to a file
script.sh >> output.txt 2>&1
```

#### Reverse ssh
[Source](https://gist.github.com/conanfanli/7252902)

```
#!/bin/sh

date
cmd=ssh -nNT -R <secretport>:localhost:22 user@homebox

function status(){
pid=`cat ~/.con.sh.pid`
if [[ -n $pid ]] && [[ -n `ps $pid | tail -n +2` ]]
then
    echo Process is running
    return 1
else
    echo Process is NOT running
    return 0
fi
}

# switch user to the user name of your home box
function getpid(){
ps aux | grep "[u]er" | cut -b10-16
}

function stop(){
pid=`getpid`
echo will kill $pid
kill $pid
}

# switch workuser to the user name of dev box
function restart(){
if [[ `w | grep devuser` == "" ]]
    # when not connection from dev, kill it and start
then
    echo No dev user, will restart
    stop
    $cmd
else
    echo dev is connected, will not kill current process
fi
}

# To connect and port forward from home box
# ssh -D <newport> devuser@localhost -p <secretport>
```


MYSQL
-----
- Disable innodb:

```
[mysqld]
innodb=OFF
ignore-builtin-innodb
skip-innodb
default-storage-engine=myisam
default-tmp-storage-engine=myisam
```

