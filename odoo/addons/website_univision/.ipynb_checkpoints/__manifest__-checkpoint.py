{
    'name': 'Univision theme',
    'description': 'Contains the theme of UniVision.',
    'version': '1.0',
    'author': "Uni Vision",
    'website': "http://uni-vision.fr/",
    'license':"LGPL-3",
    'category': 'Theme/Creative',
    'assets' : {
        'website._assets_primary_variables': [
            'website_univision/static/scss/primary_variables.scss'
            'website_univision/static/scss/secondary_variables.scss'
        ],
        'website._assets_frontend_helpers': [
            'website_univision/static/scss/bootstrap_overridden.scss'
        ]
    },

    'depends': ['website'],
    
    'data': [
    ],
}