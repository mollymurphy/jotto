from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'jotto.views.home', name='home'),
    url(r'^register/','jotto.views.register',name='register'),
    url(r'^user_profile/','jotto.views.upload_file',name='upload_file'),
    url(r'^login/','jotto.views.login_user',name='login_user'),
    url(r'^logout/','jotto.views.logout_user',name='logout'),
    url(r'^getword/','jotto.views.get_word',name='getword'),
    url(r'^rules/','jotto.views.rules',name='rules'),
    url(r'^play/','jotto.views.start_play',name='play'),
    url(r'^storeMatch/$','jotto.views.storeMatch',name="storeMatch"),
    url(r'^leaderboard/','jotto.views.leaderboard',name="leaderboard"),

    # url(r'^upload_file/','jotto.views.upload_file',name='upload_file'),
]