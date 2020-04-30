from fpdf import FPDF
from PIL import Image
import os

def makePdf(pdfFileName, listPages):

	cover = Image.open(listPages[0])
	width, height = cover.size

	pdf = FPDF(unit = "pt", format = [width, height])

	for page in listPages:
		pdf.add_page()
		pdf.image(page, 0, 0)

	pdf.output(pdfFileName, "F")

makePdf("result.pdf", [imgFileName for imgFileName in os.listdir('.') \
					   if imgFileName.endswith("png")])

#版权声明：本文为CSDN博主「巨輪」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
#原文链接：https://blog.csdn.net/u011863024/java/article/details/104197828
