#!/usr/bin/env python
# coding: utf-8
import os
import sys
from pdf2docx import extract_tables, parse
import docx2txt
import pandas as pd 
import numpy as np
import re
import docx2txt
import json

def path_list(path):
    
    path_list = os.listdir(path)
    path_list = [os.path.join(path,file) for file in path_list]
    
    return path_list


def extract_table(pdf_list,csv_path):

    for pdf in pdf_list:
    
        pattern = "PDFs/(.*?).pdf"
        folder = re.search(pattern, pdf).group(1)
        if not os.path.exists(os.path.join(csv_path,folder)):
            os.makedirs(os.path.join(csv_path,folder))
        
        tables = extract_tables(pdf)
        for i,table in enumerate(tables):
            
            df = pd.DataFrame.from_records(table)
            df.columns = df.iloc[0]
            df = df[1:]
            
            save_path = os.path.join(csv_path,folder,str(i)+'.csv')
            df.to_csv(save_path, index=False)
            
    return
            

def extract_docx(pdf_list,docx_path):
    
    for pdf in pdf_list:
    
        pattern = "PDFs/(.*?).pdf"
        file = re.search(pattern, pdf).group(1)
        save_path = os.path.join(docx_path,file+'.docx')
        parse(pdf,save_path)
        
    return

def extract_text(docx_list,output_path):
    
    def text_processing(text): #add on more regex rules when needed
        text = text.split('\n\n')
        text = [x.strip() for x in text]
        text = list(filter(None, text))
        text = [x.replace("\n", "") for x in text]
        return text
        
    
    json_dict = {}
    for docx in docx_list:
        
        pattern = "Docx/(.*?).docx"
        file = re.search(pattern,docx).group(1)
        json_dict[file] = []
        
        text = docx2txt.process(docx)
        para_list = text_processing(text)
        
        for para in para_list:
            para_dict = {}
            para_dict['Text'] = para
            json_dict[file].append(para_dict)
    
    output = os.path.join(output_path,'output.json')
    with open(output, 'w') as fp:
        json.dump(json_dict, fp, indent=4)
        
    return
        
        