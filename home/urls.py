from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
# index는 대문, blog는 게시판
from home.views import index, blog, posting
from . import views

app_name='home'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name = 'index'),
    path('blog/' ,views.blog, name='blog'),
    # URL:80/blog/숫자로 접속하면 게시글-세부페이지(posting)
    path('blog/<int:pk>/',views.posting, name="posting"),
    path('blog/new_post/', views.new_post),
        path('blog/<int:pk>/remove/', views.remove_post),

]

# 이미지 URL 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)