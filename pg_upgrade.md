**TL;DR**

https://medium.com/@tk512/upgrading-postgresql-from-9-3-to-9-4-on-ubuntu-14-04-lts-2b4ddcd26535#.ykg7kfkhu
```bash
sudo pg_dropcluster 9.4 main --stop
sudo pg_upgradecluster 9.3 main
sudo pg_dropcluster 9.3 main
```

---

While upgrading Ubuntu 14.04 to 14.10, I got the following message:

> The PostgreSQL version 9.3 is obsolete, but the server or client packages are still installed. Please install the latest packages (postgresql-9.4 and postgresql-client-9.4) and upgrade the existing clusters with pg_upgradecluster

Once the Ubuntu upgrade finished, I used `aptitude search` to check which versions of postgres I have installed. 

```
i   postgresql                                                        - object-relational SQL database (supported version)
i A postgresql-9.3                                                    - object-relational SQL database, version 9.3 server
i A postgresql-9.4                                                    - object-relational SQL database, version 9.4 server
i A postgresql-client-9.3                                             - front-end programs for PostgreSQL 9.3
i A postgresql-client-9.4                                             - front-end programs for PostgreSQL 9.4
i A postgresql-contrib-9.3                                            - additional facilities for PostgreSQL
i A postgresql-contrib-9.4                                            - additional facilities for PostgreSQL
```

Looks like the Ubuntu upgrade included PostgreSQL 9.4, but I still need to upgrade from 9.3 to 9.4.

Run `pg_lsclusters`, your 9.3 and 9.4 main clusters should be "online".

```
pg_lsclusters 
Ver Cluster Port Status Owner    Data directory               Log file
9.3 main    5432 online postgres /var/lib/postgresql/9.3/main /var/log/postgresql/postgresql-9.3-main.log
9.4 main    5433 online postgres /var/lib/postgresql/9.4/main /var/log/postgresql/postgresql-9.4-main.log
```

There already is a cluster "main" for 9.4 (since this is created by default on package installation).
This is done so that a fresh installation works out of the box without the need to create a cluster first,
but of course it clashes when you try to upgrade 9.3/main when 9.4/main also exists.
The recommended procedure is to remove the 9.4 cluster with `pg_dropcluster` and then upgrade with `pg_upgradecluster`.

Stop the 9.4 cluster and drop it.

```bash
sudo pg_dropcluster 9.4 main --stop
```

Upgrade the 9.3 cluster to the latest version.

```bash
sudo pg_upgradecluster 9.3 main
```

Your 9.3 cluster should now be "down".

```
pg_lsclusters 
Ver Cluster Port Status Owner    Data directory               Log file
9.3 main    5433 down   postgres /var/lib/postgresql/9.3/main /var/log/postgresql/postgresql-9.3-main.log
9.4 main    5432 online postgres /var/lib/postgresql/9.4/main /var/log/postgresql/postgresql-9.4-main.log
```

Check that the upgraded cluster works, then remove the 9.3 cluster.

```bash
sudo pg_dropcluster 9.3 main
```
