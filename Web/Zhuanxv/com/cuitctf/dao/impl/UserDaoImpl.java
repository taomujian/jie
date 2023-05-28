package com.cuitctf.dao.impl;

import com.cuitctf.dao.UserDao;
import com.cuitctf.po.User;
import java.util.List;
import org.springframework.orm.hibernate3.support.HibernateDaoSupport;

/* loaded from: UserDaoImpl.class */
public class UserDaoImpl extends HibernateDaoSupport implements UserDao {
    public List<User> findUserByName(String name) {
        return getHibernateTemplate().find("from User where name ='" + name + "'");
    }

    public List<User> loginCheck(String name, String password) {
        return getHibernateTemplate().find("from User where name ='" + name + "' and password = '" + password + "'");
    }
}
