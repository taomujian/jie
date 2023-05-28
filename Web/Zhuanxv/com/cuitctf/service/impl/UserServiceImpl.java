package com.cuitctf.service.impl;

import com.cuitctf.dao.UserDao;
import com.cuitctf.po.User;
import com.cuitctf.service.UserService;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/* loaded from: UserServiceImpl.class */
public class UserServiceImpl implements UserService {
    private UserDao userDao;

    public UserDao gerUserDao() {
        return this.userDao;
    }

    public void setUserDao(UserDao userDao) {
        this.userDao = userDao;
    }

    @Override // com.cuitctf.service.UserService
    public List<User> findUserByName(String name) {
        return this.userDao.findUserByName(name);
    }

    @Override // com.cuitctf.service.UserService
    public List<User> loginCheck(String name, String password) {
        String name2 = name.replaceAll(" ", "").replaceAll("=", "");
        Pattern.compile("^[0-9a-zA-Z]+$").matcher(name2);
        Matcher password_matcher = Pattern.compile("^[0-9a-zA-Z]+$").matcher(password);
        if (password_matcher.find()) {
            return this.userDao.loginCheck(name2, password);
        }
        return null;
    }
}
