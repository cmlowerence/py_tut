# Write a program to manipulate pdf files using pyPDF. Your programs should be able to merge multiple pdf files into a single pdf. You are welcome to add more functionalities
# py_pdf is a free and open-source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files. It can also add custom data, viewing options, and passwords to PDF files. py_pdf can retrieve text and metadata from PDFs as well.

# Reading Metadata
from PyPDF2 import PdfReader as pdf_reader, PdfWriter as pdf_writer
import os
import time
import datetime
from functions import *

rootDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(rootDir)
print()
print(" Here we have these directories and files: ".center(70,"="))
cont_desc = content_dir(rootDir)


for content in cont_desc:
  print(f"{content['index']}. {content['name']} ({content['type']})")
print()

# Asking to change directory
print("Do you want to change the directory?")
dir_name = get_valid_dir_name()
if dir_name is not None:
  changeDir(dir_name)
  print(f"Directory changed to {dir_name}")
  print('Content of Directory: ')
  file_content = os.listdir()
  for index,file in enumerate(file_content,1):
    print(f"{index}. {file}")
  pdf_files = [file for file in os.listdir() if file.endswith('.pdf')] # list of all pdf files in directory
  if pdf_files:
    print("\nDo you want to merge the pdf files? ")
    merge_choice = input("Enter 'yes' to continue merging and just Enter to skip: ")
    
    if merge_choice.lower() == 'yes' and pdf_files:
      # Printing all the pdf files with S.No.
      
      print(" We have these pdf files ".center(50,"*"))
      print() # for Extra new line
      
      print("S.No.|  \t File Name")
      print("--------------------------")
      pdf_files_list = []
      for index, file in enumerate(pdf_files,1):
        pdf_files_list.append({'index': index, 'name': file})
        print(f" {index}.  | \t{file}")
      print("Enter the S.No. of pdf files which you want to merge separated with ','\nfor eg.: 1,2,3")
      indices = input("Enter the S.No.: ")
      ind_list = [int(ind) for ind in indices.split(",")]
      pdf_names = [name_dict['name'] for name_dict in pdf_files_list if name_dict['index'] in ind_list]
      print()
      if pdf_names:
        print(f"Merging files: {', '.join(pdf_names)}")
        confirm = input("Should we continue (press just 'Enter' to continue): ")
        if confirm == '':
          
          print(f"Merging {', '.join(pdf_names)}...")
          merger = pdf_writer()
          try:
            for pdf in pdf_names:
              merger.append(pdf)
            new_name = input("Name of the new pdf: ")
            if new_name+'.pdf' in os.listdir():
              print("The name of the file already exist. Renaming with random name")
              new_name = new_name + '_'+ datetime.datetime.now().strftime("%d-%m-%y_%H:%M:%S")
            if new_name:
              merger.write(f"{new_name}.pdf")
            else:
              new_name = datetime.datetime.now().strftime("%d-%m-%y_%H:%M:%S")
              merger.write(f"{new_name}.pdf")
            print(f"PDF Merged under {new_name}.pdf name")
            merger.close()
          except Exception as e:
            print(e)
            print("Terminating program...")
            exit()
      else:
        print("No such S.No. in the list.",flush=True)
        time.sleep(1)
        print("Terminating Program...",flush=True)
        time.sleep(1)
        exit()
  else:
    print("No PDF Files found.",flush=True)
    time.sleep(1)
    print("Terminating Program...",flush=True)
    time.sleep(1)
    exit()