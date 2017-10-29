from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls import url


router = routers.DefaultRouter()

urlpatterns = router.urls + [
    url(r'^tokens/', obtain_jwt_token),
]
