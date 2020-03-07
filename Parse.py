import os

import requests
from bs4 import BeautifulSoup

chapter_title_number = ['০০', '০১', '০২', '০৩', '০৪', '০৫', '০৬', '০৭', '০৮', '০৯', '১০', '১১', '১২', '১৩', '১৪', '১৫',
                        '১৬', '১৭', '১৮', '১৯', '২০', '২১', '২২', '২৩', '২৪', '২৫', '২৬', '২৭', '২৮', '২৯', '৩০', '৩১',
                        '৩২', '৩৩', '৩৪', '৩৫', '৩৬', '৩৭', '৩৮', '৩৯', '৪০', '৪১', '৪২', '৪৩', '৪৪', '৪৫', '৪৬', '৪৭',
                        '৪৮', '৪৯', '৫০', '৫১', '৫২', '৫৩', '৫৪', '৫৫', '৫৬', '৫৭', '৫৮', '৫৯', '৬০', '৬১', '৬২', '৬৩',
                        '৬৪', '৬৫', '৬৬', '৬৭', '৬৮', '৬৯', '৭০','৭১','৭২','৭৩','৭৩','৭৪','৭৫','৭৬','৭৭','৭৮','৭৯','৮০','৮১','৮২','৮৩','৮৪','৮৫','৮৬','৮৭','৮৮','৮৯','৯০','৯১','৯২','৯৩','৯৪','৯৫','৯৬','৯৭','৯৮','৯৯','১০০']

chapter_title_ordinal = ['শুন্য', 'প্রথম', 'দ্বিতীয়', 'তৃতীয়', 'চতুর্থ', 'পঞ্চম', 'ষষ্ঠ', 'সপ্তম', 'অষ্টম', 'নবম',
                         'দশম', 'একাদশ', 'দ্বাদশ', 'ত্রয়োদশ', 'চতুর্দশ', 'পঞ্চদশ', 'ষোড়শ', 'সপ্তদশ', 'অষ্টাদশ',
                         'ঊনবিংশ', 'বিংশ', 'একবিংশ', 'দ্বাবিংশ', 'ত্রয়োবিংশ', 'চতুর্বিংশ', 'পঞ্চবিংশ', 'ষট্‌বিংশ',
                         'সপ্তবিংশ', 'অষ্টাবিংশ', 'ঊনত্রিংশ', 'ত্রিংশ', 'একত্রিংশ', 'দ্বাত্রিংশ', 'ত্রয়োত্রিংশ',
                         'চতুর্ত্রিংশ', 'চতুর্ত্রিংশ', 'ষট্‌ত্রিংশ', 'সপ্তত্রিংশ', 'অষ্টাত্রিংশ', 'ঊনচত্বারিংশ',
                         'চত্বারিংশ', 'একচত্বারিংশ', 'দ্বিচত্বারিংশ', 'ত্রয়শ্চত্বারিংশ', 'চতুঃচত্বারিংশ',
                         'পঞ্চচত্বারিংশ', 'ষট্‌চত্বারিংশ', 'সপ্তচত্বারিংশ', 'অষ্টচত্বারিংশ', 'ঊনপঞ্চাশৎ', 'পঞ্চাশৎ', '৫১', '৫২', '৫৩', '৫৪', '৫৫', '৫৬', '৫৭', '৫৮', '৫৯', '৬০', '৬১', '৬২', '৬৩',
                        '৬৪', '৬৫', '৬৬', '৬৭', '৬৮', '৬৯', '৭০','৭১','৭২','৭৩','৭৩','৭৪','৭৫','৭৬','৭৭','৭৮','৭৯','৮০','৮১','৮২','৮৩','৮৪','৮৫','৮৬','৮৭','৮৮','৮৯','৯০','৯১','৯২','৯৩','৯৪','৯৫','৯৬','৯৭','৯৮','৯৯','১০০']

