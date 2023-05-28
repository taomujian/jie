package com.cuitctf.action;

import com.opensymphony.xwork2.ActionSupport;
import java.io.InputStream;
import org.apache.struts2.ServletActionContext;

/* loaded from: DownloadAction.class */
public class DownloadAction extends ActionSupport {
    private String fileName;

    public InputStream getDownloadFile() throws Exception {
        return ServletActionContext.getServletContext().getResourceAsStream("/ctfpage/images/" + this.fileName);
    }

    public String execute() throws Exception {
        String suffix = this.fileName.substring(this.fileName.lastIndexOf(".") + 1);
        if (!suffix.equals("xml") && !suffix.equals("jpg") && !suffix.equals("class")) {
            return "suffix_error";
        }
        return "success";
    }

    public String getFileName() {
        return this.fileName;
    }

    public void setFileName(String fileName) {
        this.fileName = fileName;
    }
}
