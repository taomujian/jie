import dpkt

# 打开pcap文件
with open('Basic-06.pcapng', 'rb') as file:
    # 创建一个pcap reader对象
    pcap_reader = dpkt.pcap.Reader(file)

    # 遍历每个数据包
    for ts, buf in pcap_reader:
        # 解析数据包
        eth = dpkt.ethernet.Ethernet(buf)
        ip = eth.data
        if isinstance(ip, dpkt.ip.IP):
            tcp = ip.data
            if isinstance(tcp, dpkt.tcp.TCP):
                # 获取TCP层的原始数据
                raw_data = tcp.data

                # 打印原始数据
                print(raw_data)

# 关闭pcap文件
file.close()
