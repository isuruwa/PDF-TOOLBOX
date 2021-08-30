#!/usr/bin/env python
#coding: utf-8
#AUTHOR : DEVIL MASTER

from art import *
import time
from os import system, name


######################### pdf info #########################

def pdfinfo():# extract_doc_info.py
    help
    from PyPDF2 import PdfFileReader

    x=input("\033[35m  [\033[33m*\033[35m]\033[1;32m Enter Input Pdf Path : ")

    def extract_information():
        with open(x, 'rb') as f:
            pdf = PdfFileReader(f)
            information = pdf.getDocumentInfo()
            number_of_pages = pdf.getNumPages()

        txt = f"""
        Information about {x} : 

        Author: {information.author}
        Creator: {information.creator}
        Producer: {information.producer}
        Subject: {information.subject}
        Title: {information.title}
        Number of pages: {number_of_pages}
        """

        print(txt)
        return information

    if __name__ == '__main__':
        extract_information()


######################### pdf merge #########################

def pdfmerger():
    
    from PyPDF2 import PdfFileReader, PdfFileWriter

    x=input("\033[35m  [\033[33m*\033[35m]\033[1;32m Enter 1st Pdf Path : ")
    y=input("\033[35m  [\033[33m*\033[35m]\033[35m Enter 2nd Pdf Path : ")
    z=input("\033[35m  [\033[33m*\033[35m]\033[36m Enter Output Pdf Path  : ")

    def merge_pdfs(paths, output):
        pdf_writer = PdfFileWriter()

        for path in paths:
            pdf_reader = PdfFileReader(path)
            for page in range(pdf_reader.getNumPages()):
                # Add each page to the writer object
                pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
        with open(output, 'wb') as out:
            pdf_writer.write(out)

    if __name__ == '__main__':
        paths = [x,y]
        merge_pdfs(paths, output=z)

######################### pdf split #########################

def pdfspliter():
    import PyPDF2

    def PDFsplit(pdf, splits):
        # creating input pdf file object
        pdfFileObj = open(pdf, 'rb')
     
        # creating pdf reader object
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
     
        # starting index of first slice
        start = 0
     
        # starting index of last slice
        end = splits[0]
     
     
        for i in range(len(splits)+1):
            # creating pdf writer object for (i+1)th split
            pdfWriter = PyPDF2.PdfFileWriter()
         
            # output pdf file name
            outputpdf = pdf.split('.pdf')[0] + str(i) + '.pdf'
         
            # adding pages to pdf writer object
            for page in range(start,end):
                pdfWriter.addPage(pdfReader.getPage(page))
         
            # writing split pdf pages to pdf file
            with open(outputpdf, "wb") as f:
                pdfWriter.write(f)
 
            # interchanging page split start position for next split
            start = end
            try:
                # setting split end position for next split
                end = splits[i+1]
            except IndexError:
                # setting split end position for last split
                end = pdfReader.numPages
         
        # closing the input pdf file object
        pdfFileObj.close()
             
    def main():
        # pdf file to split
        pdf = input("\033[35m  [\033[33m*\033[35m]\033[1;32m Enter Input Pdf Path : ")

        outputpdf = input("\033[35m  [\033[33m*\033[35m]\033[31m Enter Output Pdf Path : ")
     
        # split page positions
        splits = [2,4]
     
        # calling PDFsplit function to split pdf
        PDFsplit(pdf, splits)
 
    if __name__ == "__main__":
        # calling the main function
        main()

######################### pdf raotate #########################

def pdfrotater():
    import PyPDF2
    import sys
 
    def PDFrotate(origFileName, newFileName, rotation):
 
        # creating a pdf File object of original pdf
        pdfFileObj = open(origFileName, 'rb')
     
        # creating a pdf Reader object
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
 
        # creating a pdf writer object for new pdf
        pdfWriter = PyPDF2.PdfFileWriter()
     
        # rotating each page
        for page in range(pdfReader.numPages):
 
            # creating rotated page object
            pageObj = pdfReader.getPage(page)
            pageObj.rotateClockwise(rotation)
 
            # adding rotated page object to pdf writer
            pdfWriter.addPage(pageObj)
 
        # new pdf file object
        newFile = open(newFileName, 'wb')
     
        # writing rotated pages to new file
        pdfWriter.write(newFile)
 
        # closing the original pdf file object
        pdfFileObj.close()
     
        # closing the new pdf file object
        newFile.close()
     
 
    def main():
 
        # original pdf file name
        origFileName = input("\033[35m  [\033[33m*\033[35m]\033[1;32m Enter Input Pdf Path  : ")
    
        # new pdf file name
        newFileName = input("\033[35m  [\033[33m*\033[35m]\033[35m Enter Output Pdf Path : ")
     
        # rotation angle
        rotation = sys.argv[2]
     
        # calling the PDFrotate function
        PDFrotate(origFileName, newFileName, rotation)
     
    if __name__ == "__main__":
        # calling the main function
        main()

