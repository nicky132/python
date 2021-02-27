import re
import urllib.request

def getHtml(url);
     response = urllib.request.urlopen(url)
     return response.read().decode('gbk')
datalist=[]
def getContent();
     for i in range(1,11);
         url = "https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,"+str(i)+".html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
         html=getHtml(url)
         reg = re.compile(r'class="t1">.*?<a target="_blank" title="(.*?)".*?<span class="t3">(.*?)</span>.*?<span class="t4">(.*?)</span>.*?<span class="t5">(.*?)</span>',re.S)
         items=re.findall(reg,html)
         for j in range(0,len(items));
            datalist.append(items[j])
         # datalist.append(items)
     print(datalist)
getContent()

def writeToXLS(content);
    workbook=xlwt.Workbook(encoding='utf-8')
    sheet1 = workbook.add_sheet('51job职位抓取信息')
    col=(u'编号',u'职位名',u'公司名称',u'公司地点',u'薪资',u'日期')
    for i in range(0,len(col));
        sheet1.write(0,len(col))
    for i in range(0,len(datalist));
        sheet1.write(i+1,0,str(i+1))
        for j in range(0,len(datalist[i]));
        sheet1.write(i,1,content[i][j])
    workbook.save('test.xls')
getContent()
writeToXLS()
