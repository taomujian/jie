# Nice_bgm

## MP3数据结构

```
typedef FrameHeader

{          //数字代表大小,单位bite
unsigned int sync:12;                        //同步信息
unsigned int version:2;                      //版本
unsigned int layer: 2;                           //层
unsigned int error protection:1;           // CRC校验
unsigned int bitrate_index:4;              //位率
unsigned int sampling_frequency:2;         //采样频率
unsigned int padding:1;                    //帧长调节
unsigned int private:1;                       //保留字
unsigned int mode:2;                         //声道模式
unsigned int mode extension:2;        //扩充模式
unsigned int copyright:1;                           // 版权
unsigned int original:1;                      //原版标志
unsigned int emphasis:2;                  //强调模式
}
```

> 帧长度是压缩时每一帧的长度,包括帧头的4个字节(32bit).它将填充的空位也计算在内.
padding的值会影响每一帧的长度（具体分析见下面的题目）

## 解题思路

> 下载附件得到一个mp3文件,用foremost分离出一个图片,图片没啥信息.用010 Editor打开mp3,发现private bit的数值的在0和1中变化,用脚本提取private bit信息得到flag.其实copyright也是在0和1中替换,多试几次得到flag

## flag

> flag{0k4_YOu_Seem_s0_cl3ver_t0_find_f1ag!}
