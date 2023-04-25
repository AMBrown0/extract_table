import pdfkit

# set the options for wkhtmltopdf
options = {
    'page-size': 'A4',
    'margin-top': '0mm',
    'margin-right': '0mm',
    'margin-bottom': '0mm',
    'margin-left': '0mm',
}

# specify the URL of the web page you want to print
url = 'https://www.instituteforapprenticeships.org/apprenticeship-standards/digital-support-technician-v1-1?view=epa&option=All'

# specify the name and path of the output PDF file
output_path = '/home/andy/Downloads/test.pdf'

# use pdfkit to convert the web page to PDF
pdfkit.from_url(url, output_path, options=options)

