<?php
class AES_key{
    private $pi = "6.2831853174";


    public function getChars(){
        $CharsList = array();
        for ($i=1; $i<=26; $i++){
            array_push($CharsList,chr(96+$i));

        }


        return $CharsList;
    }


    public function getPiChars(){
        $nPai = $this->pi;
        $CharsList = $this->getChars();
        $nPai = str_replace(".", "", $nPai);
        $nPaiArray = str_split($nPai);
        $PiCharsList = array();


        for ($i=0; $i<=count($nPaiArray); $i++){
            array_push($PiCharsList, $CharsList[$nPaiArray[$i]]);
        }


        return implode("",$PiCharsList);
    }


    public function aaa(int $n){
        return $n % 5;
    }


    public function bbb(int $n){
        $s = ($n+1)*($n-1) % 5;
        $s = $s + $n*4%3;
        $s = $s + $n/4*3;
        $s = $this->aaa(314) / ($s%5*$n+7) + 5;


        return $s;
    }

    public function ccc(int $n){
        $k = 3;
        $CharsList = $this->getChars();
        $PadCharsList = array();
        for ($i=0; $i< $n*$k; $i=$i+$k){
            array_push($PadCharsList, $CharsList[$i]);
        }


        return implode('',$PadCharsList);
    }


}

class AES_enc{
/*
 * 加密算法：AES
 * 加密模式：CBC
 * 填充模式：PKCS7Padding
 * */
    private $cipher;

    public function __construct(string $data){
        $this->setCipher($this->encAES($data));
    }

    public function encAES(string $data){
        $s = new AES_key;
        $key = $s->getPiChars().$s->ccc($s->bbb(2568));
        $iv = substr(md5($key), 0, 16);
        //$enc = openssl_encrypt($data, $mod, $key, 1, $iv);
        return base64_encode($enc);
    }


    public function getCipher(){
        return $this->cipher;
    }


    public function setCipher($cipher){
        $this->cipher = $cipher;
    }
}