######################### pdf watermark #########################

def pdfwatermarker():
    from PyPDF2 import PdfFileWriter, PdfFileReader

    def create_watermark(input_pdf, output, watermark):
        watermark_obj = PdfFileReader(watermark)
        watermark_page = watermark_obj.getPage(0)

        pdf_reader = PdfFileReader(input_pdf)
        pdf_writer = PdfFileWriter()

        # Watermark all the pages
        for page in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page)
            page.mergePage(watermark_page)
            pdf_writer.addPage(page)

        with open(output, 'wb') as out:
            pdf_writer.write(out)

    if __name__ == '__main__':
        create_watermark(
            input_pdf=input("\033[35m  [\033[33m*\033[35m]\033[1;32m Enter Input Pdf Path     : "), 
            output=input("\033[35m  [\033[33m*\033[35m]\033[35m Enter Output Pdf Path    : "),
            watermark=input("\033[35m  [\033[33m*\033[35m]\033[36m Enter Watermark Pdf Path : "))

######################### pdf encrypt #########################

def pdfencrypter():
    from PyPDF2 import PdfFileWriter, PdfFileReader

    def add_encryption(input_pdf, output_pdf, password):
        pdf_writer = PdfFileWriter()
        pdf_reader = PdfFileReader(input_pdf)

        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

        pdf_writer.encrypt(user_pwd=password, owner_pwd=None, 
                        use_128bit=True)

        with open(output_pdf, 'wb') as fh:
            pdf_writer.write(fh)

    if __name__ == '__main__':
        add_encryption(input_pdf=input("\033[35m  [\033[33m*\033[35m]\033[1;32m Enter Input Pdf Path  : "),
                    output_pdf=input("\033[35m  [\033[33m*\033[35m]\033[31m Enter Output Pdf Path : "),
                    password=input("\033[35m  [\033[33m*\033[35m]\033[36m Enter Password : "))

######################### pdf decrypt #########################

def pdfdecrypter():
    import pikepdf
    from tqdm import tqdm

    input_pdf=input("\033[35m  [\033[33m*\033[35m]\033[1;32m Enter Input Pdf Path : ")
    listtxt=input("\033[35m  [\033[33m*\033[35m]\033[35m Enter Wordlist Path  : ")

    # load password list
    passwords = [ line.strip() for line in open(listtxt) ]

    # iterate over passwords
    for password in tqdm(passwords, "\033[35m  [\033[33m*\033[35m]\033[36m Decrypting PDF"):
        try:
            # open PDF file
            with pikepdf.open(input_pdf, password=password) as pdf:
                # Password decrypted successfully, break out of the loop
                print("\033[35m  [\033[33m*\033[35m]\033[1;32m [+] Password found:", password)
                break
        except pikepdf._qpdf.PasswordError as e:
            # wrong password, just continue in the loop
            continue

######################### pdf to audio #########################

def pdf2audio():
    import PyPDF2
    import pyttsx3

    inpdf = input("\033[35m  [\033[33m*\033[35m]\033[1;32m Enter Input Pdf Path : ")

    # path of the PDF file
    path = open(inpdf, 'rb')

    # creating a PdfFileReader object
    pdfReader = PyPDF2.PdfFileReader(path)

    # the page with which you want to start
    # this will read the page of 25th page.
    from_page = pdfReader.getPage(24)

    # extracting the text from the PDF
    text = from_page.extractText()

    # reading the text
    speak = pyttsx3.init()
    speak.say(text)
    speak.runAndWait()


######################### text to pdf #########################

def txt2pdf():
    from fpdf import FPDF

    # save FPDF() class into
    # a variable pdf
    pdf = FPDF()


    myfile = input("\033[35m  [\033[33m*\033[35m]\033[1;32m Enter Input Pdf Path  : ")
    outpdf=input("\033[35m  [\033[33m*\033[35m]\033[36m Enter Output Pdf Path : ")

    # Add a page
    pdf.add_page()

    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Arial", size = 15)

    # open the text file in read mode
    f = open(myfile, "r")

    # insert the texts in pdf
    for x in f:
	    pdf.cell(200, 10, txt = x, ln = 1, align = 'C')

    # save the pdf with name .pdf
    pdf.output(outpdf)



######################### pdf to text #########################

