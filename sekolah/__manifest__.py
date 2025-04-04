{
    'name': "Sekolah",
    'version': '1.0',
    'depends': ['base'],
    'author': "Muhammad Geral Herpavy",
    'category': 'App',
    'description': """
        Ini adalah aplikasi sistem CRUD sederhana untuk manajemen data sekolah yaitu data siswa.
    """,
    'application': True,
    'data': [
        # Security
        'security/ir.model.access.csv',

        # Views
        'views/sekolah_property.xml',
        'views/sekolah_kota.xml',
        'views/report/grafik_kelahiran.xml',
        'views/report/grafik_kota.xml',
        'views/menu.xml',
    ]
}