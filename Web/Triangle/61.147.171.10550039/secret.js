function enc_pw(e) {
    var _ = stoh(atob(getBase64Image("frei"))),
    t = 4096,
    r = 8192,
    m = 12288,
    R = new uc.Unicorn(uc.ARCH_ARM, uc.MODE_ARM);
    R.reg_write_i32(uc.ARM_REG_R8, r), 
    R.reg_write_i32(uc.ARM_REG_R9, m), 
    R.reg_write_i32(uc.ARM_REG_R10, e.length), 
    R.mem_map(t, 4096, uc.PROT_ALL);
    for (var a = 0; a < o2.length; a++) 
        R.mem_write(t + a, [_[o2[a]]]);
    R.mem_map(r, 4096, uc.PROT_ALL), 
    R.mem_write(r, stoh(e)), 
    R.mem_map(m, 4096, uc.PROT_ALL);
    var o = t,
    u = t + o2.length;
    return R.emu_start(o, u, 0, 0), htos(R.mem_read(m, e.length))
}

function get_pw() {
    for (var e = stoh(atob(getBase64Image("templar"))), _ = "", t = 0; t < o3.length; t++) 
        _ += String.fromCharCode(e[o3[t]]);
    return _
}

function test_pw(e, _) {
    var t = stoh(atob(getBase64Image("eye"))),
    r = 4096,
    m = 8192,
    R = 12288,
    a = new uc.Unicorn(uc.ARCH_ARM, uc.MODE_ARM);
    a.reg_write_i32(uc.ARM_REG_R9, m), 
    a.reg_write_i32(uc.ARM_REG_R10, R), 
    a.reg_write_i32(uc.ARM_REG_R8, _.length), 
    a.mem_map(r, 4096, uc.PROT_ALL);
    for (var o = 0; o < o1.length; o++) 
        a.mem_write(r + o, [t[o1[o]]]);
    a.mem_map(m, 4096, uc.PROT_ALL), 
    a.mem_write(m, stoh(_)), 
    a.mem_map(R, 4096, uc.PROT_ALL), 
    a.mem_write(R, stoh(e));
    var u = r,
    c = r + o1.length;
    return a.emu_start(u, c, 0, 0), a.reg_read_i32(uc.ARM_REG_R5)
}

function login() {
    var input = document.getElementById('password').value;
    var enc = enc_pw(input);
    var pw = get_pw();
    if (test_pw(enc, pw) == 1) {
        alert('Well done!');
    } else {
        alert('Try again ...');
    }
}

var pw = get_pw()
console.log(pw)
