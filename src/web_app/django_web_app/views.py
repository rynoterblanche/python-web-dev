from django.views import View


class ViewWrapper(View):
    view_creator_func = None
    upload_picture_name = None

    def get(self, request, *args, **kwargs):
        kwargs.update(request.GET.dict())

        response = self.view_creator_func(request, **kwargs).get(**kwargs)
        return response
