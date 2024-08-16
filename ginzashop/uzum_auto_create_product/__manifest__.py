{
    'name': 'Uzum Auto Create Product',
    "summary": "Auto create product from uzum",
    "author": "Ruzimurodov Nodirjon",
    'version': '0.1',
    'depends': ['base', 'web', "website_sale", "stock"],
    'data': [
        "views/uzum_button.xml",
    ],
    'assets': {
        'web.assets_backend': [
        ],
    },
    'installable': True,
    'application': True,
}
