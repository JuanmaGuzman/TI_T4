from api_data import get_espepcific_course, get_trays, get_courses, get_ingredients, get_espepcific_tray, get_espepcific_course, get_espepcific_ingredient, search_tray, search_course, search_ingredient

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/") 
def home():
    
    bandejas = []
    respuesta = get_trays()
    for item in respuesta:
        bandeja = []
        id = item[0]
        nombre = item[1]
        precio = item[2]
        bandeja.append(id)
        bandeja.append(nombre)
        bandeja.append(precio)
        bandejas.append(bandeja)

    return render_template("vista_principal.html", bandejas=bandejas)


@app.route("/platos") 
def courses():
    
    platos = []
    respuesta = get_courses()
    for item in respuesta:
        plato = []
        id = item[0]
        nombre = item[1]
        precio = item[2]
        plato.append(id)
        plato.append(nombre)
        plato.append(precio)
        platos.append(plato)

    return render_template("vista_platos.html", platos=platos)


@app.route("/ingredientes") 
def ingredientes():
    
    ingredientes = []
    respuesta = get_ingredients()
    for item in respuesta:
        ingrediente = []
        id = item[0]
        nombre = item[1]
        precio = item[2]
        ingrediente.append(id)
        ingrediente.append(nombre)
        ingrediente.append(precio)
        ingredientes.append(ingrediente)

    return render_template("vista_ingredientes.html", ingredientes=ingredientes)


@app.route("/bandeja/<id_>")
def tray(id_):

    respuesta = get_espepcific_tray(id_)
    datos = respuesta[0]
    platos = respuesta[1:]
        
    return render_template("vista_bandeja.html", datos=datos, platos=platos)


@app.route("/plato/<id_>")
def course(id_):

    respuesta = get_espepcific_course(id_)
    datos = respuesta[0]
    ingredientes = respuesta[1:]
        
    return render_template("vista_plato.html", datos=datos, ingredientes=ingredientes)


@app.route("/ingrediente/<id_>")
def ingredient(id_):

    respuesta = get_espepcific_ingredient(id_)
    datos = respuesta[0]
        
    return render_template("vista_ingrediente.html", datos=datos)


@app.route("/buscador")
def searcher():
    items = []
    name = request.args.get('search')

    res_trays = search_tray(name)
    res_courses = search_course(name)
    res_ingredients = search_ingredient(name)

    trays = res_trays[0]
    courses = res_courses[0]
    ingredients = res_ingredients[0]

    if trays == courses == ingredients == [None, None, None]:
        return "None"

    else:
        if trays != [None, None, None]:
            for item in res_trays:
                id = item[0]
                nombre = item[1]
                precio = item[2]
                tipo = item[3]
                items.append([id, nombre, precio, tipo])
        
        if courses != [None, None, None]:
            for item in res_courses:
                id = item[0]
                nombre = item[1]
                precio = item[2]
                tipo = item[3]
                items.append([id, nombre, precio, tipo])

        if ingredients != [None, None, None]:
            for item in res_ingredients:
                id = item[0]
                nombre = item[1]
                precio = item[2]
                tipo = item[3]
                items.append([id, nombre, precio, tipo])

    return render_template("searcher.html", items=items)

if __name__ == "__main__":
    #app.run()
    app.run(host="127.0.0.1", port=8000, debug=True)


