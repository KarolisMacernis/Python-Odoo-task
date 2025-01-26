from odoo import models, fields, api

class KnygosIsdavimas(models.Model):
    _name = 'biblioteka.knygos_isdavimas'
    _description = 'Knygos išdavimas'

    kontaktas_id = fields.Many2one('res.partner', string='Kontaktas', required=True)
    pradzios_data = fields.Date(string='Pradžios data', required=True)
    pabaigos_data = fields.Date(string='Pabaigos data', required=True)
    knygu_ids = fields.Many2many('biblioteka.knyga', string='Knygos')
    busena = fields.Selection([
        ('uzrezervuota', 'Užrezervuota'),
        ('isduota', 'Išduota'),
        ('grazinta', 'Grąžinta'),
        ('atsaukta', 'Atšaukta')
    ], string='Būsena', default='uzrezervuota')

    @api.model
    def tikrinti_veluojancias_knygas(self):
        pass