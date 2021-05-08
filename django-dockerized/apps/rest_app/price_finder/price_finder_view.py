from rest_framework.views import APIView
from rest_framework.response import Response
from .parser import get_prices


class PriceFinderAPIView(APIView):
    def get(self, request):
        product_name = request.query_params.get("product")
        return Response(get_prices(product_name))
