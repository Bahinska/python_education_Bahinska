from rest_framework import status, filters
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from product.serializers import ProductSerializer
from product.models import Product


class ProductListView(ListAPIView):
    # queryset and serializer for "GET" auto-define
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    http_method_names = ["get", "post"]

    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ["ID", "title", "image_url",
                     "price", "created_at", "updated_at"
                     ]

    def post(self, request):
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


class ProductDetailView(APIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    @staticmethod
    def get_object(identifier):
        #Helper method, looking for certificate with some id
        try:
            return Product.objects.get(ID=identifier)
        except Product.DoesNotExist:
            return None

    def get(self, request, pk):
        certificate = self.get_object(pk)
        if certificate is None:
            return Response({"status": 404,
                             "message": "Product not found"},
                            status=status.HTTP_404_NOT_FOUND)

        else:
            serializer = ProductSerializer(certificate)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        product = self.get_object(pk)
        if product is None:
            return Response({"status": 404,
                             "message": "Product not found"},
                            status=status.HTTP_404_NOT_FOUND)

        product_data = JSONParser().parse(request)
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

    def delete(self, request, pk):
        certificate = self.get_object(pk)
        if certificate is None:
            return Response({"status": 404,
                             "message": "Product not found"},
                            status=status.HTTP_404_NOT_FOUND)
        else:
            certificate.delete()
            return Response({"status": 200,
                             "message": "Successfully deleted!"},
                            status=status.HTTP_200_OK)

