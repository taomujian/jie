<?php
include "lib.php";
include "config.php";
error_reporting(0);

function waf($password){
    return $password;
}

$username = $_POST["Username"];
$password = $_POST["Password"];

if (isset($username)&&isset($password)) {
    $data = $db->querySingle("SELECT * FROM users WHERE username='${username}'and password='$password).'", true);
    $host = str_replace(' ', '', $data['host']);
    $port = (int) $data['port'];
    print_r($port);
} else {
    $resp ="Invalid username or password";
    echo $json_resp;
}
?>