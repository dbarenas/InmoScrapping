#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests


def fotocasa(url, typeResult):
    req = requests.get(url)

    statusCode = req.status_code
    htmlText = req.text

    # Comprobamos que la petición nos devuelve un Status Code = 200
    statusCode = req.status_code

    res = []
    if statusCode == 200:
        # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
        html = BeautifulSoup(req.text, "lxml")

        if typeResult == 'page':
            pagina = html.find_all('div', {'class': 'sui-Pagination'})
            for j, pagina in enumerate(pagina):
                listpag = pagina.getText().split('...')[1].replace('>', '')
            limitPage = range(1, int(listpag))
            return limitPage

        elif typeResult == 'results':
            pagina = html.find_all('div', {'class': 're-Card-link'})
            for j, pagina in enumerate(pagina):
                dicto = {}
                title = pagina.find(
                    'a', {'class': 're-Card-title'}).getText().encode('utf-8')
                approxAddress = title.split(' en ')[1]
                tipo = title.split(' ')[0]
                rootLink = pagina.find('a', {'class': 're-Card-title'})['href']
                try:
                    price = pagina.find(
                        'span', {'class': 're-Card-price'}).getText().encode('utf-8').split('€')[0]
                except AttributeError:
                    price = 0
                info = pagina.find(
                    'span', {'class': 're-Card-feature'}).getText().encode('utf-8').split(' ')[0]
                info2 = pagina.find_all('span', {'class': 're-Card-feature'})
                if len(info2) == 2:
                    info2 = info2[1].getText().split(' ')[0]
                dicto = {'title': title, 'approxAddress': approxAddress, 'tipo': tipo,
                         'link': rootLink, 'price': price, 'nrooms': info, 'm2': info2}
                res.append(dicto)
            return res


def main():
    #url = "http://www.fotocasa.es/es/comprar/casas/espana/todas-las-zonas/l?text=46120"
    url = "http://www.fotocasa.es/es/comprar/casas/valencia-provincia/horta-nord/l"
    res = fotocasa(url, 'results')  # result over the page crawled
    pages = fotocasa(url, 'page')  # number of pages
    cont = 0
    for i in pages:
        cont = cont+1
        urlParse = url+'/'+str(i)+''

        for j in fotocasa(urlParse, 'results'):
            print j

        if cont == 1:
            break

if __name__ == '__main__':
    main()
