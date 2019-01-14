# os module is used to open the directory
import os

# docx module is used to read the docx file in give directory
from docx import Document

# pyPEDF2 module is used to read the PDF file in given directory
from PyPDF2 import PdfFileReader

# no_of_docFile function is used to count the number of pages in each files 

def no_of_docFile(d ,file):
	
	page_count =0
	no_of_lines = 0
	for lines in Document(d+file).paragraphs:
		no_of_lines += 1
		
		if(no_of_lines == 25):
			page_count += 1
			no_of_lines = 0
	
	if(no_of_lines != 25):
		page_count += 1
	
	return(page_count)		

""" docx function is used to read all the docx file from given directory and the function finaly return the 
	number of pages
					"""
def docx(directory):
	
	total_no_of_pg = 0
	
	for root, dirs, files in os.walk(directory):
		for file in files:
			
			if file.endswith('.docx'):
					
					total_no_of_pg += no_of_docFile(directory,file)
	
	return total_no_of_pg			

def pdf(directory):

	total_no_of_pg = 0

	for root, dirs, files in os.walk(directory):
		for file in files:
			
			if file.endswith('.docx'):
					
					total_no_of_pg += no_of_pgPdf(directory,file)

	return(total_no_of_pg)



def no_of_pgPdf(d, file):
	pdf = PdfFileReader(open(d+file,'rb'))
	
	return(pdf.getNumPages())


