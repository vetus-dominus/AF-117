# pylint: disable=no-member
# pylint: disable=import-error
# pylint: disable=no-name-in-module
# pylint: disable=too-many-ancestors
# pylint: disable=too-few-public-methods
""" VIEW """
from django.db                 import transaction
from rest_framework            import viewsets
from rest_framework.exceptions import APIException
from library.tasks             import send_email_message
from library.models            import Booklist
from library.models            import Users
from library.serializers       import BooklistSerializer
from library.serializers       import UsersSerializer
from django.conf               import settings

class BooklistViewSet(viewsets.ModelViewSet):
    """ BooklistViewSet """
    serializer_class = BooklistSerializer
    queryset         = Booklist.objects.all()


class UsersViewSet(viewsets.ModelViewSet):
    """ UsersViewSet """
    serializer_class = UsersSerializer
    queryset         = Users.objects.all()

    def perform_create(self, serializer):
        """ perform create function """
        try:
            with transaction.atomic():
                instance = serializer.save()
                instance.save()
                message = "Hello, " + instance.name + "!\n\nI'm glad to see you on Library.it"
                transaction.on_commit(
                    lambda: send_email_message.delay(
                        instance.email,
                        settings.MAIL_FROM,
                        'Welcome to Library',
                        message
                    )
                )
        except Exception as err:
            raise APIException(str(err)) from err