chapter_title_word = ['শুন্য', 'এক', 'দুই', 'তিন', 'চার', 'পাঁচ', 'ছয়', 'সাত', 'আট', 'নয়', 'দশ', 'এগারো', 'বারো',
                      'তেরো', 'চৌদ্দ', 'পনেরো', 'ষোল', 'সতেরো', 'আঠারো', 'উনিশ', 'কুড়ি', 'একুশ', 'বাইশ', 'তেইশ',
                      'চব্বিশ', 'পঁচিশ', 'ছাব্বিশ', 'সাতাশ', 'আঠাশ', 'ঊনত্রিশ', 'ত্রিশ', 'একত্রিশ', 'বত্রিশ', 'তেত্রিশ',
                      'চৌত্রিশ', 'পঁয়ত্রিশ', 'ছত্রিশ', 'সাঁয়ত্রিশ', 'আটত্রিশ', 'ঊনচল্লিশ', 'চল্লিশ', 'একচল্লিশ',
                      'বিয়াল্লিশ', 'তেতাল্লিশ', 'চুয়াল্লিশ', 'পঁয়তাল্লিশ', 'ছেচল্লিশ', 'সাতচল্লিশ', 'আটচল্লিশ',
                      'ঊনপঞ্চাশ', 'পঞ্চাশ', 'একান্ন', 'বাহান্ন', 'তিপ্পান্ন', 'চুয়ান্ন', 'পঞ্চান্ন', 'ছাপ্পান্ন', 'সাতান্ন''আটান্ন', 'ঊনষাট', 'ষাট', 'একষট্টি', 'বাষট্টি', 'তেষট্টি',
                        '৬৪', '৬৫', '৬৬', '৬৭', '৬৮', '৬৯', '৭০','৭১','৭২','৭৩','৭৩','৭৪','৭৫','৭৬','৭৭','৭৮','৭৯','৮০','৮১','৮২','৮৩','৮৪','৮৫','৮৬','৮৭','৮৮','৮৯','৯০','৯১','৯২','৯৩','৯৪','৯৫','৯৬','৯৭','৯৮','৯৯','১০০']


def prettify(html):
    html_soup = BeautifulSoup(html, features="lxml")
    return html_soup.prettify()


def get_format(chapter_url):
    response = requests.get(chapter_url)
    soup = BeautifulSoup(response.text, features="lxml")
    chapter = soup.find('span', class_="current-item").string

    if chapter[:4] == '০১. ' or chapter[:4] == '০০. ' or chapter[:4] == '১.০১':
        chapter_title_format = 'first'
    elif chapter[:3] == '১. ' or chapter[:3] == '০. ' or chapter[:3] == '১.১':
        chapter_title_format = 'one'
    elif chapter[-4:] == '– ০১' or chapter[-4:] == '– ০০':
        chapter_title_format = 'last'
    else:
        chapter_title_format = 'full'

    title = soup.find('a', rel='tag').string

    if '(' in title:
        i = title.find('(')
        title = title[:i-1]

    print("BOOK : " + title)
    print("format : " + chapter_title_format)

    # if input() == 'n':
        # title = input()

    return chapter_title_format, title


