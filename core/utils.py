from rest_framework.exceptions import NotFound


def get_object_or_error(model, *args, **kwargs):
    try:
        obj = model.objects.get(*args, **kwargs)
        return obj
    except model.DoesNotExist:
        raise NotFound(detail="{} not found".format(model.__name__))
