import binascii


png_head = "89 50 4E 47 0D 0A 1A 0A 00 00 00 0D"
png_tail = "00 00 00 00 49 45 4E 44 AE 42 60 82"
idat = "49 44 41 54"
WIDTH, HEIGHT = 400, 400

def create_head():
    head = binascii.a2b_hex(''.join(png_head.split(" ")))
    ihdr = binascii.a2b_hex(''.join("49 48 44 52".split(" ")))
    width = WIDTH.to_bytes(4, byteorder="big")
    height = HEIGHT.to_bytes(4, byteorder="big")
    info = binascii.a2b_hex(''.join("08 02 00 00 00".split(" ")))
    crc32 = binascii.crc32(ihdr + width + height +
                           info).to_bytes(4, byteorder="big")
    return head + ihdr + width + height + info + crc32

def get_IDAT(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    length = len(data).to_bytes(4, byteorder="big")
    idat_head = binascii.a2b_hex(''.join(idat.split(" ")))
    crc32 = binascii.crc32(idat_head + data).to_bytes(4, byteorder="big")
    return length + idat_head + data + crc32

def create_tail():
    return binascii.a2b_hex(''.join(png_tail.split(" ")))


if __name__ == "__main__":
    head = create_head()
    tail = create_tail()

    all_idta = b""
    for file_path in ["8bece0fc07ab41d984363ba3474e2f4d/puzzle/yvxmeawg.data", "8bece0fc07ab41d984363ba3474e2f4d/puzzle/rnydeiho.data", "8bece0fc07ab41d984363ba3474e2f4d/puzzle/uozjmdnl.data", "8bece0fc07ab41d984363ba3474e2f4d/puzzle/fhnkotmb.data",
              "8bece0fc07ab41d984363ba3474e2f4d/puzzle/jlxphwfm.data", "8bece0fc07ab41d984363ba3474e2f4d/puzzle/yscijlzx.data", "8bece0fc07ab41d984363ba3474e2f4d/puzzle/ciaoxptf.data", "8bece0fc07ab41d984363ba3474e2f4d/puzzle/blczioav.data",
              "8bece0fc07ab41d984363ba3474e2f4d/puzzle/jtxsbevz.data", "8bece0fc07ab41d984363ba3474e2f4d/puzzle/lstjobzi.data", "8bece0fc07ab41d984363ba3474e2f4d/puzzle/pyusgabf.data", "8bece0fc07ab41d984363ba3474e2f4d/puzzle/wgkapjbh.data",
              "8bece0fc07ab41d984363ba3474e2f4d/puzzle/xufbyndk.data", "8bece0fc07ab41d984363ba3474e2f4d/puzzle/csizrgxn.data", "8bece0fc07ab41d984363ba3474e2f4d/puzzle/oaeqnubi.data", "8bece0fc07ab41d984363ba3474e2f4d/puzzle/gpiuezjw.data",
              "8bece0fc07ab41d984363ba3474e2f4d/puzzle/tihzkoyu.data", "8bece0fc07ab41d984363ba3474e2f4d/puzzle/hbctmwqj.data", "8bece0fc07ab41d984363ba3474e2f4d/puzzle/ycqzmbrw.data", "8bece0fc07ab41d984363ba3474e2f4d/puzzle/fkjhepcs.data",
              "8bece0fc07ab41d984363ba3474e2f4d/puzzle/kczwtlrd.data", "8bece0fc07ab41d984363ba3474e2f4d/puzzle/dwelszrk.data", "8bece0fc07ab41d984363ba3474e2f4d/puzzle/uilqywot.data", "8bece0fc07ab41d984363ba3474e2f4d/puzzle/xufnmacj.data",
              "8bece0fc07ab41d984363ba3474e2f4d/puzzle/jrbiznkl.data", "8bece0fc07ab41d984363ba3474e2f4d/puzzle/mrxtfkzj.data"]:
              all_idta += get_IDAT(file_path)

    with open("flag.png", "wb") as f:
        f.write(head + all_idta + tail)
