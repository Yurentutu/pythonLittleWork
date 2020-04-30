from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import os
from tkinter import *
import requests



def buttonClick():
    #button['text']="下载中"
    url=entry.get()
    #print(url)
    #获取文库文档URL
    #url=input('请输入目标文库文档链接：')
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    print(os.getcwd())
    #模拟浏览器，获取页面资源
    driver = webdriver.Firefox(executable_path=os.getcwd()+'\geckodriver.exe',options=options)
    driver.maximize_window()
    driver.get(url)
    time.sleep(3)

    #获取文章标题，并创建文件夹
    docName = driver.find_element_by_class_name('doc-header-title').text
    if not os.path.exists(docName):  
                os.mkdir(docName)
    filePath = docName+'/'

    #获取文章页码
    pagesText=driver.find_element_by_class_name('page-count').text[1:]
    pages = int(pagesText)

    fileType = driver.find_element_by_tag_name('body').get_attribute("class")
    if(fileType == 'sf-2111 newTools'):      
        #创建doc文件，滚动页面，获取实时页面资源，写入文件
        with open(filePath+docName+'.doc', 'w', encoding='utf-8') as f:
            for page in range(1,pages+1):
                #如果滚动到第3页，获取资源结束，模拟单击继续阅读标签
                if(page == 4):
                    target = driver.find_element_by_css_selector("div[id='html-reader-go-more']")
                    driver.execute_script("arguments[0].scrollIntoView();",target)
                    nextPage = target.find_element_by_css_selector("span[class='fc2e']")
                    time.sleep(1)
                    nextPage.click()
                target = driver.find_element_by_id("pageNo-"+str(page))
                driver.execute_script("arguments[0].scrollIntoView(false);",target)
                #根据页面渲染时间，调整sleep函数的参数
                time.sleep(0.1)
                #调整文档格式，写入文件
                ps = target.find_elements_by_tag_name('p')
                sign = False  #sign变量，标记是否已经写入换行
                for p in ps:
                    if p.text == '':
                        if sign == False:
                            f.write('\n')
                        sign = True
                    else:
                        f.write(p.text)
                        sign = False
            f.close()
    elif(fileType == 'sf-2111 flowPPt'):
        for page in range(1,pages+1):
        #如果滚动到第3页，获取资源结束，模拟单击继续阅读标签
            if(page == 4):
                try:
                    target = driver.find_element_by_css_selector("div[id='html-reader-go-more']")
                except:
                    break
                driver.execute_script("arguments[0].scrollIntoView();",target)
                nextPage = target.find_element_by_css_selector("span[class='fc2e']")
                time.sleep(1)
                nextPage.click()
            #针对需要付费的页面无法爬取
            try:
                target = driver.find_element_by_class_name("reader-pageNo-"+str(page))
            except:
                break
            driver.execute_script("arguments[0].scrollIntoView(false);",target)
            #根据页面渲染时间，调整sleep函数的参数
            time.sleep(0.1)
            imgs = target.find_elements_by_tag_name('img')
            for img in imgs:
                imgUrl = img.get_attribute("src")
                with open(filePath+str(page)+'.jpg', 'wb') as f:
                    f.write(requests.get(imgUrl).content)
                f.close()
    else:
        pass
        #entry['text']="程序暂未适配该格式文档！"
        #弹出暂未适配该格式文档！！
        
    #关闭模拟浏览器
    driver.quit()
    #entry['text']="程序暂未适配该格式文档！"
    #label["text"]="下载完成"
    #window.destroy()


window = Tk()
window.title("百度文库下载工具")
window.resizable(0,0)
label = Label(window,text="请输入目标文档链接后点击：")
label.pack(side = LEFT)
entry = Entry()
entry.pack(side = RIGHT)
button = Button(window,text="下载",command = buttonClick)
button.pack(side = RIGHT)
window.mainloop()


