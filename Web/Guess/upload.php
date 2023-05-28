

<?php
error_reporting(0);
function show_error_message($message)
{
    die("<div class=\"msg error\" id=\"message\">
    <i class=\"fa fa-exclamation-triangle\"></i>$message</div>");
}

function show_message($message)
{
    echo("<div class=\"msg success\" id=\"message\">
    <i class=\"fa fa-exclamation-triangle\"></i>$message</div>");
}

function random_str($length = "32")
{
    $set = array("a", "A", "b", "B", "c", "C", "d", "D", "e", "E", "f", "F",
        "g", "G", "h", "H", "i", "I", "j", "J", "k", "K", "l", "L",
        "m", "M", "n", "N", "o", "O", "p", "P", "q", "Q", "r", "R",
        "s", "S", "t", "T", "u", "U", "v", "V", "w", "W", "x", "X",
        "y", "Y", "z", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9");
    $str = '';

    for ($i = 1; $i <= $length; ++$i) {
        $ch = mt_rand(0, count($set) - 1);
        $str .= $set[$ch];
    }

    return $str;
}

session_start();



$reg='/gif|jpg|jpeg|png/';
if (isset($_POST['submit'])) {

    $seed = rand(0,999999999);
    mt_srand($seed);
    $ss = mt_rand();
    $hash = md5(session_id() . $ss);
    setcookie('SESSI0N', $hash, time() + 3600);

    if ($_FILES["file"]["error"] > 0) {
        show_error_message("Upload ERROR. Return Code: " . $_FILES["file-upload-field"]["error"]);
    }
    $check2 = ((($_FILES["file-upload-field"]["type"] == "image/gif")
            || ($_FILES["file-upload-field"]["type"] == "image/jpeg")
            || ($_FILES["file-upload-field"]["type"] == "image/pjpeg")
            || ($_FILES["file-upload-field"]["type"] == "image/png"))
        && ($_FILES["file-upload-field"]["size"] < 204800));
    $check3=!preg_match($reg,pathinfo($_FILES['file-upload-field']['name'], PATHINFO_EXTENSION));


    if ($check3) show_error_message("Nope!");
    if ($check2) {
        $filename = './uP1O4Ds/' . random_str() . '_' . $_FILES['file-upload-field']['name'];
        if (move_uploaded_file($_FILES['file-upload-field']['tmp_name'], $filename)) {
            show_message("Upload successfully. File type:" . $_FILES["file-upload-field"]["type"]);
        } else show_error_message("Something wrong with the upload...");
    } else {
        show_error_message("only allow gif/jpeg/png files smaller than 200kb!");
    }
}
?>