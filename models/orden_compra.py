# -*- coding: utf-8 -*-

from odoo import models, fields, api

class OrdenCompra(models.Model):
     _name = 'orden_compra'
     _description = 'son las solicitudes u ordenes que se ingresan al inventario(falta recepcionar, se ingresará directo para la prueba)'

     proveedor = fields.Char("Proveedor")
     descripcion = fields.Char("Descripción")
     formas_pago = fields.Char("Formas de pago")
     total = fields.Float("Total")
