from django.urls import path

from clinics.views import *

urlpatterns = [
    path('actions/', ActionListAPIView.as_view(), name='actions'),
    path('online-appointments/', OnlineAppointmentCreateAPIView.as_view(), name='online-appointments'),
    path('news-categories/', NewsCategoryListAPIView.as_view(), name='news-categories'),
    path('news/<int:pk>/', NewsDetailAPIView.as_view(), name='news-detail'),
    path('specialists/', SpecialistListAPIView.as_view(), name='specialist-list'),
    path('contact-chief-doctor/', ContactChiefDoctorCreateAPIView.as_view(), name='contact-chief-doctor'),
    path('feedbacks/', FeedbackListAPIView.as_view(), name='feedback'),
    path('feedbacks-create/', FeedbackCreateAPIView.as_view(), name='feedback'),
    path('about-us/', AboutUsAPIView.as_view(), name='about-us'),
    path('photogallery-categories/', PhotoGalleryCategoryListAPIView.as_view(), name='photogallery-categories'),
    path('photogalleries/', PhotoGalleryListAPIView.as_view(), name='photogalleries'),
    path('licenses/', LicenceListAPIView.as_view(), name='licenses'),
    path('specialists/<int:pk>/', SpecialistDetailAPIView.as_view(), name='specialist-detail'),
    path('vacancies/', VacancyListAPIView.as_view(), name="vacancies-list"),
    path('contacts/', ContactAPIView.as_view(), name="contacts"),
    path('story-categories/', StoryCategoriesListAPIView.as_view(), name='story-categories-detail'),
    path('home-slider/', HomeSliderListView.as_view(), name='home-slider'),

]