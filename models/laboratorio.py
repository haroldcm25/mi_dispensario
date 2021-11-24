# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Laboratorio(models.Model):
    _name = 'laboratorio'
    _description = 'Son los nombres de los laboratorios de medicamentos'

    name = fields.Char("Nombre")
