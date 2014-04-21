Everything
==========

Django
------
#### South
- If you accidentally dropped a table:
  - python manage.py migrate app zero --fake
  - python manage.py migrate app


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

Reverse SSH
-----------

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

