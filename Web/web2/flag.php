<?php
$miwen="a1zLbgQsCESEIqRLwuQAyMwLyq2L5VwBxqGA3RQAyumZ0tmMvSGM2ZwB4tws";

function encode($str){
    $_o=strrev($str);
    $_ = '';
    // echo $_o;

    for($_0=0;$_0<strlen($_o);$_0++){

        $_c=substr($_o,$_0,1);
        $__=ord($_c)+1;
        $_c=chr($__);
        $_= $_.$_c;   
    } 
    return str_rot13(strrev(base64_encode($_)));
}

function decode($str){
    $str = str_rot13($str);
    $_o = strrev($str);
    $_o = base64_decode($_o);
    $_ = '';

    for($_0=1;$_0<strlen($_o);$_0++){
        $_c=substr($_o,$_0,1);
        $__=ord($_c)-1;
        $_c=chr($__);
        $_= $_.$_c;
    }

    return strrev($_);
}

echo decode($miwen)
?>