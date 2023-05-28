# SECCON 2016: biscuiti

## challenge description
**source:** [ctftime](https://ctftime.org/task/3176)
**Category:** Web, Crypto
**Points:** 300
**Description:** 

> Can you login as admin?
>
> http://biscuiti.pwn.seccon.jp/
>
> [biscuiti.zip](http://files.quals.seccon.jp/biscuiti.zip)

## setup local environment
### 1. pull images
`docker pull sysucsa/ctfs_docker:seccon2016_web_biscuiti`
### 2. run it
`docker run -d -p 8000:80 sysucsa/ctfs_docker:seccon2016_web_biscuiti
`

then access `http://127.0.0.1:8000`, you will see a login form.

## write-up
https://github.com/ssst0n3/ctf-wp/tree/master/2016/seccon/WEB/biscuiti
