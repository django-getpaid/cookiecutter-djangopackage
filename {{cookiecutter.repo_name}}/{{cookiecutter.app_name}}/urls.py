### Use this only if standard flow provided by django-getpaid does not cover your use-case.


# from django.conf.urls import url
#
# from .views import {{ cookiecutter.broker_name|replace('_', ' ')|title()|replace(' ', '') }}ReturnView
#
# urlpatterns = [
#     url(r"^return/(?P<pk>[0-9a-f-]+)/$", {{ cookiecutter.broker_name|replace('_', ' ')|title()|replace(' ', '') }}ReturnView.as_view(), name="return-view")
# ]
