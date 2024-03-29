{
    'name': 'Univision Theme',
    'description': 'Contains the theme of UniVision.',
    'version': '16.0.1.0.0',
    'author': "Uni Vision",
    'website': "http://uni-vision.fr/",
    'license': "LGPL-3",
    'category': 'Website/Theme',
    'assets': {
        'web._assets_primary_variables': [
            ('prepend', 'website_univision/static/src/scss/primary_variables.scss'),
            ('prepend', 'website_univision/static/src/scss/secondary_variables.scss')
        ],
        'web._assets_frontend': [
            'website_univision/static/src/scss/bootstrap_overridden.scss',
        ]
    },

    'depends': ['website'],

    'data': [
    ],
}
