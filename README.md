# bulk-insert tool

# bulk insert tool Commands

## 1. db init
  - typer main.py run init dbname(default mysql)
```
>>> typer main.py run init mysql
host: localhost
port: 3306
user: root
password: root
db: cli_test
is your database correct?
url: localhost:3306/cli_test
id/pw: root/root
 [y/N]: y
connect success!!
```

## 2. db connection load
  - typer main.py run load
 ```
 >>> typer main.py run load
 ['mysql', 'localhost', '3306', 'root', 'root', 'cli_test']
 ```
 
## 3. sql
  - typer main.py run sql 'sql'
```
>>> typer main.py run sql 'select * from test'
(1439415, 668448884, 'lmhlx5inay84e5w87lxe', datetime.date(7846, 5, 28))
(1439416, 931464901, '1x1d475u0t1a3qpdhd6e', datetime.date(967, 6, 22))
(1439417, 1548848311, 'cty2kj18rl9oi7if4e3h', datetime.date(7217, 8, 12))
(1439418, 769572117, 'spvce7xx736i7yrle8qg', datetime.date(7974, 6, 21))
(1439419, 364382520, 'vghrbs7duwuvx4p02j0j', datetime.date(2401, 6, 13))
```

## 4. bulk insert
  - typer main.py run bulk 'table' --row 'insert row (default 1)'
```
>>> typer main.py run bulk test --row 10000
insert rows: 10000
```

### 4-1. bulk insert --rm option
  - typer main.py run bulk 'table' --row 'insert row' --rm
```
>>> typer main.py run bulk test --row 10000 --rm
delete rows: 10000
insert rows: 10000
```

# bulk-insert records check
```
>>> typer main.py run bulk test --row 10000 --rm
delete rows: 10000
insert rows: 10000

>>> typer main.py run sql 'select * from test limit 5'
```
<img width="599" alt="스크린샷 2023-02-23 오전 3 10 55" src="https://user-images.githubusercontent.com/72899707/220718366-e8d10320-b903-40a4-966e-be2ba86d5e0b.png">

# Caution

Supported DB: mysql, mariadb __(preparing postgresql)__

pk: pk only supports auto_increment.

Unique: Uniqueness is guaranteed only for the rows specified in the --row option. __(Only integer and varchar support unique)__
