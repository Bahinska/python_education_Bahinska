"""
Almost everything about Swagger endpoints documentation
"""
from drf_yasg import openapi

class SwaggerDocDicts:
    PRODUCT_EXAMPLE = {
        "ID": "string",
        "title": "string",
        "image_url": "string",
        "price": "number",
        "created_at": "yyyy-mm-dd",
        "updated_at": "yyyy-mm-dd"
    }

    PRODUCT_NOT_FOUND_RESPONSE = {
        "status": 404,
        "message": "Product not found"
    }

    PRODUCT_BAD = {
        "status": 400,
        "errors": {
            "field_1": "error_1",
            "field_2": "error_2"
        }
    }

    PRODUCT_CREATE_RESPONSE = {
        "status": 200,
        "message": "Product successfully created",
        "certificate": PRODUCT_EXAMPLE
    }

    PRODUCT_UPDATE_RESPONSE = {
        "status": 200,
        "message": "Product successfully updated",
        "certificate": PRODUCT_EXAMPLE
    }

    PRODUCT_DELETE_RESPONSE = {
        "status": 200,
        "message": "Successfully deleted!"
    }

    PRODUCT_FORBIDDEN = {
        "status": 403,
        "message": "Updating id is forbidden"
    }

    PRODUCT_INPUT_PARAMETER = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "ID": openapi.Schema(type=openapi.TYPE_STRING,
                                       description='Id',
                                       max_length=9),
            "title": openapi.Schema(type=openapi.TYPE_STRING,
                                                     description='Title',
                                                     max_length=256),
            "image_url": openapi.Schema(type=openapi.TYPE_STRING,
                                            description='Image url',
                                            max_length=256),
            "price": openapi.Schema(type=openapi.TYPE_NUMBER,
                                         description='Price'),
            "cteated_at": openapi.Schema(type=openapi.TYPE_STRING,
                                       description='Date of create',
                                       format="date"),
            "updated_at": openapi.Schema(type=openapi.TYPE_STRING,
                                       description='Date of update',
                                       format="date"),
        })

class EndpointDocs:
    GET_LIST = {
        "operation_description": "Get list of all Products from database",
        "responses": {
            "200": openapi.Response(
                description="Obtain list of all products from database",
                examples={
                    "application/json": [
                        SwaggerDocDicts.PRODUCT_EXAMPLE,
                    ]
                }
            ),
        }
    }

    POST = {
        "request_body": SwaggerDocDicts.PRODUCT_INPUT_PARAMETER,
        "operation_description": "Insert new Product into a database",
        "responses": {
            "200": openapi.Response(
                description="Valid product -> write to database",
                examples={
                    "application/json": SwaggerDocDicts.PRODUCT_CREATE_RESPONSE
                }
            ),
            "400": openapi.Response(
                description="Invalid product -> discard",
                examples={
                    "application/json": SwaggerDocDicts.PRODUCT_BAD
                }
            ),
        }
    }

    GET = {
        "operation_description": "Get Product by id from database",
        "responses": {
            "200": openapi.Response(
                description="Valid id -> obtain product from database",
                examples={
                    "application/json": SwaggerDocDicts.PRODUCT_EXAMPLE
                }
            ),
            "404": openapi.Response(
                description="Invalid id -> response HTTP 404",
                examples={
                    "application/json": SwaggerDocDicts.PRODUCT_NOT_FOUND_RESPONSE
                }
            ),
        }
    }

    PUT = {
        "request_body": SwaggerDocDicts.PRODUCT_INPUT_PARAMETER,
        "operation_description": "Edit Product record by ID in database",
        "responses": {
            "200": openapi.Response(
                description="Valid id -> obtain product from database",
                examples={
                    "application/json": SwaggerDocDicts.PRODUCT_UPDATE_RESPONSE
                }
            ),
            "400": openapi.Response(
                description="Invalid product -> discard",
                examples={
                    "application/json": SwaggerDocDicts.PRODUCT_BAD
                }
            ),
            "404": openapi.Response(
                description="Invalid id -> response HTTP 404",
                examples={
                    "application/json": SwaggerDocDicts.PRODUCT_NOT_FOUND_RESPONSE
                }
            ),
            "403": openapi.Response(
                description="Change id -> response HTTP 403",
                examples={
                    "application/json": SwaggerDocDicts.PRODUCT_FORBIDDEN
                }
            ),
        }
    }

    DELETE = {
        "operation_description": "Delete Product by id from database",
        "responses": {
            "200": openapi.Response(
                description="Valid id -> delete certificate from database",
                examples={
                    "application/json": SwaggerDocDicts.PRODUCT_DELETE_RESPONSE
                }
            ),
            "404": openapi.Response(
                description="Invalid id -> response HTTP 404",
                examples={
                    "application/json": SwaggerDocDicts.PRODUCT_NOT_FOUND_RESPONSE
                }
            ),
        }
    }