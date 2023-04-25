#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 22:57:22 2023

@author: andy
"""

import PyPDF2

# Set the path to your input and output PDF files
input_pdf_path = '/home/andy/Downloads/test.pdf'
output_pdf_path = '/home/andy/Downloads/out.pdf'

# Open the input PDF file
with open(input_pdf_path, 'rb') as input_pdf_file:
    input_pdf = PyPDF2.PdfReader(input_pdf_file)
    
    # Create a new PDF file
    output_pdf = PyPDF2.PdfWriter()
    
    # Loop through each page of the input PDF file
    for page_num in range(len(input_pdf.pages)):
        # Extract the current page from the input PDF file
        current_page = input_pdf.pages[page_num]
        
        # Get the current page dimensions
        current_page_width = current_page.mediabox.width
        current_page_height = current_page.mediabox.height
        
        # Create a new page with double the height
        new_page = current_page
        new_page.mediabox.upper_right = (
            current_page_width,
            2 * current_page_height
        )
        
        # Add the new page to the new PDF file
        output_pdf.add_page(new_page)
    
    # Write the new PDF file to disk
    with open(output_pdf_path, 'wb') as output_pdf_file:
        output_pdf.write(output_pdf_file)