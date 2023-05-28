# warmup

> 这是通过file参数来完成的

## 涉及函数

### mb_substr

> mb_substr(string $str, int $start[, int $length = NULL [, string $encoding = mb_internal_encoding() ]] ) : string

> mb_substr()函数返回字符串的一部分,之前我们学过 substr()函数,它只针对英文字符,如果要分割的中文文字则需要使用 mb_substr().如果start参数是负数且length小于或等于start,则length为0.

### mb_strpos

> mb_strpos(haystack, needle),返回要查找的字符串在别一个字符串中首次出现的位置,haystack是要被检查的字符串,needle是要搜索的字符串

## 思路分析

> 首先打开首页,查看源代码,发现source.php,访问获取源代码,分析代码得到要传入file参数,又看到hint.php,直接访问提示flag在ffffllllaaaagggg文件.代码重要的函数是mb_substr和mb_strpos,前者是截取字符串,后者是返回要查找的字符串在别一个字符串中首次出现的位置.截取出的字符串必须在白名单才能继续下去,mb_substr($_page, 0, mb_strpos($_page . '?', '?')就是来截取?前面的字符的,所以?前面得是source.php或者hint.php.然后就会返回true继续下去,代码中有urldecode,说明payload也是可以url编码,不过前面仍然得是source.php或者hint.php.满足if (! empty(\$_REQUEST['file']) && is_string($_REQUEST['file']) && emmm::checkFile(\$_REQUEST['file']))条件后到include的时候就可以使用../进行跨目录读取文件了

## payload

> source.php?../../../../../ffffllllaaaagggg

> hint.php?../../../../../ffffllllaaaagggg

> source.php%3f../../../../../ffffllllaaaagggg

## flag

> flag{25e7bce6005c4e0c983fb97297ac6e5a}