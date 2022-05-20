from django.http import HttpResponse
from django.template import loader

from app_familia.models import Familiar


# Vista Index
def index(request):
    template = loader.get_template('app.html')
    context_dict = {
        'familiares': Familiar.objects.all()
    }
    render = template.render(context_dict)

    return HttpResponse(render)


def create(request, familiar_id):
    return HttpResponse("Formulario para agregar un Familiar")


def store(request):
    pass


def edit(request, familiar_id):
    pass


def update(request):
    pass


def delete(request, familiar_id):
    pass
