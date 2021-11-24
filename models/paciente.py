# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Paciente(models.Model):
     _name = 'paciente'
     _description = 'Son los pacientes a los que se les dispensa medicamentos'

     cedula = fields.Char("Cédula")
     primer_nombre = fields.Char("Primer nombre")
     segundo_nombre = fields.Char("Segundo nombre")
     primer_apellido = fields.Char("Primer apellido")
     segundo_apellido = fields.Char("Segundo apellido")
     genero = fields.Char("Género")
     fecha_nacimiento = fields.Date("Fecha nacimiento")
     active = fields.Boolean("Estado", default=True)

     # cliente
     cliente_id = fields.Many2one('cliente', string="Cliente Relacionado")
     nit_cliente = fields.Char(string="Cliente", related="cliente_id.nit_cliente")

