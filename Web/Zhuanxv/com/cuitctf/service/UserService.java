package com.cuitctf.service;

import com.cuitctf.po.User;
import java.util.List;

/* loaded from: UserService.class */
public interface UserService {
    List<User> findUserByName(String str);

    List<User> loginCheck(String str, String str2);
}
