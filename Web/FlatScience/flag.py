
import os
import io
import re
import hashlib
import requests
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

def download_pdf(url):
    # 跟据不同网站pdf存放的目录进行修改
    re1 = '[a-fA-F0-9]{32,32}.pdf'
    re2 = '[0-9\/]{2,2}index.html'
    print(url)
    req = requests.get(url).text
    re_1 = re.findall(re1,req)
    for i in re_1:
        os.system('wget '+ url + i)
    re_2 = re.findall(re2,req)
    for j in re_2:
        new_url = url+j[0:2]
        get_pdf(new_url)

def get_pdf():
    return [i for i in os.listdir("./") if i.endswith("pdf")]

def convert_pdf_2_text(path):
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    device = TextConverter(rsrcmgr, retstr, codec='utf-8', laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    with open(path, 'rb') as fp:
        for page in PDFPage.get_pages(fp, set()):
            interpreter.process_page(page)
        text = retstr.getvalue()
    device.close()
    retstr.close()
    return text
 
 
def find_password():
    download_pdf('http://61.147.171.105:60170/')
    pdf_path = get_pdf()
    for i in pdf_path:
        print("Searching word in " + i)
        pdf_text = convert_pdf_2_text(i).split(" ")
        for word in pdf_text:
            sha1_password = hashlib.sha1(word+"Salz!").hexdigest()
            if sha1_password == '3fab54a50e770d830c0416df817567662a9dc85c':
                print("Find the password :" + word)
                exit()
 
if __name__ == "__main__":
    find_password()