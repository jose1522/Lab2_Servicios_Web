from . import db
from .models import *
from sqlalchemy import text, or_, and_, any_
from .schemas import *
from json2xml import json2xml


def allProducts():
    productList = Producto.query.order_by(text("Nombre_Producto asc")).all()
    schema = ProductSchema(many=True)
    jsonResult = schema.jsonify(productList).json
    xmlResult = json2xml.Json2xml(jsonResult).to_xml()
    return jsonResult, xmlResult


def suppliersByProvince(province: str=None):

    if 'Alajuela' == province:
        supplierList = Proveedore.query.filter(Proveedore.Direccion.like('%Alajuela%')).order_by(text("Nombre_Proveedor asc")).all()
    else:
        supplierList = Proveedore.query.filter(or_(Proveedore.Direccion.like('%Cartago%'), Proveedore.Direccion.like('%Guanacaste%'))).order_by(text("Nombre_Proveedor asc")).all()

    schema = SupplierSchema(many=True)
    jsonResult = schema.jsonify(supplierList).json
    xmlResult = json2xml.Json2xml(jsonResult).to_xml()
    return jsonResult, xmlResult


def cantonsByProvince(province: tuple):

    cantonList = Canton.query.filter(Canton.Provincia.has(Provincia.Nombre.in_(province))).order_by(text("Cod_Provincia, Nombre asc")).all()
    schema = CantonSchema(many=True)
    jsonResult = schema.jsonify(cantonList).json
    xmlResult = json2xml.Json2xml(jsonResult).to_xml()
    return jsonResult, xmlResult


def ordersByProvince(province: tuple = None):

    orderList = Pedido.query.join(Proveedore).filter(Proveedore.Direccion.like('%Limón%')).all()
    schema = OrderSchema(many=True)
    jsonResult = schema.jsonify(orderList).json
    xmlResult = json2xml.Json2xml(jsonResult).to_xml()
    return jsonResult, xmlResult


def productByLine(line: tuple = None):

    productList = Producto.query.join(Linea).filter(Linea.Descripcion_Linea.in_(line)).order_by(text("Nombre_Producto asc")).all()
    schema = ProductSchema(many=True)
    jsonResult = schema.jsonify(productList).json
    xmlResult = json2xml.Json2xml(jsonResult).to_xml()
    return jsonResult, xmlResult