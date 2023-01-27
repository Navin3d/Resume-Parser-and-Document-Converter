import os

from rest_framework.response import Response
from rest_framework.decorators import api_view
from docx2pdf import convert
from doc2pdf import convert as convert_doc
from django.http import FileResponse


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DOCX_DIR = f"{BASE_DIR}/static/input/docx/"
DOC_DIR = f"{BASE_DIR}/static/input/doc/"
OUT_DIR = f"{BASE_DIR}/static/output/"


# @api_view(["GET"])
# def parse_resume(request):
#     data = resumeparse.read_file("https://navindurai.netlify.app/github/Navin%20Durai's%20resume.pdf")
#     return Response(status=200, data=data)


def write_data_into_file(directory, data):
    file_opened = open(directory, 'wb+')
    for chunk in data.chunks():
        file_opened.write(chunk)


def conv_docx(data):
    directory = DOCX_DIR + data.name
    output_file = data.name.split(".docx")
    converted = f"{OUT_DIR}{output_file[0]}-conv"
    write_data_into_file(directory, data)
    convert(directory, converted)


def conv_doc(data):
    directory = DOC_DIR + data.name
    output_file = data.name.split(".doc")
    converted = f"{OUT_DIR}{output_file[0]}-conv"
    write_data_into_file(directory, data)
    convert_doc(directory, converted)


@api_view(["POST"])
def convert_docx_to_pdf(request):
    data = request.FILES["file"]
    conv_docx(data)
    return Response(status=200, data="convert_docx_to_pdf Done!")


@api_view(["POST"])
def convert_doc_to_pdf(request):
    data = request.FILES["file"]
    conv_doc(data)
    return Response(status=200, data="convert_doc_to_pdf Done!")


def get_file(directory):
    file_data = open(directory, "rb")
    return file_data


@api_view(["GET"])
def get_a_file(request, file_name):
    data = get_file(f"{ OUT_DIR }{ file_name }")
    return FileResponse(data, as_attachment=True, filename=file_name)
