<?php
// +----------------------------------------------------------------------
// | ThinkPHP [ WE CAN DO IT JUST THINK ]
// +----------------------------------------------------------------------
// | Copyright (c) 2006-2016 http://thinkphp.cn All rights reserved.
// +----------------------------------------------------------------------
// | Licensed ( http://www.apache.org/licenses/LICENSE-2.0 )
// +----------------------------------------------------------------------
// | Author: liu21st <liu21st@gmail.com>
// +----------------------------------------------------------------------

// [ 应用入口文件 ]

// 定义应用目录
define('APP_PATH', __DIR__ . '/../application/');
// 加载框架引导文件
require __DIR__ . '/../thinkphp/start.php';

if(isset($_GET["s"]))
{
    if($_SERVER["SERVER_NAME"] !== $_SERVER["REMOTE_ADDR"])
      {   echo "您的ip是".$_SERVER["REMOTE_ADDR"]."<hr/>"."本服务器的ip为127.0.0.1"."<hr/>"."这是一台内网机器，只接受本机请求"."<hr/>";
          die("sorry,you are not our people");
      }
}
