from rest_framework import viewsets
from rest_framework import permissions

"""
This class is here to allow setting permissions per action
see https://stackoverflow.com/questions/35970970/django-rest-framework-permission-classes-of-viewset-method
"""
class BaseModelViewSet(viewsets.ModelViewSet):
    queryset = ''
    serializer_class = ''
    permission_classes = (permissions.AllowAny,)

    # Refer to https://stackoverflow.com/a/35987077/1677041
    permission_classes_by_action = {
        'create': permission_classes,
        'list': permission_classes,
        'retrieve': permission_classes,
        'update': permission_classes,
        'destroy': permission_classes,
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            if self.action:
                action_func = getattr(self, self.action, {})
                action_func_kwargs = getattr(action_func, 'kwargs', {})
                permission_classes = action_func_kwargs.get('permission_classes')
            else:
                permission_classes = None

            return [permission() for permission in (permission_classes or self.permission_classes)]