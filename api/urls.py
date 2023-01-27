from django.urls import path
from .views import *


urlpatterns = [
    # path("parser/", parse_resume),
    path("convert/docx/", convert_docx_to_pdf),
    path("convert/doc/", convert_doc_to_pdf),
    path("file/<str:file_name>/", get_a_file),
]
