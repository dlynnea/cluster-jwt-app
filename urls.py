from django.contrib import admin
from django.urls import include, path
# from conduit.core import views

# from django.urls import path, include
# from rest_framework import routers
# from conduit.apps.authentication import views
# from conduit.views import views
# from conduit.apps.views import UserViewSet
# from api.views import CreateUserView
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/', views.index, name='index'),
    # path('home/', views.index, name='index'),
    # path('signup/', views.signup, name='signup'),
    # path('create/', CreateUserView.as_view()),
    # path('', include(router.urls)),
    path('api/', include('conduit.apps.authentication.urls', namespace='authentication')),
]
