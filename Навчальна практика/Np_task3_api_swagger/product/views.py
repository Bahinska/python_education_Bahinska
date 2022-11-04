from django.utils.decorators import method_decorator
from rest_framework import status, filters
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from product.serializers import ProductSerializer
from product.models import Product
from copy import deepcopy
from drf_yasg.utils import swagger_auto_schema
from .docs import EndpointDocs
from rest_framework.pagination import LimitOffsetPagination

@method_decorator(
    name="get",
    decorator=swagger_auto_schema(**EndpointDocs.GET_LIST)
)
class ProductListView(ListAPIView):
    """
    (List)APIView class for "GET" and "POST" methods
    from url /api/v1/products/
    "GET" is auto-defined (with filters, ordering, offset and limit) for getting products
    """
    # queryset and serializer for "GET" auto-define
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    http_method_names = ["get", "post"]

    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ["ID", "title", "image_url",
                     "price", "created_at", "updated_at"
                     ]

    #  offset and limit
    pagination_class = LimitOffsetPagination

    @swagger_auto_schema(**EndpointDocs.POST)
    def post(self, request):
        """
        "POST" HTTP-request, append database with new product
        """
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": 200,
                             "message": "Product successfully created",
                             "product": serializer.data},
                            status=status.HTTP_200_OK)
        else:
            return Response({"status": 400,
                             "errors": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)


def get_id(obj):
    serializer = ProductSerializer(deepcopy(obj))
    return serializer.data["ID"]


class ProductDetailView(APIView):
    """
    APIView class for "PUT", "GET" and "DELETE" requests
    from url /api/v1/products/<some id to perform action with>
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


    @staticmethod
    def get_object(identifier):
        """
        Helper method, looking for product with some id
        """
        try:
            return Product.objects.get(ID=identifier)
        except Product.DoesNotExist:
            return None

    @swagger_auto_schema(**EndpointDocs.GET)
    def get(self, request, pk):
        """
        "GET" HTTP-request, obtain product by id
        """
        product = self.get_object(pk)
        if product is None:
            return Response({"status": 404,
                             "message": "Product not found"},
                            status=status.HTTP_404_NOT_FOUND)

        else:
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(**EndpointDocs.PUT)
    def put(self, request, pk):
        """
        "PUT" HTTP-request, edit the existing record (by id) except id
        """
        product = self.get_object(pk)
        if product is None:
            return Response({"status": 404,
                             "message": "Product not found"},
                            status=status.HTTP_404_NOT_FOUND)

        product_data = JSONParser().parse(request)

        if get_id(product) != product_data["ID"]:
            return Response({"status": 403,
                             "message": "Updating id is forbidden"},
                            status=status.HTTP_403_FORBIDDEN)

        serializer = ProductSerializer(product, data=product_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": 200,
                             "message": "Product successfully updated",
                             "product": serializer.data},
                            status=status.HTTP_200_OK)
        else:
            return Response({"status": 400,
                             "errors": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(**EndpointDocs.DELETE)
    def delete(self, request, pk):
        """
        "DELETE" HTTP-request, delete product by id
        """
        product = self.get_object(pk)
        if product is None:
            return Response({"status": 404,
                             "message": "Product not found"},
                            status=status.HTTP_404_NOT_FOUND)
        else:
            product.delete()
            return Response({"status": 200,
                             "message": "Successfully deleted!"},
                            status=status.HTTP_200_OK)

