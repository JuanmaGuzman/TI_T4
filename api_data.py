import requests
import math



def get_trays():
    trays_list = []
    url = 'https://tarea-4.2022-1.tallerdeintegracion.cl/trays'
    response = requests.get(url)
    content = response.json()

    if response.status_code == 200:
        actual_page = int(content['page'])
        total_pages = math.ceil(int(content['total']) / 50)

        while actual_page <= total_pages:
            loop_response = requests.get(url, params={'page': actual_page})
            loop_content = loop_response.json()
            actual_page += 1

            for tray in loop_content['items']:
                trays_list.append([tray['id'], tray['name'], tray['price']])

    else:
        trays_list.append([None, None, None])

    return trays_list
    

def get_espepcific_tray(id):
    tray_list = []
    url = f'https://tarea-4.2022-1.tallerdeintegracion.cl/trays/{id}'
    response = requests.get(url)

    if response.status_code == 200:
        content = response.json()
        tray_list.append([content['id'], content['name'], content['description'], content['expiration'], content['price'], content['size']])

        for course in content['courses']:
            tray_list.append([course['id'], course['name'], course['category'], course['img_url']])

    else:
        tray_list.append([None, None])

    return tray_list


def get_courses():
    courses_list = []
    url = 'https://tarea-4.2022-1.tallerdeintegracion.cl/courses'
    response = requests.get(url)
    content = response.json()

    if response.status_code == 200:
        actual_page = int(content['page'])
        total_pages = math.ceil(int(content['total']) / 50)

        while actual_page <= total_pages:
            loop_response = requests.get(url, params={'page': actual_page})
            loop_content = loop_response.json()
            actual_page += 1

        for course in loop_content['items']:
            courses_list.append([course['id'], course['name'], course['price']])
    
    else:
        courses_list.append([None, None, None])

    return courses_list
    

def get_espepcific_course(id):
    course_list = []
    url = f'https://tarea-4.2022-1.tallerdeintegracion.cl/courses/{id}'
    response = requests.get(url)

    if response.status_code == 200:
        content = response.json()
        course_list.append([content['id'], content['name'], content['description'], content['expiration'], content['price'], content['size']])

        for course in content['ingredients']:
            course_list.append([course['id'], course['name'], course['quantity']])

    else:
        course_list.append([None, None])

    return course_list


def get_ingredients():
    ingredients_list = []
    url = 'https://tarea-4.2022-1.tallerdeintegracion.cl/ingredients'
    response = requests.get(url, params={'page': 1})
    content = response.json()

    if response.status_code == 200:
        actual_page = int(content['page'])
        total_pages = math.ceil(int(content['total']) / 50)

        while actual_page <= total_pages:
            print(actual_page)
            loop_response = requests.get(url, params={'page': actual_page})
            loop_content = loop_response.json()
            print(f"aca: {len(loop_content['items'])}")
            actual_page += 1
        
            for ingredient in loop_content['items']:
                ingredients_list.append([ingredient['id'], ingredient['name'], ingredient['price']])

    else:
        ingredients_list.append([None, None, None])

    return ingredients_list
    

def get_espepcific_ingredient(id):
    ingredient_list = []
    url = f'https://tarea-4.2022-1.tallerdeintegracion.cl/ingredients/{id}'
    response = requests.get(url)

    if response.status_code == 200:
        content = response.json()
        ingredient_list.append([content['id'], content['name'], content['description'], content['expiration'], content['price'], content['size']])

    else:
        ingredient_list.append([None])

    return ingredient_list


def search_tray(name):
    items = []
    url = 'https://tarea-4.2022-1.tallerdeintegracion.cl/search/trays'
    response = requests.get(url, params={'name': name})
    content = response.json()

    if response.status_code == 200:
        if len(content) == 0:
            items.append([None, None, None])
        else:
            for tray in content:
                items.append([tray['id'], tray['name'], tray['price'], "bandeja"])

    else:
        items.append([None, None, None])

    return items


def search_course(name):
    items = []
    url = 'https://tarea-4.2022-1.tallerdeintegracion.cl/search/courses'
    response = requests.get(url, params={'name': name})
    content = response.json()

    if response.status_code == 200:
        if len(content) == 0:
            items.append([None, None, None])
        else:
            for course in content:
                items.append([course['id'], course['name'], course['price'], "plato"])

    else:
        items.append([None, None, None])

    return items


def search_ingredient(name):
    items = []
    url = 'https://tarea-4.2022-1.tallerdeintegracion.cl/search/ingredients'
    response = requests.get(url, params={'name': name})
    content = response.json()

    if response.status_code == 200:
        if len(content) == 0:
            items.append([None, None, None])
        else:
            for i in content:
                items.append([i['id'], i['name'], i['price'], "ingrediente"])

    else:
        items.append([None, None, None])

    return items


