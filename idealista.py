#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup

import requests


def idealista(url, ntype):
    page = url.split('pagina-')[1].split('.')[0]

    req = requests.get(url, cert="cert.pem")

    statusCode = req.status_code
    htmlText = req.text

    # Comprobamos que la petición nos devuelve un Status Code = 200
    statusCode = req.status_code

    results = []
    if statusCode == 200:
        # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
        html = BeautifulSoup(req.text, "lxml")

        # Obtenemos todos los divs donde estan las entradas

        npage = []
        pagina = html.find_all('div', {'class': 'pagination'})
        for j, pagina in enumerate(pagina):
            res = pagina.find_all('a', {'class': ''})
            for link in res:
                npage.append(link.getText())
        size = len(npage)
        pages = range(int(page), int(npage[size-1])+1, 1)

        entradas = html.find_all('div', {'class': 'item-info-container'})
        res = []

        for i, entrada in enumerate(entradas):
            dicto = {}
            tipo = entrada.find(
                'a', {'class': 'item-link'}).getText().encode('utf-8').split(' ')
            rootLink = entrada.find('a', {'class': 'item-link'})
            title = rootLink.getText().encode('utf-8')
            approxAddress = title.split(' en')[1]
            price = entrada.find(
                'div', {'class': 'row price-row clearfix'}).getText().encode('utf-8')
            info = entrada.find('span', {'class': 'item-detail'}).getText()
            info2 = entrada.find_all('span', {'class': 'item-detail'})
            dicto = {'tipo': title.split(' en')[0], 'link': rootLink['href'], 'price': price.split('€ ')[
                0].strip(), 'nrooms': info[0], 'm2': info2[1].getText().encode('utf-8').split(' ')[0], 'approxAddress': approxAddress}
            res.append(dicto)

    if ntype == 'pages':
        return pages
    elif ntype == 'results':
        return res


def main():
    #url = "https://www.idealista.com/buscar/venta-viviendas/alboraya/pagina-10.htm"
    url = "https://www.idealista.com/buscar/venta-viviendas/con-de-dos-dormitorios,de-tres-dormitorios,de-cuatro-cinco-habitaciones-o-mas,piscina/alboraya/pagina-5.htm"
    pages = idealista(url, 'pages')
    for i in pages:
        urlParse = url.split('pagina-')[0]+'pagina-'+str(i)+'.htm'
        for j in idealista(urlParse, 'results'):
            print j

if __name__ == '__main__':
    main()

#this is the structure in HTML of the page what this script crawl
# 24 <div class="item-info-container">
#  <div class="logo-branding">
#  <a data-xiti-click="listado::logo-agencia" href="/pro/1143465681392475567-130047543/" title="Engel &amp; Völkers Valencia">
#  <div class="logo-border"></div>
#   <img alt="Engel &amp; Völkers Valencia" data-ondemand-img="https://st3.idealista.com/92/31/cc/1143465681392475567-130047543.gif" src="https://st1.idealista.com/static/common/img/icons/px.png"/> </a> </div>
#   <a class="item-link " data-xiti-click="listado::enlace" href="/inmueble/35263094/" title="Piso en La Seu, València">Piso en La Seu, València</a>
#   <div class="row price-row clearfix"> <span class="item-price">320.000<span>€</span></span> </div>
#    <span class="item-detail">4 <small>hab.</small></span>
#    <span class="item-detail">180 <small>m²</small></span>
#     <span class="item-detail">1ª <small><span>planta</span> con ascensor</small></span>
#      <p class="item-description">Cuando entramos en esta vivienda lo primero que nos impresiona es la gran luminosidad que tiene. Dos estancias con grandes ventanales con...</p>
#      <div class="item-toolbar clearfix">
#      <div class="item-toolbar-contact">
#      <span class="icon-phone item-not-clickable-phone">960 960 891</span>
#      <a class="icon-phone phone-btn item-clickable-phone" data-xiti-markup='{ "click": {"xtPage":"listado::conversiones::contacto-por-telf","mustXtn2":true,"actionType":"PAGE"} }' data-xiti-page="telf_cliente_v" href="tel:960960891" target="_blank">
#      <span>960 960 891</span> </a> <button class="icon-mail email-btn action-email fake-anchor" data-xiti-click="listado::enlace-contactar">
#      <span>Contactar</span></button> </div> <div class="item-toolbar-actions"> <button class="icon-fav favorite-btn action-fav fake-anchor" data-role="add" data-text-add="Guardar" data-text-remove="Quitar">
#      <span>Guardar</span> </button> <button class="icon-delete trash-btn action-discard fake-anchor" data-role="add" data-text-remove="Descartar" rel="nofollow">
#      <span>Descartar</span></button> </div> </div> </div>
