#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
from app import app
from flask.json import jsonify
import json


@app.route('/')
@app.route('/index')
def scrap():
    # url = "http://www.fotocasa.es/es/comprar/casas/alboraya/alboraya-centro/l"
    # req = requests.get(url)

    # statusCode = req.status_code
    # htmlText = req.text

    # # Comprobamos que la petición nos devuelve un Status Code = 200
    # statusCode = req.status_code

    # results = []
    # if statusCode == 200:
    #     # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
    #     html = BeautifulSoup(req.text, "lxml")

    #     pagina = html.find_all('div', {'class': 're-Card-link'})
    #     for j, pagina in enumerate(pagina):
    #         dicto = {}

    #         # print j,pagina
    #         title = pagina.find(
    #             'a', {'class': 're-Card-title'}).getText().encode('utf-8')
    #         tipo = title.split(' ')[0]
    #         rootLink = pagina.find('a', {'class': 're-Card-title'})['href']
    #         price = pagina.find('div', {'class': 're-Card-priceContainer--price'}).getText().encode('utf-8').split(' ')[0]
    #         info = pagina.find('span', {'class': 're-Card-feature'}).getText().encode('utf-8').split(' ')[0]
    #         info2 = pagina.find_all('span', {'class': 're-Card-feature'})
    #         if len(info2) == 2:
    #             info2 = info2[1].getText().split(' ')[0]
    #         dicto = {'tipo': tipo, 'link': rootLink, 'price': price, 'nrooms': info, 'm2': info2}
    #         results.append(dicto)

    req_data = {}
    req_data['tipo'] = 40
    req_data['link'] = 43
    req_data['nrooms'] = 444

    return json.dumps(req_data, indent=2)


def index():
    return scrap()