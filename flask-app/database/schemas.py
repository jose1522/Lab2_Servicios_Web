from . import ma


class ProductSchema(ma.Schema):
    class Meta:
        fields = ('Cod_Producto', 'Nombre_Producto', 'Cod_Linea', 'Cod_Proveedor', 'Descontinuado')


class SupplierSchema(ma.Schema):
    class Meta:
        fields = ('Cod_Proveedor', 'Nombre_Proveedor', 'Telefono', 'Direccion')


class CantonSchema(ma.Schema):
    class Meta:
        fields = ('Cod_Canton', 'Nombre', 'Cod_Provincia')


class OrderSchema(ma.Schema):
    class Meta:
        fields = ('Num_Pedido', 'Fecha_Pedido', 'Monto_Pedido', 'Cod_Proveedor')


