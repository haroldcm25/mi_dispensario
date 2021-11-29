# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Proveedor(models.Model):
    _name = 'proveedor'
    _description = 'proveedor de productos de dispensario'

    name = fields.Char("Nombre")

    # def funcion_mi_boton(self):
    #     pass