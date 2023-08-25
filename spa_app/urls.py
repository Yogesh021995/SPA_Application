from django.urls import path
from .views import sign_in, get_staff_members, save_visitor_details,get_drinks,save_visitor_drink

urlpatterns = [
    path('api/sign_in/', sign_in, name='sign-in'),
    path('api/get_staff_members/', get_staff_members, name='get-staff-members'),
    path('api/save_visitor_details/', save_visitor_details, name='save-visitor-details'),
    path('api/get_drinks/', get_drinks, name='get-drinks'),
    path('api/save_visitor_drink/', save_visitor_drink, name='save-visitor-drink'),
]