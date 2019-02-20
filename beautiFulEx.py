import requests # urlib
from bs4 import BeautifulSoup


def web(page,WebUrl):
    
    if(page>0):
        url = WebUrl
        
        code = requests.get(url)
        plain = code.text
        s = BeautifulSoup(plain, "html.parser")
        #<span class="a-size-small a-color-secondary"></span>
        #<span class="a-size-base a-color-price s-price a-text-bold">
        #    <span class="currencyINR">&nbsp;&nbsp;</span>23,990</span>
        
        for link in s.findAll('a',{'class':'s-access-detail-page'}):
            #for link in s.findAll('span',{'class':'a-size-base a-color-price s-price a-text-bold'}):
             #   print(link.text)
            
        
            #a-row a-spacing-none
            
            tet = link.get('title')
            print(tet)
            tet_2 = link.get('href')
            print(tet_2)
            tet_3 = link.get('class')
            print(tet_3)
            tet_4 = link.get('style')
            print(tet_4)
            for link in s.findAll('a',{'class':'a-link-normal a-text-normal'}):
                tet = link.get('href')
                print(tet)
                tet_2 = link.get('a class')
                print(tet_2)
        for link in s.findAll('span',{'class':'a-size-base a-color-price s-price a-text-bold'}):
                    print(link.text)
            
web(1,'https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=mobile')
