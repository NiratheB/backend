from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json
from backend.models import Shape


def get_models():
    spheres = Shape.objects.values('type', 'color', 'attributes')
    return {'spheres': list(spheres)}


def create_model(data):

    try:
        json_data = json.loads(data)
        new_shape = Shape(type=json_data['type'], color= json_data['color'],
                          attributes=json_data['attributes'])
        new_shape.save()
        return {'success':True}
    except Exception as e:
        return {'success':False, 'message': str(e)}


@csrf_exempt
def process_models(request):
    if request.method == 'POST':
        response = create_model(request.body)
    else:
        response = get_models()

    return JsonResponse(response)


