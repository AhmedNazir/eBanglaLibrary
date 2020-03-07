import os

def initial(book_title, writer):

    if not os.path.exists("book"):
        os.makedirs("book")

    file =  open("title.txt",'w',encoding='utf-8')
    file.close()
    
    with open('res/about-01-title.xhtml', encoding='utf-8') as f:
        with open('book/about-01-title.xhtml', 'w', encoding='utf-8') as file:
            temp = f.read()
            temp = temp.replace('dummy-title', book_title)
            temp = temp.replace('dummy-writer', writer)
            file.write(temp)

    with open('res/about-04-about-reader.xhtml', encoding='utf-8') as f:
        with open('book/about-04-about-reader.xhtml', 'w', encoding='utf-8') as file:
            file.write(f.read())

    with open('res/about-05-acknowledgement.xhtml', encoding='utf-8') as f:
        with open('book/about-05-acknowledgement.xhtml', 'w', encoding='utf-8') as file:
            file.write(f.read())

    with open('res/about-06-about-contributor.xhtml', encoding='utf-8') as f:
        with open('book/about-06-about-contributor.xhtml', 'w', encoding='utf-8') as file:
            file.write(f.read())

    with open('res/style.css', encoding='utf-8') as f:
        with open('book/style.css', 'w', encoding='utf-8') as file:
            file.write(f.read())