from idealista import idealista
from fotocasa import fotocasa


def searchby(search_string):
    toLook = ['latitude', 'longitude', 'minPrice',
              'maxPrice', 'minRooms', 'minBathrooms', 'minSurface']
    fotocasa_vocabulary = ['latitude', 'longitude', 'minPrice',
                           'maxPrice', 'minRooms', 'minBathrooms', 'minSurface']
    idealista_vocabulary = ['precio-desde_', 'con-precio-hasta_', 'de-tres-dormitorios', 'de-cuatro-cinco-habitaciones-o-mas',
                            'dos-banos', 'tres-banos-o-mas', 'metros-cuadrados-mas-de_40', 'metros-cuadrados-menos-de_160']

    dicto = {}
    for param in toLook:
        for nlist in search_string.split('&'):
            if param in nlist:
                dicto[param] = nlist.split('=')[1]

    print dicto

    dict_idealista = {}

    dict_idealista['precio-desde_'] = dicto['minPrice']
    dict_idealista['con-precio-hasta_'] = dicto['maxPrice']
    dict_idealista['con-de-dos-dormitorios'] = dicto['minRooms']
    dict_idealista['de-tres-dormitorios'] = dicto['minRooms']
    dict_idealista['de-cuatro-cinco-habitaciones-o-mas'] = dicto['minRooms']
    dict_idealista['dos-banos'] = dicto['minBathrooms']
    dict_idealista['tres-banos-o-mas'] = dicto['minBathrooms']
    dict_idealista['metros-cuadrados-mas-de_40'] = dicto['minSurface']
    dict_idealista['metros-cuadrados-menos-de_160'] = dicto['minSurface']

    print dict_idealista

# url = "http://www.fotocasa.es/es/comprar/casas/valencia-provincia/horta-nord/l"
# res = fotocasa(url, 'results')  # result over the page crawled
# pages = fotocasa(url, 'page')  # number of pages

# for i in res:
#   print i

# url = "https://www.idealista.com/buscar/venta-viviendas/alboraya/pagina-10.htm"
# #url = "https://www.idealista.com/buscar/venta-viviendas/con-de-dos-dormitorios,de-tres-dormitorios,de-cuatro-cinco-habitaciones-o-mas,piscina/alboraya/pagina-5.htm"
# pages = idealista(url, 'pages')
# for i in pages:
#     urlParse = url.split('pagina-')[0]+'pagina-'+str(i)+'.htm'
#     for j in idealista(urlParse, 'results'):
#         print j

#https://maps.googleapis.com/maps/api/geocode/json?address=46120%20espa%C3%B1a&key=AIzaSyA3_pU-6LlW-sLGAmLCsqVU85Uje5Gz5EI

def main():
    search = "latitude=39.539274241677404&longitude=-0.40359793141169775&minPrice=50000&maxPrice=250000&minRooms=2&minBathrooms=2&minSurface=100"
    searchby(search)


if __name__ == '__main__':
    main()
