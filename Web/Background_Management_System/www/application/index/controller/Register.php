<?php

namespace app\index\controller;

use think\Controller;
use think\Db;
use think\Request;
use think\Validate;

class Register extends Controller
{
    public function create()
    {
        //halt('hello');
        return view();
    }

    public function add(Request $request)
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
        $validate = Validate::make(['password'=>'require|min:3|max:40|confirm','username'=>'require|min:3|max:40']);
        $status = $validate->check($post);
        $username=  $post['username'];
        $pass= mysqli_real_escape_string($con,$post['password']);
        if($status) {
            if (preg_match("/select|update|delete|insert|into|set|;|between|regexp|like|rlike|=|substr|mid|ascii|join|char|order|count|rand|floor|group|extractvalue|updatexml|exp|concat|outfile|\(|\)/i", $username) || preg_match("/select|update|delete|insert|into|set|;|between|regexp|like|rlike|=|substr|mid|ascii|join|char|order|count|rand|floor|group|extractvalue|updatexml|exp|concat|outfile|\(|\)/i", $pass)) {
            $this->success('go out!! hacker','/xinan/public/index/index/index');
        } else {
                $relogin = Db::table('users')->where('username',$post['username'])->find();
                if ($relogin){
                    return "<script>alert('该用户名已被注册');window.location.href='/xinan/public/index/register/create'; </script>";
                }else{
                    $sql = "insert into users ( username, password) values(\"$username\", \"$pass\")";
                    $result = mysqli_query($con,"insert into users ( username, password) values(\"$username\", \"$pass\")") or die('Error Creating your user account,  : '.mysqli_error());
                    if($result){
                        $this->success('注册成功 快去登陆吧','/xinan/public/index/login/index');
                    }else{
                        $this->error('注册失败，请联系管理员');
                    }
                }
            }
        }
        else{
            $this->error($validate->getError());
        }
    }
}
