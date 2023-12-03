from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('hm',views.home),
    path('cat',views.catdet,name='details'),
    path('cat/<str:name>',views.details,name='det'),
    path('item',views.item_list,name='item_list'),
    path('item/<str:name>',views.edit_item,name='update'),
    path('new',views.item_form,name="new"),
    path('del/<str:name>',views.delete_item,name='delete'),
    path('news', views.news, name='news'),
    path('newsadd',views.news_form,name='newnews'),
    path('dele/<str:Title>', views.delete_news, name='dele'),
    path('edit/<str:Title>',views.edit_news,name='edt'),
    path('about',views.about),
    path('catego/<str:cat_name>',views.showcat,name='catego'),
    

]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)