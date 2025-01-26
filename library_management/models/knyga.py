from odoo import models, fields

class Knyga(models.Model):
    _name = 'biblioteka.knyga'
    _description = 'Bibliotekos knyga'

    pavadinimas = fields.Char(string='Pavadinimas', required=True)
    aprasymas = fields.Text(string='Aprašymas')
    puslapiu_skaicius = fields.Integer(string='Puslapių skaičius')
    zanro_ids = fields.Many2many('biblioteka.zanras', string='Žanrai')