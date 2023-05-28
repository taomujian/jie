# easylaravel

## 思路分析

> 打开网站,查看源码,发现了源码地址,下载下来进行代码审计,发现登陆后note路由存在sql注入漏洞,以管理员身份登陆后可以访问flag路由获取flag,发现了管理员邮箱.重置管理员账号需要管理员邮箱和token,可以通过注入获取token

> 先注册一个账号,用户名是下面的payload,先确定列数,再使用联合注入获取token

```
test' order by 6#
test' union select 1,(select token from password_resets where email='admin@qvq.im'),3,4,5#
```

> 拿到token= 1dfde2e1f75253e07d05342d1e39819c126d76e5d96ac348255fd772829f93b0,接下来根据路由规则访问密码重置页,重置密码成功

> 直接访问flag后发现获取不了flag,这是因为laravel存在blade过期问题

> 在laravel中,模板文件是存放在resources/views中的,然后会被编译放到storage/framework/views中,而编译后的文件存在过期的判断.

> 在 Illuminate/View/Compilers/Compiler.php 中可以看到:

```
/**
 * Determine if the view at the given path is expired.
 *
 * @param  string  $path
 * @return bool
 */
public function isExpired($path)
{
    $compiled = $this->getCompiledPath($path);

    // If the compiled file doesn't exist we will indicate that the view is expired
    // so that it can be re-compiled. Else, we will verify the last modification
    // of the views is less than the modification times of the compiled views.
    if (! $this->files->exists($compiled)) {
        return true;
    }

    $lastModified = $this->files->lastModified($path);

    return $lastModified >= $this->files->lastModified($compiled);
}
```

> 过期时间是依据文件的最后修改时间来判断的,所以判断服务器上编译后的文件最后修改时间大于原本模板文件,那么怎么去删除(修改)编译后的文件?再来看看 UploadController 的上传：

```
public function upload(UploadRequest $request)
{
    $file = $request->file('file');
    if (($file && $file->isValid())) {
        $allowed_extensions = ["bmp", "jpg", "jpeg", "png", "gif"];
        $ext = $file->getClientOriginalExtension();
        if(in_array($ext, $allowed_extensions)){
            $file->move($this->path, $file->getClientOriginalName());
            Flash::success('上传成功');
            return redirect(route('upload'));
        }
    }
    Flash::error('上传失败');
    return redirect(route('upload'));
}
```

> 这里只能上传后缀为图片的文件,在UploadRequest中限制了文件必须为image,但是这个基本上是个摆设,很好绕过,可以看到文件是被上传到了$this->path,也就是storage/app/public

```
public function __construct()
{
    $this->middleware(['auth', 'admin']);
    $this->path = storage_path('app/public');
}
```

> 这个目录是没办法直接访问的,那么就算是能成功上传脚本文件也是没办法的,往下看还有两个方法

```
public function files()
{
    $files = array_except(Storage::allFiles('public'), ['0']);
    return view('files')->with('files', $files);
}

public function check(Request $request)
{
    $path = $request->input('path', $this->path);
    $filename = $request->input('filename', null);
    if($filename){
        if(!file_exists($path . $filename)){
            Flash::error('磁盘文件已删除,刷新文件列表');
        }else{
            Flash::success('文件有效');
        }
    }
    return redirect(route('files'));
}
```

> files是取出上传目录下的文件并展示,check方法检查文件是否仍存在于磁盘上,这里接收了两个参数path和filename,那么就相当于文件路径完全可控,但是这里只经过了file_exists,貌似没什么用,但是 file_exists中的参数完全可控,所以可以使用phar://协议来触发一次反序列化操作,这里看看swiftmailer/swiftmailer/lib/classes/Swift/ByteStream/TemporaryFileByteStream.php,swiftmailer是一个默认组件,用于邮件功能,跟入这个类看一下

```
class Swift_ByteStream_TemporaryFileByteStream extends Swift_ByteStream_FileByteStream
{
    public function __construct()
    {
        $filePath = tempnam(sys_get_temp_dir(), 'FileByteStream');

        if ($filePath === false) {
            throw new Swift_IoException('Failed to retrieve temporary file name.');
        }

        parent::__construct($filePath, true);
    }

    public function getContent()
    {
        if (($content = file_get_contents($this->getPath())) === false) {
            throw new Swift_IoException('Failed to get temporary file content.');
        }

        return $content;
    }

    public function __destruct()
    {
        if (file_exists($this->getPath())) {
            @unlink($this->getPath());
        }
    }
}
```

> 可以发现正是想要的文件删除,这里遇到一个问题,编译后文件的文件名不知道,这里跟入Illuminate/View/Compilers/Compiler.php

```
/**
 * Get the path to the compiled version of a view.
 *
 * @param  string  $path
 * @return string
 */
public function getCompiledPath($path)
{
    return $this->cachePath.'/'.sha1($path).'.php';
}
```

> 可以发现其实是基于路径的sha1值,但是服务器上的路径在哪儿呢,在使用管理员身份登录后,可以看到一条note,使用了nginx的默认配置,那么flag文件的完整路径就是/usr/share/nginx/html/resources/views/auth/flag.blade.php,经过sha1后得到34e41df0934a75437873264cd28e2d835bc38772.php

> 把exp用php打包成phar文件,然后上传1.gif,check的时候传入自定义的path和filename,然后访问/flag,得到flag

## flag

> flag{d64e4b06f672429682a96b11172a8938}

## 参考

> https://cloud.tencent.com/developer/article/1367783

> https://blog.csdn.net/Tel_milk/article/details/127979878