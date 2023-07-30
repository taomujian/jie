# Before running, modify your filename and add "DDH_instances = " at the beginning of the file.
load('/Users/taomujian/Desktop/project/jie/Crypto/DDH_Game/f59b06e8-8c70-4164-a1a6-bca330f67307/DDH_instances.sage')

# curve
p = 0x1a0111ea397fe69a4b1ba7b6434bacd764774b84f38512bf6730d2a0f6b0f6241eabfffeb153ffffb9feffffffffaaab
K = GF(p)
a = K(0x00)
b = K(0x04)
E = EllipticCurve(K, (a, b))
# G = E(0x17F1D3A73197D7942695638C4FA9AC0FC3688C4F9774B905A14E3A3F171BAC586C55E83FF97A1AEFFB3AF00ADB22C6BB, 0x08B3F481E3AAA0F1A09E30ED741D8AE4FCF5E095D5D00AF600DB18CB2C04B3EDD03CC744A2888AE40CAA232946C5E7E1)
E.set_order(0x73EDA753299D7D483339D80809A1D80553BDA402FFFE5BFEFFFFFFFF00000001 * 0x396C8C005555E1568C00AAAB0000AAAB)

G = E(3745324820672390389968901155878445437664963280229755729082200523555105705468830220374025474630687037635107257976475, 2578846078515277795052385204310204126349387494123866919108681393764788346607753607675088305233984015170544920715533)
n = G.order()

# Embedding degree of the curve
k = 12


def solve_ECDDHP(DDH_instances, G, Ep, m, n):
    """
    Parameters:
        DDH_instances - list consists of (aG, bG, cG), where aG, bG, cG are EC_point.xy()
        m - embedding degree of <G>
        n - G's order. 
    """
    sols = []
    
    Fpm.<x> = GF(p^m)
    Epm = Ep.base_extend(Fpm) 
    
    G = Epm(G)
    
    for ins in DDH_instances:
        aG, bG, cG = ins
        aG = Epm(aG); bG = Epm(bG); cG = Epm(cG)
        
        # e_aG_bG = aG.weil_pairing(bG, n)
        e_aG_bG = aG.tate_pairing(bG, n, m)
        
        e_G_cG = G.tate_pairing(cG, n, m)
        if e_aG_bG == e_G_cG:
            sols.append(True)
        else:
            sols.append(False)
    
    return sols

sols = solve_ECDDHP(DDH_instances, G, E, k, n)
# print(sols)

pt = 0
for i in range(len(sols)):
    pt += sols[i] * (2^i)

print(pt)