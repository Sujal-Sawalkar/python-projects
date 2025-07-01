def extract_text():
    from PyPDF2 import PdfReader # type: ignore

    pdf = PdfReader("bhagwat-geeta.pdf")
    for page in pdf.pages:
        print(page.extract_text())

def merge_pdfs():
    from PyPDF2 import PdfMerger# type: ignore
    import os

    merger = PdfMerger()
    files = [file for file in os.listdir() if file.endswith(".pdf")]
    for pdf in files:
        merger.append(pdf)

    merger.write("merged-pdf.pdf")
    merger.close()

def encrypt_pdf():
    from PyPDF2 import PdfReader, PdfWriter# type: ignore

    reader = PdfReader("input.pdf") 
    writer = PdfWriter()
    
    for page in reader.pages:
        writer.add_page(page)
    
    writer.encrypt(user_password="1234", owner_password=None)
    
    with open("encrypted_output.pdf", "wb") as f:
       writer.write(f)
                
    print("PDF encrypted successfully")     

def extract_metadata():
    from PyPDF2 import PdfReader# type: ignore
    path = "bhagwat-geeta.pdf"
    with open(path, 'rb') as f:
        pdf = PdfReader(f)
    
    information = pdf.metadata
    # print(information)
    print("\nAuthor is ",information.author)
    print("\nCreator is ",information.creator)
    print("\nTitle is ",information.title)
    print("\nProducer is ",information.producer)

    no_of_p = len(pdf.pages)
    print("\n   Number of Pages are",no_of_p)
    

def pdf_tool():
    print("\n📄 PDF Utility Tool 📄")
    print("1. Extract text from a PDF")
    print("2. Merge multiple PDFs")
    print("3. Encrypt a PDF")
    print("4. Extract Metadata from a PDF")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    match choice:
        case "1":
            print("→ Extracting text...")
            extract_text()

        case "2":
            print("→ Merging PDFs...")
            merge_pdfs()
                
        case "3":
            print("→ Encrypting PDF...")
            encrypt_pdf()

        case "4":
            print("→ Extracting Metadata...")
            extract_metadata()
           
        case "5":
            print("Goodbye!")
            return
        case _:
            print("⚠️ Invalid choice. Please try again.")


while True:
    pdf_tool()
