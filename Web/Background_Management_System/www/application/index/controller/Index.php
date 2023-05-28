<?php
namespace app\index\controller;

use app\common\model\Users;
use think\Controller;
use think\Db;
use think\Request;

class Index extends Controller
{
    public function index()
    {
        return view('index');
    }

}
