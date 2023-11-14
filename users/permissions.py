from rest_framework.permissions import BasePermission


class IsThatUser(BasePermission):
    def has_permission(self, request, view):
        return request.user == view.queryset.get(pk=view.kwargs['pk'])
