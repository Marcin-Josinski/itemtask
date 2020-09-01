from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class ItemCreateView(APIView):
    def post(self, request: Request) -> Response:
        return Response(status=status.HTTP_204_NO_CONTENT)
