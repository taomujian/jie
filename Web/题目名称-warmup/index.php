

<!doctype html>
<html>

<head>
    <meta charset="utf-8">
    <title>平平无奇的登陆界面</title>
</head>
<style type="text/css">
    body {
        margin: 0;
        padding: 0;
        font-family: sans-serif;
        background: url("static/background.jpg");
        /*背景图片自定义*/
        background-size: cover;
    }
    
    .box {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 400px;
        padding: 40px;
        background: rgba(0, 0, 0, .8);
        box-sizing: border-box;
        box-shadow: 0 15px 25px rgba(0, 0, 0, .5);
        border-radius: 10px;
        /*登录窗口边角圆滑*/
    }
    
    .box h2 {
        margin: 0 0 30px;
        padding: 0;
        color: #fff;
        text-align: center;
    }
    
    .box .inputBox {
        position: relative;
    }
    
    .box .inputBox input {
        width: 100%;
        padding: 10px 0;
        font-size: 16px;
        color: #fff;
        letter-spacing: 1px;
        margin-bottom: 30px;
        /*输入框设置*/
        border: none;
        border-bottom: 1px solid #fff;
        outline: none;
        background: transparent;
    }
    
    .box .inputBox label {
        position: absolute;
        top: 0;
        left: 0;
        padding: 10px 0;
        font-size: 16px;
        color: #fff;
        pointer-events: none;
        transition: .5s;
    }
    
    .box .inputBox input:focus~label,
    .box .inputBox input:valid~label {
        top: -18px;
        left: 0;
        color: #03a9f4;
        font-size: 12px;
    }
    
    .box input[type="submit"] {
        background: transparent;
        border: none;
        outline: none;
        color: #fff;
        background: #03a9f4;
        padding: 10px 20px;
        cursor: pointer;
        border-radius: 5px;
    }
</style>

<body>
    <div class="box">
        <h2>请登录</h2>
        <form method="post" action="index.php">
            <div class="inputBox">
                <input type="text" name="username" required="">
                <label>用户名</label>
            </div>
            <div class="inputBox">
                <input type="password" name="password" required="">
                <label>密码</label>
            </div>
            <input type="submit" name="" value="登录">
        </form>
    </div>
</body>

</html>

<?php
include 'conn.php';
include 'flag.php';


if (isset ($_COOKIE['last_login_info'])) {
    $last_login_info = unserialize (base64_decode ($_COOKIE['last_login_info']));
    try {
        if (is_array($last_login_info) && $last_login_info['ip'] != $_SERVER['REMOTE_ADDR']) {
            die('WAF info: your ip status has been changed, you are dangrous.');
        }
    } catch(Exception $e) {
        die('Error');
    }
} else {
    $cookie = base64_encode (serialize (array ( 'ip' => $_SERVER['REMOTE_ADDR']))) ;
    setcookie ('last_login_info', $cookie, time () + (86400 * 30));
}


if(isset($_POST['username']) && isset($_POST['password'])){
	$table = 'users';
	$username = addslashes($_POST['username']);
	$password = addslashes($_POST['password']);
	$sql = new SQL();
	$sql->connect();
	$sql->table = $table;
    $sql->username = $username;
    $sql->password = $password;
    $sql->check_login();
}


?>