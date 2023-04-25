#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 19:22:27 2023

@author: andy
"""
import pandas as pd
import camelot

pdf_file='/home/andy/Downloads/test.pdf'
#pdf_file='https://gstcouncil.gov.in/sites/default/files/gst-revenue-collection-march2020.pdf'
#tables = camelot.read_pdf('')
#tables=camelot.read_pdf(pdf_file, pages='all',line_scale=40, copy_text=['v'])
#tables=camelot.read_pdf(pdf_file,flavor="lattice",pages='all',process_background=True)
#tables=camelot.read_pdf(pdf_file,flavor="lattice",pages='all',process_background=True)
tables=camelot.read_pdf(pdf_file,flavor="lattice",pages='all')
i=0
for table in tables:
    table_no_string=str(i)
    table_string=f"{table_no_string}.csv"
    table.df.to_csv(table_string)
    i+=1
    
# merged_tables = []
# for table in tables:
#     if len(table._bbox) == 2:  # Check if the table spans across multiple pages
#         merged_tables[-1]._data += table._data  # Merge the table with the previous table
#     else:
#         merged_tables.append(table)

# # Convert the tables to Pandas DataFrames
# tables_df = [table.df for table in merged_tables]

# # Concatenate the tables
# complete_table = pd.concat(tables_df, ignore_index=True)