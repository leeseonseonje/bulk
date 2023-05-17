# bulk-insert tool

# bulk insert tool Commands

## 1. db init
  - python main.py init dbname(default mysql)
```
>>> python main.py init mysql
host: localhost
port: 3306
user: root
password: root
db: cli_test
connect success!!
```

## 2. db connection load
  - python main.py load
```
 >>> python main.py load
 dbms: mysql
 host/port: localhost/3306
 user/password: root/root
 db: cli_test
```
 
## 3. sql
  - python main.py sql 'sql'
```
>>> typer main.py run sql 'select * from test order by id desc limit 10'
count: 10
(377632490, 1907334006, 'jixv7pw6matwxuijtudq', datetime.date(1991, 1, 14))
(377632489, 394097271, 'rkmvoejjrmpjn2ynaiu5', datetime.date(1987, 12, 16))
(377632488, 978318389, 'xzbdwn2j8dopbplm6mf8', datetime.date(1979, 1, 13))
(377632487, 802074465, 'nxp7nwh0ewvc9ec9005g', datetime.date(1985, 8, 13))
(377632486, 1899704016, 'jvrhmtryzseijnc6605l', datetime.date(1987, 1, 17))
(377632485, 554525884, '4r6mienmorq240on0bcu', datetime.date(1989, 10, 1))
(377632484, 552641192,'wglq3gxpn2kftrokpr3x', datetime.date(1994, 10, 4))
(377632483, 1831062817, '588oxop57rxjtt2a7hmx', datetime.date(2001, 8, 2))
(377632482, 541219314, 'ae1os464262bk4pknhv3', datetime.date(2001, 2, 15))
(377632481, 1839120451, 'vvbwc70ygn7fsx8ql9w3', datetime.date(1992, 4, 22))
```

## 4. bulk insert
  - python main.py bulk 'table' --row 'insert row (default 1)'
```
>>> python main.py bulk test --row 100000
working time: 0:00:01.796998
```

### 4-1. options

#### --ran
  - Generate random values (guaranteed unique x)
  
  ___ex) python main.py bulk 'table' --row 100000 --ran___
  
# Caution

Supported DB: mysql, mariadb __(preparing postgresql)__

pk: pk only supports auto_increment.
