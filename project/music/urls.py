from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


app_name = "music"

urlpatterns = [
    path('', views.singer_list_create),
    path('<int:singer_id>', views.singer_detail_update_delete),
    path('<int:singer_id>/song', views.song_list_create),
    path('<int:singer_id>/song/<int:song_id>', views.song_detail),
    path('tags/<str:tags_name>', views.find_tag)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)