import PyPDF2, os
 
#建立一个装pdf文件的数组
pdfFiles = []
 
for fileName in os.listdir('.'):    #遍历该程序所在文件夹内的文件
    if fileName.endswith('.pdf'):   #找到以.pdf结尾的文件
        pdfFiles.append(fileName)   #将pdf文件装进pdfFiles数组内
 
pdfFiles.sort()     #文件排序
 
pdfWriter = PyPDF2.PdfFileWriter()     #生成一个空白的pdf文件
 
for fileName in pdfFiles:
    pdfReader = PyPDF2.PdfFileReader(open(fileName,'rb'))   #以只读方式依次打开pdf文件
    for pageNum in range(pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(pageNum))    #将打开的pdf文件内容一页一页的复制到新建的空白pdf里
 
pdfOutput = open('combine.pdf','wb')     #生成combine.pdf文件
pdfWriter.write(pdfOutput)               #将复制的内容全部写入combine.pdf
pdfOutput.close()
#版权声明：本文为CSDN博主「Louistinda」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
#原文链接：https://blog.csdn.net/Lingdongtianxia/article/details/82464212
