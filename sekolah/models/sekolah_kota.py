from odoo import models, fields

class SekolahKota(models.Model):
    _name = "sekolah.kota"
    _description = "Data Kota"
    _order = "name"
    _sql_constraints = [
        ("check_name", "UNIQUE(name)", "Kota sudah ada!")
    ]

    name = fields.Char("Kota", required=True)

    city_ids = fields.One2many("sekolah.property", "city_id", string="Record")