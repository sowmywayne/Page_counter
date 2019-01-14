import os
from docx import Document


# document = Document('/Users/sowmy_wayne/Desktop/sample.docx')

# count = 0
# temp = 0
# for p in document.paragraphs:
# 	count += 1
# 	if(count == 25):
# 		temp += 1
# 		count = 0
# print(count)		
# if(count%25 != 0):
# 	temp += 1
# print(temp)	

# directory = "/Users/sowmy_wayne/Documents/Pyhton"

# for root, dirs, files in os.walk(directory):
#     for file in files:
#         if file.endswith('.txt'):
#             print (file)


def docx(directory):
	for root, dirs, files in os.walk(directory):
    	for file in files:
        	if file.endswith('.docx'):
            	print (file)



