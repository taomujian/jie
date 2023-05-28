package com.cuitctf.action;

import com.cuitctf.po.User;
import com.cuitctf.service.UserService;
import com.cuitctf.util.InitApplicationContext;
import com.opensymphony.xwork2.ActionContext;
import com.opensymphony.xwork2.ActionSupport;
import java.util.List;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import org.springframework.context.ApplicationContext;

/* loaded from: UserLoginAction.class */
public class UserLoginAction extends ActionSupport {
    private UserService userService;
    private User user;

    public UserLoginAction() {
        ApplicationContext context = InitApplicationContext.getApplicationContext();
        this.userService = (UserService) context.getBean("userService");
    }

    public String execute() throws Exception {
        System.out.println("start:" + this.user.getName());
        ActionContext actionContext = ActionContext.getContext();
        Map<String, Object> request = (Map) actionContext.get("request");
        try {
            if (!userCheck(this.user)) {
                request.put("error", "登录失败，请检查用户名和密码");
                System.out.println("登陆失败");
                return "error";
            }
            System.out.println("login SUCCESS");
            ActionContext.getContext().getSession().put("user", this.user);
            return "success";
        } catch (Exception e) {
            e.printStackTrace();
            throw e;
        }
    }

    public boolean isValid(String username) {
        return matcher("[a-zA-Z0-9]{1-16}", username);
    }

    private static boolean matcher(String reg, String string) {
        Pattern pattern = Pattern.compile(reg);
        Matcher matcher = pattern.matcher(string);
        boolean tem = matcher.matches();
        return tem;
    }

    public boolean userCheck(User user) {
        List<User> userList = this.userService.loginCheck(user.getName(), user.getPassword());
        if (userList != null && userList.size() == 1) {
            return true;
        }
        addActionError("Username or password is Wrong, please check!");
        return false;
    }

    public UserService getUserService() {
        return this.userService;
    }

    public void setUserService(UserService userService) {
        this.userService = userService;
    }

    public User getUser() {
        return this.user;
    }

    public void setUser(User user) {
        this.user = user;
    }
}
