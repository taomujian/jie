# Very_Luacky

## 解题思路

> 下载附件,给出的地址账号已经无法访问了.

> 承接Luaky的Writeup）关于第二个flag,并不知道每一轮会与哪一种类型的AI进行对战.所以使用最初的50手去识别AI的类型:Slime最好识别因为它总是有规律地改变自己的下一手;Alpaca也很容易识别只要你每次都只出0,这样它每次只会要么用上一手要么就是(last% 3,但永远不会是剩下的这一种情况.如果前两种都不是,那就知道在和Nozomi对战.

> 经过100轮后获得了第二个flag：hitcon{Got AC by r4nd() % 3! Nozomi p0wer chuunyuuuuu~ <3}

## flag

> hitcon{Got AC by r4nd() % 3! Nozomi p0wer chuunyuuuuu~ <3}