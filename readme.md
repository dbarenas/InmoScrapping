------------------------
houser-extractor
------------------------

The requriment:

Extract house listings from fotocasa and idealista, provide a web services with login for get the info with a simple http login.

JAN 19 2017 viclopla [11:16 AM] 
Tipo de Inmueble (Casa, piso, trastero...), rango de precios, Habitaciones, baños, rango de superficie en m2 y por último, localización entendiendo que es un radio en km desde la posición del inmueble que se toma como referencia

Instructions of use:

1. Create a virtualenv


```
	virtualenv env
	source env/bin/activate 
```
2. Install the requeriments.txt file
```
	pip install -r requeriments.txt
```

#NOTE - 02/03/2017  - For this actual version

3. Install the firefox version inside the file
```
	python idealista.py	
	python fotocasa.py
```

```

	[{'nrooms': u'4', 'price': ' 600.000', 'link': '/inmueble/33930628/', 'tipo': 'Piso', 'm2': '231'}, {'nrooms': u'6', 'price': ' 700.000', 'link': '/inmueble/33930500/', 'tipo': 'Piso', 'm2': '262'}, {'nrooms': u'5', 'price': ' 695.000', 'link': '/inmueble/33930627/', 'tipo': 'Piso', 'm2': '240'}, {'nrooms': u'3', 'price': ' 595.000', 'link': '/inmueble/33930770/', 'tipo': '\xc3\x81tico', 'm2': '145'}, {'nrooms': u'2', 'price': ' 699.900', 'link': '/inmueble/35280981/', 'tipo': 'Casa', 'm2': '458'}, {'nrooms': u'5', 'price': ' 690.000', 'link': '/inmueble/33307360/', 'tipo': 'Piso', 'm2': '224'}, {'nrooms': u'4', 'price': ' 345.000', 'link': '/inmueble/35080649/', 'tipo': 'Piso', 'm2': '160'}, {'nrooms': u'1', 'price': ' 123.000', 'link': '/inmueble/35603943/', 'tipo': 'Piso', 'm2': '60'}, {'nrooms': u'5', 'price': ' 690.000', 'link': '/inmueble/34747929/', 'tipo': 'Piso', 'm2': '241'}, {'nrooms': u'5', 'price': ' 625.000', 'link': '/inmueble/28932919/', 'tipo': 'Piso', 'm2': '340'}, {'nrooms': u'4', 'price': ' 890.000', 'link': '/inmueble/34700340/', 'tipo': 'Piso', 'm2': '288'}, {'nrooms': u'7', 'price': ' 995.000', 'link': '/inmueble/29199572/', 'tipo': 'Piso', 'm2': '300'}, {'nrooms': u'3', 'price': ' 595.000', 'link': '/inmueble/33754716/', 'tipo': '\xc3\x81tico', 'm2': '145'}, {'nrooms': u'3', 'price': ' 390.000', 'link': '/inmueble/30850646/', 'tipo': 'Piso', 'm2': '198'}, {'nrooms': u'4', 'price': ' 390.000', 'link': '/inmueble/35220543/', 'tipo': '\xc3\x81tico', 'm2': '120'}, {'nrooms': u'4', 'price': ' 145.000', 'link': '/inmueble/35716638/', 'tipo': 'Piso', 'm2': '119'}, {'nrooms': u'4', 'price': ' 600.000', 'link': '/inmueble/30418218/', 'tipo': 'Piso', 'm2': '231'}, {'nrooms': u'3', 'price': ' 382.000', 'link': '/inmueble/34825395/', 'tipo': 'Piso', 'm2': '118'}, {'nrooms': u'2', 'price': ' 330.000', 'link': '/inmueble/29540095/', 'tipo': 'Piso', 'm2': '100'}, {'nrooms': u'4', 'price': ' 178.000', 'link': '/inmueble/31816259/', 'tipo': 'Piso', 'm2': '118'}, {'nrooms': u'4', 'price': ' 390.000', 'link': '/inmueble/27195037/', 'tipo': '\xc3\x81tico', 'm2': '114'}, {'nrooms': u'2', 'price': ' 186.000', 'link': '/inmueble/35260222/', 'tipo': 'Piso', 'm2': '90'}, {'nrooms': u'1', 'price': ' 250.000', 'link': '/inmueble/31908003/', 'tipo': 'Piso', 'm2': '70'}, {'nrooms': u'3', 'price': ' 265.000', 'link': '/inmueble/33531167/', 'tipo': 'Piso', 'm2': '85'}, {'nrooms': u'4', 'price': ' 320.000', 'link': '/inmueble/35263094/', 'tipo': 'Piso', 'm2': '180'}, {'nrooms': u'4', 'price': ' 240.000', 'link': '/inmueble/31704973/', 'tipo': 'Piso', 'm2': '129'}, {'nrooms': u'5', 'price': ' 435.000', 'link': '/inmueble/35555660/', 'tipo': 'Piso', 'm2': '212'}, {'nrooms': u'2', 'price': ' 215.000', 'link': '/inmueble/34816695/', 'tipo': 'Piso', 'm2': '95'}, {'nrooms': u'7', 'price': ' 485.000', 'link': '/inmueble/32336804/', 'tipo': 'Piso', 'm2': '286'}, {'nrooms': u'5', 'price': ' 255.000', 'link': '/inmueble/33944915/', 'tipo': 'Piso', 'm2': '135'}]

```

#In the file rest you can found the structure of restful service who use the scripts like functions

//Next step implement the flask restful service 

ToDo
+ Search by parameters inside the object
+ Validation of parameters
+ Integrate area parameter in a map 