def pdf2txt():
    #pip install pdfminer.six
    import io

    from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
    from pdfminer.converter import TextConverter
    from pdfminer.layout import LAParams
    from pdfminer.pdfpage import PDFPage


    def convert_pdf_to_txt(path):
        '''Convert pdf content from a file path to text

        :path the file path
        '''
        rsrcmgr = PDFResourceManager()
        codec = 'utf-8'
        laparams = LAParams()

        with io.StringIO() as retstr:
            with TextConverter(rsrcmgr, retstr, codec=codec,
                            laparams=laparams) as device:
                with open(path, 'rb') as fp:
                    interpreter = PDFPageInterpreter(rsrcmgr, device)
                    password = ""
                    maxpages = 0
                    caching = True
                    pagenos = set()

                    for page in PDFPage.get_pages(fp,
                                                pagenos,
                                                maxpages=maxpages,
                                                password=password,
                                                caching=caching,
                                                check_extractable=True):
                        interpreter.process_page(page)

                    return retstr.getvalue()

    x=input("\033[35m  [\033[33m*\033[35m]\033[36m Enter Input Pdf Path : ")

    if __name__ == "__main__":
        print(convert_pdf_to_txt(x)) 

######################### begin #########################

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def back():
  print("\n")
  input("\033[37m  [\033[31m+\033[37m] Press Enter To Go Back")
  menu()

def banner(topic):
  clear()
  print("\033[1;32m")
  tprint(topic)

def author():
  print("                   \033[37m[\033[31m+\033[37m] DEVELOPED BY DEVIL MASTER \033[37m[\033[31m+\033[37m]")
  print("                   \033[37m[\033[31m+\033[37m]     github.com/isuruwa    \033[37m[\033[31m+\033[37m]\n\n")


######################### Menu #########################

def menu():
  banner("""  PDF-TOOLKIT\n""")
  author()
  print("\033[35m  [\033[33m*\033[35m]\033[31m 1.Pdf To Text")
  print("\033[35m  [\033[33m*\033[35m]\033[1;32m 2.Text To Pdf")
  print("\033[35m  [\033[33m*\033[35m]\033[34m 3.Pdf Merger")
  print("\033[35m  [\033[33m*\033[35m]\033[35m 4.Pdf Spliter")
  print("\033[35m  [\033[33m*\033[35m]\033[36m 5.Pdf Rotater")
  print("\033[35m  [\033[33m*\033[35m]\033[37m 6.Pdf Watermarker")
  print("\033[35m  [\033[33m*\033[35m]\033[1;32m 7.Pdf Encrypter")
  print("\033[35m  [\033[33m*\033[35m]\033[31m 8.Pdf Decrypter")
  print("\033[35m  [\033[33m*\033[35m]\033[35m 9.Pdf To Audio")
  print("\033[35m  [\033[33m*\033[35m]\033[36m 10.Pdf Info")
  print("\033[35m  [\033[33m*\033[35m]\033[31m 11.Exit\n")
  choice=input("\033[37m  [\033[31m+\033[37m] Enter Choice : ")
  if choice == "1" or choice == "01":
    banner("""           PDF 2 TXT""")
    author()
    pdf2txt()
    back()
  elif choice == "2" or choice == "02":
    banner("""          TXT 2 PDF""")
    author()
    txt2pdf()
    back()
  elif choice == "3" or choice == "03":
    banner("""   PDF MERGER""")
    author()
    pdfmerger()
    back()
  elif choice == "4" or choice == "04":
    banner(""" PDF SPLITER""")
    author()
    pdfspliter()
    back()
  elif choice == "5" or choice == "05":
    banner(""" PDF ROTATER""")
    author()
    pdfrotater()
    back()
  elif choice == "6" or choice == "06":
    banner(""" PDF WATERMAKER""")
    author()
    pdfwatermarker()
    back()
  elif choice == "7" or choice == "07":
    banner(""" PDF ENCRYPTER""")
    author()
    pdfencrypter()
    back()
  elif choice == "8" or choice == "08":
    banner(""" PDF DECRYPTER""")
    author()
    pdfdecrypter()
    back()
  elif choice == "9" or choice == "09":
    banner("""   PDF 2 AUDIO""")
    author()
    pdf2audio()
    back()
  elif choice == "10":
    banner("""           PDF INFO""")
    author()
    pdfinfo()
    back()
  elif choice == "11":
    time.sleep(1)
    print("\n")
    print("\033[37m  [\033[31m+\033[37m] THANK YOY ! \033[37m [\033[31m+\033[37m]\n")
    time.sleep(1)
    print("\033[37m  [\033[31m+\033[37m] STAY SAFE ! \033[37m [\033[31m+\033[37m]\n")
    time.sleep(1)
    print("\033[37m  [\033[31m+\033[37m] EXPECT US !\n")
    time.sleep(1)
    quit()
  elif choice == "":
    time.sleep(1)
    menu()
  else:
    print("\033[37m  [\033[31m+\033[37m] Wrong Choice")
    time.sleep(1)
    menu()

menu()
