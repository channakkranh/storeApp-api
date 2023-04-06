# from django.urls import path
# from.import views

# urlpatterns = [
#     path('test/',views.test)

# ]
from django.urls import path
from .views import ItemList, ItemDetail,LocationList,LocationDetail

urlpatterns=[
    path('item/',ItemList.as_view()),
    path('item/<int:pk>',ItemDetail.as_view()),
    path('LocationList/',LocationList.as_view()),
    path('LocationList/<int:pk>',LocationDetail.as_view()),
]