import orodja
import re
import requests 
stevilo_strani =100
count = 0
autorji = []
ocene = []
knjige = []
ilustratorji = []
genre = []
about = []



vzorec = (
    r'<span itemprop=\'name\' role=\'heading\' aria-level=\'4\'>'
    r'(?P<naslov>.*)'
    r'</span>\n'
    r'</a>\s*<br/>\n'
    r'\s*<span class=\'by\'>by</span>\n'
    r"<span itemprop='author' itemscope='' itemtype='http://schema.org/Person'>\n"
    r"<div class='authorName__container'>\n"
    r'<a class="authorName" itemprop="url" href="'
    r'https://www.goodreads.com/author/show/(?P<autorID>.*?)\D*"><span itemprop="name">'
    r'(?P<autor>.*?)</span></a>(\s<span class="greyText">\(Goodreads Author\)</span>)?\n'
    r'</div>\n'
    r'</span>\n'
    r'\s*\n'
    r'\s*<br/>\n'
    r'\s*<div>\n'
    r'\s*<span class="greyText smallText uitext">\n'
    r'\s*<span class="minirating"><span class="stars staticStars'
    r'\s*notranslate"(\s.*)?><span size="12x12"(\sclass="staticStar p\d*")?'
    r'\s*>(.*)?</span><span size="12x12" class="staticStar p\d*"'
    r'\s*></span><span size="12x12" class="staticStar p\d*"'
    r'\s*></span><span size="12x12" class="staticStar p\d*"'
    r'\s*></span><span size="12x12" class="staticStar p\d*">'
    r'</span></span> (?P<ocena>.*?) avg rating &mdash; (?P<glasovi>.*?) ratings</span>'
)

vzorec_title = (
    r'<a title="(.*)" href="/book/show/(?P<povezava>.*)">'
    )

vzorec_knjiga = (
    r'<span itemprop=\'name\' role=\'heading\' aria-level=\'4\'>'
    r'(?P<naslov>.*)</span>'
    )


vzorec_ilustrator = (
    r'<h1 id="bookTitle" class="gr-h1 gr-h1--serif" itemprop="name">\n'
    r'(\s*)(?P<naslov>.*)\n'
    r'</h1>(\n.*)+\n'
    r"<div class='authorName__container'>\n"
    r'(.*)<span itemprop="name">(?P<autor>.*)</span></a>(.*)?\n'
    r'</div>\n'
    r"(.*)\n"
    r'((.*)<span itemprop="name">)?'
    r'((?P<ilustrator>.*)</span></a>)?\n'
    )

vzorec_genre = (
    r'\s*<div class="elementList ">\n'
    r'\s*<div class="left">\n'
    r'\s*<a class="(.*)">(?P<genre>.*)</a>\n'
    r'\s*</div>\n'
    r'\s*<div class="right">\n'
    r'\s*<a title="(.*)">(?P<genre_glasovi>.*)\susers</a>'
    )

vzorec_about = (
    r'<span itemprop="numberOfPages">(?P<dolzina>.*) pages</span></div>\n'
    r'(\s)*\n'
    r'\s*<div class="row">'
    r'\s* Published'
    r'\s*\D*(\d{0,3})?\D{0,3}\s(?P<izdano>.*)'
    r'(.*\n)*'
    r'\s*<div class="infoBoxRowItem">(?P<naslov>.*)</div>'
    r'(.*\n)*'
    r".*itemprop='inLanguage'>(?P<jezik>.*)</div>"
    )



for stran in range(stevilo_strani):
    page_number = 1 + stran
    url = f'https://www.goodreads.com/list/show/1.Best_Books_Ever?page={page_number}'
    datoteka = f'najbolj-znane-knjige-stran/{page_number}.html'
    #orodja.shrani_spletno_stran(url, datoteka)
    vsebina = orodja.vsebina_datoteke(datoteka)
    for zadetek in re.finditer(vzorec, vsebina):
        print(zadetek)
        knjige.append(zadetek.groupdict().copy())

    '''        
    for podatek in re.finditer(vzorec_title, vsebina):
        link = podatek.groupdict()
        url_posamezne = f'https://www.goodreads.com/book/show/{link["povezava"]}.html'
        datoteka_posamezne = f'posamezne_knjige/{link["povezava"]}.html'
        #orodja.shrani_spletno_stran(url_posamezne, datoteka_posamezne)
        vsebina_posamezne = orodja.vsebina_datoteke(datoteka_posamezne)
        for zadetek in re.finditer(vzorec, vsebina):
            vsi_podatki.append(zadetek.groupdict().copy())
            '''
            
'''        
        
        for zadetek in re.finditer(vzorec_autor, vsebina):
            autorji.append(zadetek.groupdict().copy())

            for zadetek in re.finditer(vzorec_ilustrator, vsebina_posamezne):
            ilustratorji.append(zadetek.groupdict().copy())

        
        for zadetek in re.finditer(vzorec_about, vsebina_posamezne):
            print(about)
            about.append(zadetek.groupdict().copy())

        
                
        for zadetek in re.finditer(vzorec_genre, vsebina_posamezne):
            genre.append(zadetek.groupdict())'''

    
    
#orodja.zapisi_csv(autorji, ['autorID', 'autor'], 'obdelani-podatki/autorji.csv')
print("SEM TU")
orodja.zapisi_csv(knjige, ['naslov', 'autorID', 'autor', 'ocena', 'glasovi'], 'obdelani-podatki/knj.csv')
#orodja.zapisi_csv(ilustratorji, ['naslov', 'autor', 'ilustrator'], 'obdelani-podatki/ilustratorji.csv')
#orodja.zapisi_csv(genre, ['genre', 'genre_glasovi'], 'obdelani-podatki/genre.csv')
#orodja.zapisi_csv(about, ['naslov', 'izdano', 'dolzina', 'jezik'], 'obdelani-podatki/splosno.csv')

    

      


            



        



    
    
