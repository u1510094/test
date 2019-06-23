from rest_framework.authentication import TokenAuthentication


class GetTokenAuthentication(TokenAuthentication):
    def authenticate(self, request):
        if 'token' in request.GET:
            return self.authenticate_credentials(request.GET.get('token'))
