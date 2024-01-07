# Write a program to manipulate pdf files using pyPDF. Your programs should be able to merge multiple pdf files into a single pdf. You are welcome to add more functionalities
# py_pdf is a free and open-source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files. It can also add custom data, viewing options, and passwords to PDF files. py_pdf can retrieve text and metadata from PDFs as well.

# Reading Metadata
from PyPDF2 import PdfReader as pdf_reader, PdfWriter as pdf_writer
import os
def isDir(path):
  if os.path.isdir(path):
    return True
  else:
    return False
def isPDF(path):
  if path.lower().endswith('.pdf'):
    return True
  else:
    return False
def changeDir(path):
  os.chdir(path)
def checkType(content):
  if os.path.isdir(content):
    return 'dir'
  elif os.path.isfile(content):
    return 'file'
  else:
    return 'unknown'
def content_dir(path):
  contents = os.listdir(path)
  return [{'name': content, 'type':checkType(content), 'index': index} for index, content in enumerate(contents)]
def readPdf(pdf):
  return pdf_reader(pdf)

rootDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(rootDir)
print()
print(" Here we have these directories and files: ".center(70,"="))
cont_desc = content_dir(rootDir)


for content in cont_desc:
  print(f"{content['index'] + 1}. {content['name']} ({content['type']})")
print()
reader = pdf_reader("./pdf/drylab.pdf")
meta = reader.metadata
# print(len(reader.pages))

# Asking to change directory
print("Do you want to change the directory?")
dir_name = input("Enter the name of directory: ")
if not dir_name in os.listdir():
  print(f"Directory {dir_name} doesn't exists")
else:
  changeDir(dir_name)
  # ... functions to be done...
  print(f"Directory changed to {dir_name}")
  for file in os.listdir():
    meta = readPdf(file).metadata
    print()
    print(f" Meta information about {file} ".center(60,'-'))
    print("Author: ",meta.author)
    print("Creator: ",meta.creator)
    print("Producer: ",meta.producer)
    print("Subject: ",meta.subject)
    print("Title: ",meta.title)
    
  print("Do you want to merge the pdf files? ")
  merger = pdf_writer()
  print(os.listdir())
  indices = input("Enter the serial no. of the pdf you want to merge: ")
  ind_list = [int(ind) - 1 for ind in indices.split(",")]
  print(ind_list)
  pdf_names = [os.listdir()[ind] for ind in ind_list]
  print(pdf_names)
  print(f"Merging {''.join(pdf_names)}...")
  for pdf in pdf_names:
    merger.append(pdf)
  merger.write("merged-pdf.pdf")
  print(f"PDF Merged")
  merger.close()
