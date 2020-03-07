from Parse import from_first_chapter, parse_book
from getUrl import get_url
from InitialFile import initial

# book_name=input()
# writer_name=input()
# first_chapter=int(input())
# url=input()


book_name = 'হাজার বছর ধরে'
writer_name = 'জহির রায়হান'
first_chapter = 1
initial(book_name, writer_name)

url = 'https://www.ebanglalibrary.com/14016/%e0%a7%a6%e0%a7%a7-%e0%a6%ae%e0%a6%b8%e0%a7%8d%e0%a6%a4-%e0%a6%ac%e0%a7%9c-%e0%a6%85%e0%a6%9c%e0%a6%97%e0%a6%b0%e0%a7%87%e0%a6%b0-%e0%a6%ae%e0%a6%a4-%e0%a6%b8%e0%a7%9c%e0%a6%95%e0%a6%9f%e0%a6%be/'

from_first_chapter(url, i=first_chapter, book=book_name, writer=writer_name,serial = 1)

# book='https://www.ebanglalibrary.com/humayunahmed/category/%E0%A6%89%E0%A6%AA%E0%A6%A8%E0%A7%8D%E0%A6%AF%E0%A6%BE%E0%A6%B8-%E0%A6%B9%E0%A7%81%E0%A6%AE%E0%A6%BE%E0%A6%AF%E0%A6%BC%E0%A7%82%E0%A6%A8-%E0%A6%86%E0%A6%B9%E0%A6%AE%E0%A7%87%E0%A6%A6/%E0%A6%B8%E0%A7%8C%E0%A6%B0%E0%A6%AD-%E0%A7%A7%E0%A7%AF%E0%A7%AE%E0%A7%AA/'

# parse_book(book, i=first_chapter, book=book_name, writer=writer_name,serial=1)



url='https://www.ebanglalibrary.com/humayunahmed/%E0%A6%85%E0%A6%A8%E0%A7%8D%E0%A6%AF-%E0%A6%B0%E0%A6%95%E0%A6%AE-%E0%A6%89%E0%A7%8E%E0%A6%B8%E0%A6%AC/'

# get_url(url)
writer_name = 'হুমায়ূন আহমেদ'
# initial('আরো হুমায়ুন', writer_name)
file = open('link.txt')
link = []
for url in file:
    link.append(url[:-1])
file.close()


# file_last = open('last.txt')
# last = int(file_last.readline())# file_last.close()

# for i in range(0,20):
#     url=link[i]
#     parse_book(url, i=first_chapter, writer=writer_name,serial=i)
start = 1
link = link[start-1:]
i = start
for url in link:

    f = False
    # if i in [13, 29, 106]:
    #     f = True

    first_chapter = 1
    if i in [2]:
        first_chapter = 0

    # parse_book(url, i=first_chapter, writer=writer_name, serial=i, flag=f)
    # from_first_chapter(url, i=first_chapter,book='সকল কাঁটা ধন্য করে', writer=writer_name, serial=i, flag=f)
    i = i+1


# i=1
# array = [21,23,5,32,11,34,22,33,6,29,15,12,24,10,7,13,35,8,27,20,16,2,14,4,25,18,26,1,31,9,30,17,19,28,3]
# for k in range(len(array)):
#     url = link [array[k]-1]
#     first_chapter=1

#     f = False
#     j= array[k]
#     if j in [5,21,32,33]: #(j == 5 or j == 21 or j == 32 or j == 33 ) :
#         f = True

#     # if (i == 41 or i == 45 or i == 46 ) :
#         # first_chapter = 0

#     parse_book(url, i=first_chapter, writer=writer_name,serial=i,flag=f)
#     i=i+1
