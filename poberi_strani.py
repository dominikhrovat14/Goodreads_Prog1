import orodja
import re
import requests 
stevilo_strani = 1
count = 0
autorji = []
ocene = []
vsi_podatki = []
ilustratorji = []
genre = []



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

vzorec_autor = (
    r'https://www.goodreads.com/author/show/(?P<autorID>.*?)\D*"><span itemprop="name">'
    r'(?P<autor>.*?)</span>'
    )

vzorec_knjiga = (
    r'<span itemprop=\'name\' role=\'heading\' aria-level=\'4\'>'
    r'(?P<naslov>.*)</span>'
    )

vzorec_ocena = (
    r'</span></span> (?P<ocena>.*?) avg rating &mdash; (?P<glasovi>.*?) ratings</span>'
    )


vzorec_ilustrator = (
    r'<h1 id="bookTitle" class="gr-h1 gr-h1--serif" itemprop="name">\n'
    r'(\s*)(?P<naslov>.*)\n'
    r'</h1>(\n.*)+\n'
    r"<div class='authorName__container'>\n"
    r'(.*)<span itemprop="name">(?P<avtor>.*)</span></a>(.*)?\n'
    r'</div>\n'
    r"(.*)\n"
    r'(.*)<span itemprop="name">'
    r'(?P<ilustrator>.*)</span></a>'
    )

vzorec_genre = (
    r'\s*<div class="elementList ">\n'
    r'\s*<div class="left">\n'
    r'\s*<a class="(.*)">(?P<genre>.*)</a>\n'
    r'\s*</div>\n'
    r'\s*<div class="right">\n'
    r'\s*<a title="(.*)">(?P<genre_glasovi>.*)\susers</a>'
    )


for stran in range(stevilo_strani):
    page_number = 1 + stran 
    url = f'https://www.goodreads.com/list/show/1.Best_Books_Ever?page={page_number}'
    datoteka = f'najbolj-znane-knjige-stran/{page_number}.html'
    vsebina = orodja.vsebina_datoteke(datoteka)
    #orodja.shrani_spletno_stran(url, datoteka)
    for podatek in re.finditer(vzorec_title, vsebina):
        link = podatek.groupdict()
        url_1 = f'https://www.goodreads.com/book/show/{link["povezava"]}.html'
        datoteka_1 = f'posamezne_knjige/{link["povezava"]}.html'
        vsebina_1 = orodja.vsebina_datoteke(datoteka_1)
        #orodja.shrani_spletno_stran(url_1, datoteka_1)
##        for zadetek in re.finditer(vzorec_autor, vsebina):
##            autorji.append(zadetek.groupdict().copy())
##
##        for zadetek in re.finditer(vzorec_ocena, vsebina):
##            ocene.append(zadetek.groupdict().copy())
##
##        for zadetek in re.finditer(vzorec, vsebina):
##            vsi_podatki.append(zadetek.groupdict().copy())
##        for podatek in re.finditer(vzorec_ilustrator, vsebina_1):
##            for zadetek in re.finditer(vzorec_ilustrator, vsebina_1):
##                ilustratorji.append(zadetek.groupdict())
        for zadetek in re.finditer(vzorec_genre, vsebina_1):
            genre.append(zadetek.groupdict())

print(genre)
    
    
##orodja.zapisi_csv(autorji, ['autorID', 'autor'], 'obdelani-podatki/autorji.csv')
##orodja.zapisi_csv(ocene, ['ocena', 'glasovi'], 'obdelani-podatki/ocene.csv')
##orodja.zapisi_csv(vsi_podatki, ['naslov', 'autorID', 'autor', 'ocena', 'glasovi'], 'obdelani-podatki/vsi_podatki.csv')
##orodja.zapisi_csv(ilustratorji, ['naslov', 'avtor', 'ilustrator'], 'obdelani-podatki/ilustratorji.csv')
orodja.zapisi_csv(genre, ['genre', 'genre_glasovi'], 'obdelani-podatki/genre.csv')

    

      


            



        



    
    
