import PyPDF2 as pdf2

with open ("D:\My Created Apps\PDFsample.pdf", mode="rb") as f:
    reader = pdf2.PdfFileReader(f)  
    writer = pdf2.PdfFileWriter()
    number_of_pages = reader.getNumPages()
        
    #extractText() only works while the file is "open" (inside 'with open')
    count = reader.numPages
    print("Number of total pages is "+ str(count))
  
    #code to define keyword to split the PDF
    for i in range(count):
        #writer = pdf2.PdfFileWriter() 
        page = reader.getPage(i)
        currentpage = page.extractText()
        if "installed" in currentpage:
            firstpage = i
            print("Installed word found in page "+str(i+1))
            writer.addPage(reader.getPage(i))
            for x in range(firstpage+1,count):
                page = reader.getPage(x)
                currentpage2 = page.extractText()
                
                if "installed" in currentpage2:
                    output_filename = '{}_page_{}.pdf'.format('fname', i+1)
                    with open(output_filename, 'wb') as out:
                        writer.write(out)
                        print("One PDF created")
                        #The following line resets the writer    
                        writer = pdf2.PdfFileWriter()
                        
                        break
                elif x == count:
                    output_filename = '{}_page_{}.pdf'.format('fname', i+1)
                    with open(output_filename, 'wb') as out:
                        writer.write(out)
                        print("Finished")
                    
                else:
                    writer.addPage(reader.getPage(x))

            else:
                    writer.addPage(reader.getPage(x))  

    output_filename = '{}_page_{}.pdf'.format('fname', i+1)
    with open(output_filename, 'wb') as out:
        writer.write(out)
        print("Last PDF created")
        print("Finished")        
                