<?php

namespace app\index\controller;

use think\Controller;
use think\Db;
use think\Request;
use think\Validate;

class Login extends Controller
{
    public function index()
    {
        return view();
    }

    public function login(Request $request)
    {
    	$dbuser ='*****';
        $dbpass ='*****';
        $dbname ="study";
        $host = 'localhost';
        @error_reporting(0);
        @$con = mysqli_connect($host,$dbuser,$dbpass,$dbname);
        // Check connection
        if (!$con)
        {
            echo "Failed to connect to MySQL: " . mysqli_error();
        }
        @mysqli_select_db($con,$dbname) or die ( "Unable to connect to the database: $dbname");
        $post = $request->post();
        $username = mysqli_real_escape_string($con,$post["username"]);
        $password = mysqli_real_escape_string($con,$post["password"]);


        if (preg_match("/select|update|delete|insert|into|set|;|between|regexp|like|rlike|=|substr|mid|ascii|join|char|order|count|rand|floor|group|extractvalue|updatexml|exp|concat|outfile|\(|\)/i", $username) || preg_match("/select|update|delete|insert|into|set|;|between|regexp|like|rlike|=|substr|mid|ascii|join|char|order|count|rand|floor|group|extractvalue|updatexml|exp|concat|outfile|\(|\)/i", $password)) {
            $this->success('go out!! hacker','/xinan/public/index/index/index');
        } else {
            $sql = "SELECT * FROM users WHERE username='$username' and password='$password'";
            $res = mysqli_query($con,$sql) or die('ERROR :(');
            $row = mysqli_fetch_row($res);
            if($row[1]){
            	//var_dump($row);
                cookie('username',$post['username']);
                session('uid',$row[0]);
                session('username',$post['username']);

                $this->success('登陆成功','/xinan/public/index/index/index');
            }else{
                return "<script>alert('账号或密码错误，请重试');window.location.href='/xinan/public/index/login/index'; </script>";
            }
        }
    }

    public function logout()
    {
        session('uid',null);
        session('username',null);
        cookie(null);
        return "<script>alert('已退出登陆');window.location.href='/xinan/public/index/index/index'; </script>";
    }
}



