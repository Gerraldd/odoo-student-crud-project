from odoo import models, fields, api
from datetime import datetime

class SekolahProperty(models.Model):
    _name = "sekolah.property"
    _description = "Sekolah Property"
    _order="name asc"

    name = fields.Char(string="Nama Siswa", required=True)
    city_id = fields.Many2one("sekolah.kota", string="Kota Asal")
    birth_day = fields.Date(string="Tanggal Lahir")
    year_of_birth = fields.Integer(string="Tahun Kelahiran", compute="_compute_tahun_kelahiran", store=True)
    nis = fields.Char(string="NIS")
    age = fields.Char(string="Umur")
    school = fields.Char(string="Asal Sekolah")
    gender = fields.Selection(
        selection=[ 
            ("laki-laki", "Laki-Laki"),
            ("perempuan", "Perempuan"),
        ],
        string="Jenis Kelamin"
        )
    
    @api.depends('birth_day')
    def _compute_tahun_kelahiran(self):
        for record in self:
            if record.birth_day:
                record.year_of_birth = record.birth_day.year
            else:
                record.year_of_birth = 0