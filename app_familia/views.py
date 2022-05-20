from django.http import HttpResponse
from app_familia.models import Familiar


# Vista Index
def index(request):
    familiares = Familiar.objects.all()
    return HttpResponse(familiares)


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
