from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class JWTAuthentication(JSONWebTokenAuthentication):

    def get_jwt_value(self, request):
        value = super().get_jwt_value(request)
        if value is None:
            value = request.query_params.get('jwt')

        return value
