<?php

namespace app\index\controller;

use think\Controller;
use think\Db;
use think\Request;
use think\Validate;

class Userinfo extends Controller
{
    public function user(Request $request)
    {
        $session = $request->session('username');
        if($session === 'admin')
        {
            return view('user',['info'=>'welcome admin!!','flag'=>'This is your hint:   <br>hint{xxxxxxxxxx}']);
        }
        else{
            return view('user',['info'=>"hello {$session}",'flag'=>'This is your hint:   <br>flag{}<br>maybe the admin have some hints:)']);
        }
    }

    public function change()
    {
        return view();
    }

    public function changeinfo(Request $request)
    {
        $dbuser ='*****';
        $dbpass ='*****';
        $dbname ="study";
        $host = 'localhost';
        @error_reporting(0);
        @$con = mysqli_connect($host,$dbuser,$dbpass,$con);
        // Check connection
        if (!$con)
        {
            echo "Failed to connect to MySQL: " . mysqli_error();
        }
        @mysqli_select_db($con,$dbname) or die ( "Unable to connect to the database: $dbname");


        $post = $request->post();
        $username = $request->session('username');
        $pass = $post['password'];
        $curr_pass = $post['current_password'];
        $validate = Validate::make(['password'=>'min:3|confirm']);
        $status = $validate->check($post);
        if($status){
            if (preg_match("/select|update|delete|insert|into|set|;|between|regexp|like|rlike|=|substr|mid|ascii|join|char|order|count|rand|floor|group|extractvalue|updatexml|exp|concat|outfile|\(|\)/i", $curr_pass) || preg_match("/select|update|delete|insert|into|set|;|between|regexp|like|rlike|=|substr|mid|ascii|join|char|order|count|rand|floor|group|extractvalue|updatexml|exp|concat|outfile|\(|\)/i", $pass)) {
            $this->success('go out!! hacker','/xinan/public/index/index/index');
            } else {
                $sql = "UPDATE users SET PASSWORD='$pass' where username='$username' and password='$curr_pass' ";
                $res = mysqli_query($con,$sql) or die('You tried to be smart, Try harder!!!! :( ');
                $row = mysqli_affected_rows();
                if($row = 1){
                    $this->success('修改成功啦','/xinan/public/index/login/index');
                }else {
                    $this->error('修改失败，请联系管理员');
                }
            }
        }else{
            $this->error($validate->getError());
        }
    }
}
