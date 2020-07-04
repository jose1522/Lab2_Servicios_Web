from flask import Blueprint, url_for, session, make_response, request, redirect, send_file, render_template
from database import db, models
from core.util import networking as net
from database.queries import *
from io import BytesIO
from form.forms import *
from werkzeug.utils import secure_filename
from xml.etree.ElementTree import parse
import json

public = Blueprint('public', '__name__')


@public.route("/test")
def test():
    canton = models.Canton.query.get(1)
    name = canton.Nombre
    res = make_response("{0}, {1}".format(name,net.getIP()))
    return res

@public.route("/lab3")
def lab3():
    form = deserializationForm()
    res = make_response(render_template('public/lab3.html', form=form))
    return res

@public.route("/")
def index():
    res = make_response(render_template('public/index.html'))
    return res

@public.route("/lab2", methods=['GET', 'POST'])
def lab2():
    jsonResult: str
    xmlResult: str
    form = selectionForm()
    response = make_response(render_template('/public/lab2.html', form=form))

    if request.method == 'POST':
        incomingForm = request.form
        report = int(incomingForm['report'])
        option = int(incomingForm['option'])
        jsonResult = xmlResult = ""

        if report == 1:
            jsonResult, xmlResult = allProducts()
        elif report == 2:
            jsonResult, xmlResult = suppliersByProvince('Alajuela')
        elif report == 3:
            jsonResult, xmlResult = suppliersByProvince()
        elif report == 4:
            jsonResult, xmlResult = cantonsByProvince(('Heredia', 'Puntarenas'))
        elif report == 5:
            jsonResult, xmlResult = ordersByProvince()
        else:
            jsonResult, xmlResult = productByLine(('Carnes',))

        if option == 1:
            result = xmlResult
            attachment_filename = "result.xml"
        else:
            result = str(jsonResult)
            attachment_filename = "result.json"

        buffer = BytesIO()
        buffer.write(result.encode('utf-8'))
        buffer.seek(0)
        response = make_response(send_file(buffer, as_attachment=True, attachment_filename=attachment_filename, mimetype='application/xml'))

    return response