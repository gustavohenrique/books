from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument

fp = open('/Users/gustavo/Downloads/Linguagem C - Luis Damas.pdf', 'rb')
parser = PDFParser(fp)
doc = PDFDocument(parser)

print doc.info
