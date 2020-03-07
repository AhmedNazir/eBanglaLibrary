from Parse import from_first_chapter, parse_book
from getUrl import get_url
from InitialFile import initial
import os

book_name = 'কিরীটী অমনিবাসর'
writer_name = 'নীহাররঞ্জন গুপ্ত'

url='https://www.ebanglalibrary.com/category/%e0%a6%a8%e0%a7%80%e0%a6%b9%e0%a6%be%e0%a6%b0%e0%a6%b0%e0%a6%9e%e0%a7%8d%e0%a6%9c%e0%a6%a8-%e0%a6%97%e0%a7%81%e0%a6%aa%e0%a7%8d%e0%a6%a4/%e0%a6%95%e0%a6%bf%e0%a6%b0%e0%a7%80%e0%a6%9f%e0%a6%bf-%e0%a6%85%e0%a6%ae%e0%a6%a8%e0%a6%bf%e0%a6%ac%e0%a6%be%e0%a6%b8/'

get_url(url)
initial(book_name, writer_name)

file = open('link.txt')
link = []
for url in file:
    link.append(url[:-1])
file.close()


# # file_last = open('last.txt')
# # last = int(file_last.readline())# file_last.close()

# # for i in range(0,20):
# #     url=link[i]
# #     parse_book(url, i=first_chapter, writer=writer_name,serial=i)

# start = 1

# link = link[start-1:]
# i = start
# for url in link:

#     f = False
#     #ignore List......
#     # if i in [13, 29, 106]:
#     #     f = True

#     #exception chapter list....
#     first_chapter = 1
#     if i in [2]:
#         first_chapter = 0

#     parse_book(url, i=first_chapter, writer=writer_name, serial=i, flag=f)
#     # from_first_chapter(url, i=first_chapter,book='সকল কাঁটা ধন্য করে', writer=writer_name, serial=i, flag=f)
#     i = i+1


i = 1 #serial
# array = [9,7,12,8,4,23,18,22,3,6,5,10,1,11,2,16,21,19,17,13,14,15,20]
array = range(1,48)
for k in range(len(array)):
    url = link [array[k]-1]
    first_chapter=1

    ignore = False
    j= array[k]
    # if j in [9]:
    #     ignore = True

    # Chapter exception................................
    if j in [12,20] :
        first_chapter = 0

    if j not in [9]:   #     ignore = True
        parse_book(url, first_chapter, writer=writer_name,serial=i,flag=ignore)

    i=i+1


os.rename('book',book_name)