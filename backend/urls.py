from django.urls import path
from .views import gas_alert
#
# from .views import (
#     CustomUserViewSet,
#     BuildingViewSet,
#     SensorViewSet,
#     SensorReadingViewSet,
#     DilutionActionViewSet, gas_alert
# )
#
# router = DefaultRouter()
# router.register(r'users', CustomUserViewSet)
# router.register(r'buildings', BuildingViewSet)
# router.register(r'sensors', SensorViewSet)
# router.register(r'readings', SensorReadingViewSet, basename='sensorreading')
# router.register(r'actions', DilutionActionViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    # path('readings/alert/', SensorReadingViewSet.as_view({'post': 'alert'}), name='gas-alert'),
    path('gas-alert/', gas_alert),
    # custom ESP32 endpoint
    #
    # # Djoser Auth (Token based)
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.authtoken')),
]
