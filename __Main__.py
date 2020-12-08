#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
sys.path.append('../Src')
import extract_table


# In[2]:


pdf_path = '..\\PDFs\\'
docx_path ='..\\Docx\\'
csv_path ='..\\CSV tables\\'
output_path = '..\\Output\\'

pdf_list = extract_table.path_list('../PDFs/')
docx_list = extract_table.path_list('../Docx/')


# In[3]:


extract_table.extract_docx(pdf_list,docx_path)
extract_table.extract_table(pdf_list,csv_path)
extract_table.extract_text(docx_list,output_path)


# In[ ]:




