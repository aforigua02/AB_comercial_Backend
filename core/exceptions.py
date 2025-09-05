from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):

    response = exception_handler(exc, context)
    if response is None:
        return Response({"error": "Internal server error."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    data = response.data

    if isinstance(data, dict):
        if "detail" in data and isinstance(data["detail"], str):
            message = data["detail"]
        elif "error" in data and isinstance(data["error"], str):
            message = data["error"]
        else:
            first_key = next(iter(data))
            first_val = data[first_key]
            if isinstance(first_val, list) and first_val and isinstance(first_val[0], str):
                message = first_val[0]
            else:
                message = str(data)
    else:
        message = str(data)

    return Response({"error": message}, status=response.status_code)
