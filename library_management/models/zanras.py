from odoo import models, fields

class Zanras(models.Model):
    _name = 'biblioteka.zanras'
    _description = 'Knygos Žanras'

    pavadinimas = fields.Char(string='Žanras', required=True)