def parse_chapter(chapter_url, chapter_format='full', book_title='book', i=1,serial=1,flag=False):
    response = requests.get(chapter_url)
    soup = BeautifulSoup(response.text, features="lxml")

    title = soup.find('a', rel='tag').string
    chapter = soup.find('span', class_="current-item").string
    # chapter_number = str(i)
    # chapter_text = chapter

    try:
        previous_url = soup.find('a', rel='prev').get('href')
        # print(previous_url)
    except:
        previous_url = ''
        # print("First Chapter ... No previous Link")

    try:
        next_url = soup.find('a', rel='next').get('href')
        # print(next_url)
    except:
        next_url = ''
        # print("Last Chapter ... No next link")

    if chapter_format == 'first':
        (chapter_number, chapter_text) = (chapter[:2], chapter[4:])
    elif chapter_format == 'one':
        (chapter_number, chapter_text) = (chapter[0], chapter[3:])
    elif chapter_format == 'last' and next_url != '':
        (chapter_number, chapter_text) = (chapter[-2:], chapter[:-4])
    elif chapter_format == 'last' and next_url == '':
        chapter = chapter.replace(' (শেষ)', '')
        (chapter_number, chapter_text) = (chapter[-2:], chapter[:-4])
    else:
        # chapter_number, chapter_text = str(i).zfill(2), chapter
        chapter_number, chapter_text = '', chapter

    soup.find("div", class_='scriptlesssocialsharing').decompose()
    try:
        soup.find("img").decompose()
    except:
        pass
    body = soup.find("div", class_="entry-content")
    body['class'] = 'body-style'

    # flag = True
    file_name = 'chapter-' + str(serial).zfill(3) + str(i).zfill(3) + ".xhtml"
    # file_name = file_name.replace(' ', '_')
    fw = open("book/" + file_name, 'w', encoding='utf-8')
    # ................................................................................
    if chapter_format == "first" or chapter_format == "one":
        temp_head = chapter_text
        temp_number = chapter_title_ordinal[i]
        temp_title = chapter_text

    elif chapter_format == "last" or flag == True:
        temp_head = book_title
        temp_number = book_title
        temp_title = chapter_title_ordinal[i]

    # elif chapter_format == 'full':
    else:
        temp_head = chapter_text
        temp_number = chapter_title_number[i]
        temp_title = chapter_text

    # ................................................................................

    head = r'<?xml version="1.0" encoding="utf-8"?><!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops"><head><title>'
    fw.write(head)
    fw.write(book_title)
    fw.write( r'</title><link href="../Styles/style.css" type="text/css" rel="stylesheet"/></head><body>')

    if temp_number:
        fw.write(r'<h2 class="right sigil_not_in_toc hh1">' + temp_number + '</h2>')
    fw.write(r'<br/><h2 class="chapter darkblue hh1">' + temp_title + '</h2>\n<hr/>\n<br/><br/>')

    # .replace("<br/>","<br/><br/>"))
    fw.write(str(body).replace("</p>", "</p><br/>"))
    fw.write(r'</body></html>')
    fw.close()

    fr = open("book/" + file_name, encoding='utf-8')
    html = prettify(fr.read())
    fr.close()

    fw = open("book/" + file_name, 'w', encoding='utf-8')
    fw.write(html)
    fw.close()

    return next_url


def from_first_chapter(first_chapter_url, i=1, book='', writer='UNKNOWN',serial=1,flag = False):
    url = first_chapter_url

    chapter_format, book_title = get_format(url)

    with open("title.txt",'a',encoding='utf-8') as file:
        file.write(book_title+"\n")

    with open('res/about-07-start.xhtml', encoding='utf-8') as f:
        with open('book/chapter-' + str(serial).zfill(3) + '000-start.xhtml', 'w', encoding='utf-8') as file:
            temp = f.read()
            temp = temp.replace('dummy-title', book_title)
            file.write(temp)

    while url != '':
        # print(f'{str(i).zfill(2)} {url}')
        url = parse_chapter(url, chapter_format, book_title, i,serial,flag)
        i += 1

    with open('res/finish.xhtml', encoding='utf-8') as f:
        with open("book/"+'chapter-' + str(serial).zfill(3) + '999.xhtml', 'w', encoding='utf-8') as file:
            file.write(f.read())


def parse_book(book_url, i=1, book='', writer='UNKNOWN',serial=1,flag =False):
    response = requests.get(book_url)
    soup = BeautifulSoup(response.text, features="lxml")

    first_chapter_url = soup.find(class_="more-link").get('href')

    from_first_chapter(first_chapter_url, i, book, writer,serial,flag)
