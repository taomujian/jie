*	éûUö
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Upload</title>
    <link rel="stylesheet" href="http://fortawesome.github.io/Font-Awesome/assets/font-awesome/css/font-awesome.css">
    <link rel="stylesheet" href="CSS/upload.css">

</head>

<body>
<div class="msg info" id="message">
    <i class="fa fa-info-circle"></i>please upload an IMAGE file (gif|jpg|jpeg|png)
</div>
<div class="container">
    <form action="?page=upload" method="post" enctype="multipart/form-data" class="form">
        <div class="file-upload-wrapper" id="file" data-text="Select an image!">
            <label for="file-upload"> <input name="file-upload-field" type="file" class="file-upload-field" value=""
                                             id="file-upload"></label>
        </div>
        <div class="div">
            <input class="button" type="submit" value="Upload Image" name="submit">
        </div>
    </form>

    <script src='http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>
    <script src="js/filename.js"></script>

</div>


</body>
</html>

<?php
error_reporting(0);

session_start();
if(isset($_GET['page'])){
    $page=$_GET['page'];
}else{
    $page=null;
}

if(preg_match('/\.\./',$page))
{
    echo "<div class=\"msg error\" id=\"message\">
    <i class=\"fa fa-exclamation-triangle\"></i>Attack Detected!</div>";
    die();
}

?>

<?php

if($page)
{
    if(!(include($page.'.php')))
    {
        echo "<div class=\"msg error\" id=\"message\">
    <i class=\"fa fa-exclamation-triangle\"></i>error!</div>";
        exit;
    }
}
?>