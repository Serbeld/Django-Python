from django.http import HttpResponse
import datetime
#from django.template import Template, Context
from django.template.loader import get_template


# Primera vista
def hello(request):

    return HttpResponse("Hello people")


def hide(request):

    return HttpResponse("Esto esta sección esta oculta, que haces aqui?? O.O")


def fecha_h(request):

    fecha = datetime.datetime.now()

    Documento = """<html>
    <body>
    <h1>
    Quieres ver la fecha???
    </h1>
    <h2>
    Aqui puedes visualizar la fecha del dia de hoy
    </h2>
    </body>
    </html>""" + str(fecha)

    return HttpResponse(Documento)


def tu_edad(request, edad, agno):

    periodo = agno - 2020
    edadFutura = edad + periodo
    Documento = """<html>
    <body>
    <h1>
    Que edad tendras en el %s???
    </h1>
    <h2>
    En el %s tendrás %s años
    </h2>
    </body>
    </html>""" % (agno, agno, edadFutura)

    return HttpResponse(Documento)


def autor(request):

    nombre = "Sergio Luis Beleño Díaz"

    #doc_externo = open("C:/Users/57314/Downloads/Django/CursoDjango/CursoDjango/Interface.html")

    #plantilla = Template(doc_externo.read())

    #doc_externo.close()

    doc_externo = get_template('Interface.html')

    #ctx = Context({"Autor": nombre})

    #documento = plantilla.render(ctx)

    documento = doc_externo.render({"Autor": nombre})

    return HttpResponse(documento)