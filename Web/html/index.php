<!DOCTYPE html>
<html>
<!-- Head -->
<head>
<title>Login</title>
<meta name="keywords" content="Login"/>
<!-- Meta-Tags -->
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<script type="application/x-javascript"> addEventListener("load", function() { setTimeout(hideURLbar, 0); }, false); function hideURLbar(){ window.scrollTo(0,1); } </script>
<!-- //Meta-Tags -->

<link href="css/popuo-box.css"  rel="stylesheet" type="text/css" media="all" />

<!-- Style --> <link rel="stylesheet" href="css/style.css"  type="text/css" media="all">


</head>
<!-- //Head -->

<!-- Body -->
<body>

    <h1>获取端口系统</h1>

    <div class="w3layoutscontaineragileits">
    <h2>Login here</h2>
        <form action="login.php" method="post">
            <input type="text" Name="Username" placeholder="Username" required>
            <input type="password" Name="Password" placeholder="PASSWORD" required>
            <ul class="agileinfotickwthree">
                <li>
                    <input type="checkbox" id="brand1" value="">
                    <label for="brand1"><span></span>Remember me</label>
                    <a href="#">Forgot password?</a>
                </li>
            </ul>
            <div class="aitssendbuttonw3ls">
                <input type="submit" value="LOGIN">
                <p> To register new account <span>→</span> <a class="w3_play_icon1" href="#small-dialog1"> Click Here</a></p>
                <div class="clear"></div>
            </div>
        </form>
    </div>
    
    <!-- for register popup -->
    <div id="small-dialog1" class="mfp-hide">
        <div class="contact-form1">
            <div class="contact-w3-agileits">
                <h3>Register Form</h3>
                <form action="#" method="post">
                        <div class="form-sub-w3ls">
                            <input placeholder="User Name"  type="text" required>
                            <div class="icon-agile">
                                <i class="fa fa-user" aria-hidden="true"></i>
                            </div>
                        </div>
                        <div class="form-sub-w3ls">
                            <input placeholder="Email" class="mail" type="email" required>
                            <div class="icon-agile">
                                <i class="fa fa-envelope-o" aria-hidden="true"></i>
                            </div>
                        </div>
                        <div class="form-sub-w3ls">
                            <input placeholder="Password"  type="password" required>
                            <div class="icon-agile">
                                <i class="fa fa-unlock-alt" aria-hidden="true"></i>
                            </div>
                        </div>
                        <div class="form-sub-w3ls">
                            <input placeholder="Confirm Password"  type="password" required>
                            <div class="icon-agile">
                                <i class="fa fa-unlock-alt" aria-hidden="true"></i>
                            </div>
                        </div>
                    <div class="login-check">
                         <label class="checkbox"><input type="checkbox" name="checkbox" checked="">I Accept Terms & Conditions</label>
                    </div>
                    <div class="submit-w3l">
                        <input type="submit" value="Register">
                    </div>
                </form>
            </div>
        </div>  
    </div>
    <!-- //for register popup -->
    <div class="w3footeragile">
        <p> &copy; 2048 获取端口系统. All Rights Reserved | Design by <a href="#">xxxxx</a></p>
    </div>

    
    <script type="text/javascript" src="js/jquery-2.1.4.min.js" ></script>

    <!-- pop-up-box-js-file -->  
        <script src="js/jquery.magnific-popup.js"  type="text/javascript"></script>
    <!--//pop-up-box-js-file -->
    <script>
        $(document).ready(function() {
        $('.w3_play_icon,.w3_play_icon1,.w3_play_icon2').magnificPopup({
            type: 'inline',
            fixedContentPos: false,
            fixedBgPos: true,
            overflowY: 'auto',
            closeBtnInside: true,
            preloader: false,
            midClick: true,
            removalDelay: 300,
            mainClass: 'my-mfp-zoom-in'
        });
                                                                        
        });
    </script>

</body>
<!-- //Body -->

</html>