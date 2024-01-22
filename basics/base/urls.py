from django.urls import path
from .views import home, profile, cityaverage, HomeListView, get_all_students, StudentJSONView, StudentXMLView, StandardView

urlpatterns = [

    path('home/', home, name="home"),
    path('homeclass/', HomeListView.as_view(), name="homeclass"),
    path('profile/<int:roll_no>', profile, name="profile"),
    path('city/', cityaverage, name="city"),
    path('students/', get_all_students, name="students"),
    path('stu_api/', StudentJSONView.as_view(), name="stu_api"),
    path('stu_xml/', StudentXMLView.as_view(), name="stu_xml"),
    path('std_all/', StandardView.as_view(), name="std_all"),
]