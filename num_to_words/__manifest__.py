{
    'name': 'Convert number to words',
    'version': "16.0.1.0.0",
    'author': "Fogits Solutions",
    'summary': """
    This module allows you to convert number to words """,
    'website': "https://www.fogits.com/",
    'description': """
        Convert invoice amount to text 
    """,
    'category': 'Accounting',
    'license': "AGPL-3",
    'depends': ['base_setup', 'account'],
    'data': [
        'views/account_invoice_view.xml',
    ]
}
