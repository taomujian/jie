<?php

class xctf{
    public $flag = '111';
    public function __wakeup(){
    exit('bad requests');
    }
}

$a = new xctf();
$b = serialize($a);
echo $b;
?>