# coding: utf-8
from sqlalchemy import Column, DECIMAL, DateTime, ForeignKey, Index, Integer, LargeBinary, NCHAR, String, Unicode, Float
from sqlalchemy.dialects.mssql import BIT
from sqlalchemy.orm import relationship
from . import db

Base = db
Model = Base.Model
metadata = Base.metadata

class Factura(Model):
    __tablename__ = 'Facturas'

    Num_Factura = Column(Integer, primary_key=True)
    Fecha_Factura = Column(DateTime, nullable=False)
    Total = Column(DECIMAL(15, 2))


class Linea(Model):
    __tablename__ = 'Lineas'

    Cod_Linea = Column(Integer, primary_key=True)
    Descripcion_Linea = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)


class Privilegio(Model):
    __tablename__ = 'Privilegios'

    Cod_Privilegio = Column(Integer, primary_key=True)
    Privilegio = Column(String(100, 'Modern_Spanish_CI_AS'), nullable=False)


class Proveedore(Model):
    __tablename__ = 'Proveedores'

    Cod_Proveedor = Column(Integer, primary_key=True)
    Nombre_Proveedor = Column(String(500, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    Telefono = Column(String(15, 'SQL_Latin1_General_CP1_CI_AS'))
    Direccion = Column(String(500, 'SQL_Latin1_General_CP1_CI_AS'))


class Provincia(Model):
    __tablename__ = 'Provincia'

    Cod_Provincia = Column(Integer, primary_key=True)
    Nombre = Column(String(100, 'Modern_Spanish_CI_AS'))


class TipoConsecutivo(Model):
    __tablename__ = 'Tipo_Consecutivo'

    Cod_Tipo_Consecutivo = Column(Integer, primary_key=True)
    Tipo_Consecutivo = Column(String(100, 'Modern_Spanish_CI_AS'))


class Usuario(Model):
    __tablename__ = 'Usuarios'

    Cod_Usuario = Column(Integer, primary_key=True)
    Nombre = Column(String(100, 'Modern_Spanish_CI_AS'))
    Pri_Ape = Column(String(100, 'Modern_Spanish_CI_AS'))
    Seg_Ape = Column(String(100, 'Modern_Spanish_CI_AS'))
    Login = Column(String(100, 'Modern_Spanish_CI_AS'), nullable=False)
    Pass = Column(String(100, 'Modern_Spanish_CI_AS'), nullable=False)
    Confirmar_Pass = Column(String(100, 'Modern_Spanish_CI_AS'), nullable=False)
    Telefono1 = Column(String(9, 'Modern_Spanish_CI_AS'))
    Telefono2 = Column(String(9, 'Modern_Spanish_CI_AS'))
    Admin_Seg = Column(BIT)
    Admin_Ad = Column(BIT)


class Sysdiagram(Model):
    __tablename__ = 'sysdiagrams'
    __table_args__ = (
        Index('UK_principal_name', 'principal_id', 'name', unique=True),
    )

    name = Column(Unicode(128), nullable=False)
    principal_id = Column(Integer, nullable=False)
    diagram_id = Column(Integer, primary_key=True)
    version = Column(Integer)
    definition = Column(LargeBinary)


class Bitacora(Model):
    __tablename__ = 'Bitacora'

    Cod_Bitacora = Column(Integer, primary_key=True)
    Cod_Usuario = Column(ForeignKey('Usuarios.Cod_Usuario'), nullable=False)
    Fecha_Hora = Column(DateTime, nullable=False)
    Descripcion = Column(String(1000, 'Modern_Spanish_CI_AS'), nullable=False)

    Usuario = relationship('Usuario')


class Canton(Model):
    __tablename__ = 'Canton'

    Cod_Canton = Column(Integer, primary_key=True)
    Nombre = Column(String(100, 'Modern_Spanish_CI_AS'))
    Cod_Provincia = Column(ForeignKey('Provincia.Cod_Provincia'))

    Provincia = relationship('Provincia')


class Consecutivo(Model):
    __tablename__ = 'Consecutivos'

    Cod_Consecutivo = Column(Integer, primary_key=True)
    Tipo = Column(ForeignKey('Tipo_Consecutivo.Cod_Tipo_Consecutivo'))
    Descripcion = Column(String(100, 'Modern_Spanish_CI_AS'))
    Valor = Column(Integer, nullable=False)
    Posee_Prefijo = Column(BIT, nullable=False)
    Prefijo = Column(String(5, 'Modern_Spanish_CI_AS'), nullable=False)

    Tipo_Consecutivo = relationship('TipoConsecutivo')


class Errore(Model):
    __tablename__ = 'Errores'

    Cod_Error = Column(Integer, primary_key=True)
    Cod_Usuario = Column(ForeignKey('Usuarios.Cod_Usuario'))
    Fecha_Hora = Column(DateTime)
    Tabla = Column(String(50, 'Modern_Spanish_CI_AS'))
    Descripcion = Column(String(1000, 'Modern_Spanish_CI_AS'))

    Usuario = relationship('Usuario')


class Pedido(Model):
    __tablename__ = 'Pedidos'

    Num_Pedido = Column(Integer, primary_key=True)
    Fecha_Pedido = Column(DateTime, nullable=False)
    Monto_Pedido = Column(Float(asdecimal=False), nullable=False)
    Cod_Proveedor = Column(ForeignKey('Proveedores.Cod_Proveedor'))

    Proveedore = relationship('Proveedore')


class PrivilegiosUsuario(Model):
    __tablename__ = 'Privilegios_Usuarios'

    Cod_Privilegio = Column(ForeignKey('Privilegios.Cod_Privilegio'), primary_key=True, nullable=False)
    Cod_Usuario = Column(ForeignKey('Usuarios.Cod_Usuario'), primary_key=True, nullable=False)
    activo = Column(BIT)

    Privilegio = relationship('Privilegio')
    Usuario = relationship('Usuario')


class Producto(Model):
    __tablename__ = 'Productos'

    Cod_Producto = Column(Integer, primary_key=True)
    Nombre_Producto = Column(String(70, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    Cod_Linea = Column(ForeignKey('Lineas.Cod_Linea'))
    Cod_Proveedor = Column(ForeignKey('Proveedores.Cod_Proveedor'))
    Descontinuado = Column(BIT, nullable=False)

    Linea = relationship('Linea')
    Proveedore = relationship('Proveedore')


class DetalleFactura(Model):
    __tablename__ = 'Detalle_Factura'

    Cod_Detalle_Factura = Column(Integer, primary_key=True)
    Num_Factura = Column(ForeignKey('Facturas.Num_Factura'), nullable=False)
    Cod_Producto = Column(ForeignKey('Productos.Cod_Producto'), nullable=False)
    Cantidad = Column(Integer, nullable=False)
    Precio = Column(DECIMAL(18, 0), nullable=False)

    Producto = relationship('Producto')
    Factura = relationship('Factura')


class DetallePedido(Model):
    __tablename__ = 'Detalle_Pedido'

    Cod_Detalle_Pedido = Column(Integer, primary_key=True)
    Num_Pedido = Column(ForeignKey('Pedidos.Num_Pedido'))
    Cod_Producto = Column(ForeignKey('Productos.Cod_Producto'))
    Cantidad = Column(Integer, nullable=False)
    Precio = Column(DECIMAL(15, 2), nullable=False)

    Producto = relationship('Producto')
    Pedido = relationship('Pedido')


class Distrito(Model):
    __tablename__ = 'Distrito'

    Cod_Distrito = Column(Integer, primary_key=True)
    Nombre = Column(String(100, 'Modern_Spanish_CI_AS'))
    Codigo_Postal = Column(NCHAR(10))
    Cod_Canton = Column(ForeignKey('Canton.Cod_Canton'))

    Canton = relationship('Canton')
