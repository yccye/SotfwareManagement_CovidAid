from django.urls import path
from . import views
app_name = 'statistic'
urlpatterns = [
    path('covid-19/ctmap', views.CtView.as_view(),name = 'covid_19_ctmap'),
    path('covid-19/csmap', views.CsView.as_view(),name = 'covid_19_csmap'),
    path('covid-19/fimap', views.CdView.as_view(),name = 'covid_19_fimap'),
    path('covid-19/gtmap', views.GtView.as_view(),name = 'covid_19_gtmap'),
    path('covid-19/gsmap', views.GsView.as_view(),name = 'covid_19_gsmap'),
    path('covid-19/ftemap', views.GdView.as_view(),name = 'covid_19_ftemap'),
    path('covid-19',views.IndexView.as_view(),name = 'covid_19'),
    path('covid-19/update',views.update,name = 'covid_19_update'),
]
