from django.http import HttpResponse
from django.template import Template,Context

def saludo(request): #Primera vista

    nombre="romel"

    doc_externo=open("C:/Users/Usuario/Desktop/6to Ciclo/LP3/ProyectosDjango/Proyecto1/Proyecto1/plantillas/index.html")

    plt=Template(doc_externo.read())

    doc_externo.close()

    ctx=Context({"nombre":nombre})

    documento=plt.render(ctx)

    return HttpResponse(documento)
