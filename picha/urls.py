from django.conf.urls import include, url
from django.contrib import admin

from feedback.views import FeedbackView

urlpatterns = [
    url(r'^feedback/$', FeedbackView.as_view(), name="feedback"),
    url(r'^admin/', include(admin.site.urls)),
]
