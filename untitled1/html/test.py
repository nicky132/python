import urllib.request
import re
import xlwt

def getHtml();
     response = urllib.request.urlopen("http://www.tmall.com")
     return response.read().decode("utf-8")

def getContent(html)
    return re.findall('<a href="(.+?)">(.+?)</a>',html)
def writeToXLS(content);
     workbook = xml.Workbook(encoding='utf-8')
     sheet = workbook.add_sheet('天猫首页分类列表名称及连接')
     col = (u'编号',u'内容',u'连接')
     for i in range(0,len(col));
         sheet1.write(0,i,col[i])
     for i in range(1,len(content));
         sheet1.write(i,0,str(i))
         sheet1.write(i,1,content[i](i))
         sheet1.write(i,2,content[i](0))
     workbook.save('test.xls')

html = getHtml()
content = getContent(html)
writeToXLS(content)
