package com.cuitctf.action;

import com.opensymphony.xwork2.ActionContext;
import com.opensymphony.xwork2.ActionSupport;
import java.io.File;
import java.util.ArrayList;
import java.util.Map;

/* loaded from: AdminAction.class */
public class AdminAction extends ActionSupport {
    private String pathName;

    public String execute() throws Exception {
        if (this.pathName == null) {
            return "list_error";
        }
        travelDirectory(this.pathName);
        return "success";
    }

    public void setPathName(String pathName) {
        this.pathName = pathName;
    }

    public void travelDirectory(String directory) {
        ArrayList arrayList = new ArrayList();
        File dir = new File(directory);
        if (dir.isFile()) {
            return;
        }
        File[] files = dir.listFiles();
        ActionContext actionContext = ActionContext.getContext();
        Map<String, Object> request = (Map) actionContext.get("request");
        if (files != null) {
            for (int i = 0; i < files.length; i++) {
                arrayList.add(files[i].getName());
                System.out.println(files[i].getName());
            }
            request.put("fileList", arrayList);
            return;
        }
        System.out.println("目录错误");
        request.put("error", "目录输入错误");
    }
}
