from selenium import webdriver
from slugify import slugify
import time

browser = webdriver.Firefox()

browser.get('https://create.kahoot.it/details/el-enroque/86a56c37-78c4-4680-9bf9-931bf2bc1f82')

time.sleep(3)

browser.find_element_by_class_name("question-list__group-toggle").click()

time.sleep(2)

questions = browser.find_elements_by_class_name("question-list__item")

file_title = slugify(browser.find_element_by_class_name("kahoot-title__heading").text.lower()) + '.txt'

preguntas_gift = []

with open(file_title, 'a') as file:
    for question in questions:
        textos = question.text.split('\n')
        titulo_pregunta = textos[1]

        respuesta_a = textos[3]
        a_is_correct = '=' if 'correct' in textos[4] else '~'
        
        respuesta_b = textos[5]
        b_is_correct = '=' if 'correct' in textos[6] else '~'

        respuesta_c = textos[7]
        c_is_correct = '=' if 'correct' in textos[8] else '~'

        try:
            respuesta_d = textos[9]
            d_is_correct = '=' if 'correct' in textos[10] else '~'
        except:
            respuesta_d = ''
            d_is_correct = ''

        pregunta = "::{0}\n:: {0} {{\n{1}{2}\n{3}{4}\n{5}{6}\n{7}{8}\n}}\n\n".format(
            titulo_pregunta,
            a_is_correct,
            respuesta_a,
            b_is_correct,
            respuesta_b,
            c_is_correct,
            respuesta_c,
            d_is_correct,
            respuesta_d)
        print(pregunta)
        file.write(pregunta)

