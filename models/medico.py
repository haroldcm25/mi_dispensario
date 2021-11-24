# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Medico(models.Model):
     _name = 'medico'
     _description = 'Son los medicos que recetan medicamentos a los pacientes'

     cedula = fields.Char("Cédula")
     nombres = fields.Char("Nombres")
     apellidos = fields.Char("Apellidos")

     #cliente
     cliente_id = fields.Many2one('cliente', string="Cliente Relacionado")
     nit_cliente = fields.Char(string="Cliente", related="cliente_id.nit_cliente") #required=False
