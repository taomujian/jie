<?php

class master
{
	private $path;
	private $name;
	
	function __construct()
	{
		
	}
	
	function stream_open($path)
	{
		if(!preg_match('/(.*)\/(.*)$/s',$path,$array,0,9))
			return 1;
		$a=$array[1];
		parse_str($array[2],$array);
		
		if(isset($array['path']))
		{
			$this->path=$array['path'];
		}
		else
			return 1;
		if(isset($array['name']))
		{
			$this->name=$array['name'];
		}
		else
			return 1;
		
		if($a==='upload')
		{
			return $this->upload($this->path,$this->name);
		}
		elseif($a==='search')
		{
			return $this->search($this->path,$this->name);
		}
		else 
			return 1;
	}
	function upload($path,$name)
	{
		if(!preg_match('/^uploads\/[a-z]{10}\/$/is',$path)||empty($_FILES[$name]['tmp_name']))
			return 1;
		
		$filename=$_FILES[$name]['name'];
		echo $filename;
		
		$file=file_get_contents($_FILES[$name]['tmp_name']);
		
		$file=str_replace('<','!',$file);
		$file=str_replace(urldecode('%03'),'!',$file);
		$file=str_replace('"','!',$file);
		$file=str_replace("'",'!',$file);
		$file=str_replace('.','!',$file);
		if(preg_match('/file:|http|pre|etc/is',$file))
		{
			echo 'illegalbbbbbb!';
			return 1;
		}
		
		file_put_contents($path.$filename,$file);
		file_put_contents($path.'user.jpg',$file);
		
		
		echo 'upload success!';
		return 1;
	}
	function search($path,$name)
	{
		if(!is_dir($path))
		{
			echo 'illegal!';
			return 1;
		}
		$files=scandir($path);
		echo '</br>';
		foreach($files as $k=>$v)
		{
			if(str_ireplace($name,'',$v)!==$v)
			{
				echo $v.'</br>';
			}
		}
		
		return 1;
	}
	
	function stream_eof()
	{
		return true;
	}
	function stream_read()
	{
		return '';
	}
	function stream_stat()
	{
		return '';
	}
	
}

stream_wrapper_unregister('php');
stream_wrapper_unregister('phar');
stream_wrapper_unregister('zip');
stream_wrapper_register('master','master');

?>