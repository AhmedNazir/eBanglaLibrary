from Parse import from_first_chapter, parse_book
from getUrl import get_url
from InitialFile import initial
import os

book_name = 'ট্রেন টু পাকিস্তান'
writer_name = 'খুশবন্ত সিং'
first_chapter = 0
initial(book_name, writer_name)

url = 'https://www.ebanglalibrary.com/7990/%e0%a7%a6%e0%a7%a6-%e0%a6%96%e0%a7%81%e0%a6%b6%e0%a6%ac%e0%a6%a8%e0%a7%8d%e0%a6%a4-%e0%a6%b8%e0%a6%bf%e0%a6%82-%e0%a6%8f%e0%a6%b0-%e0%a6%9f%e0%a7%8d%e0%a6%b0%e0%a7%87%e0%a6%a8-%e0%a6%9f%e0%a7%81/'

from_first_chapter(url, i=first_chapter, book=book_name, writer=writer_name,serial = 1)

# book='https://www.ebanglalibrary.com/humayunahmed/category/%E0%A6%89%E0%A6%AA%E0%A6%A8%E0%A7%8D%E0%A6%AF%E0%A6%BE%E0%A6%B8-%E0%A6%B9%E0%A7%81%E0%A6%AE%E0%A6%BE%E0%A6%AF%E0%A6%BC%E0%A7%82%E0%A6%A8-%E0%A6%86%E0%A6%B9%E0%A6%AE%E0%A7%87%E0%A6%A6/%E0%A6%B8%E0%A7%8C%E0%A6%B0%E0%A6%AD-%E0%A7%A7%E0%A7%AF%E0%A7%AE%E0%A7%AA/'

# parse_book(book, i=first_chapter, book=book_name, writer=writer_name,serial=1)

os.rename('book',book_name)