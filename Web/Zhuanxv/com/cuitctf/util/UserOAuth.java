package com.cuitctf.util;

import com.opensymphony.xwork2.ActionContext;
import com.opensymphony.xwork2.ActionInvocation;
import com.opensymphony.xwork2.interceptor.AbstractInterceptor;
import java.util.Map;

/* loaded from: UserOAuth.class */
public class UserOAuth extends AbstractInterceptor {
    public String intercept(ActionInvocation invocation) throws Exception {
        Map session = invocation.getInvocationContext().getSession();
        Object userName = session.get("user");
        if (userName == null) {
            ActionContext actionContext = ActionContext.getContext();
            Map<String, Object> request = (Map) actionContext.get("request");
            request.put("error", "请先登录");
            return "login_error";
        }
        return invocation.invoke();
    }
}
