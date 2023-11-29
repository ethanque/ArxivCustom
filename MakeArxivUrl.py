# Generates a text file containing the URL for an Arxiv advanced search. Maintain your own list of authors and keywords in the provided format.

import urllib.parse

# Authors and Abstracts definitions
authors_terms = [
    'LastName, FirstName',
    'Ccc, Aaa B',
    'AnotherLastName, AnotherFirstName M I'
]
authors_field_type = 'author'

abstracts_terms = [
    '"Exact term in quotes"',
    '"Burgeoning subfield"',
    '"Exciting topic"'
]
abstracts_field_type = 'abstract'

# Initialize TxtStr
txt_str = "https://arxiv.org/search/advanced?advanced=&"
field_num = -1

# Combine Authors and Abstracts into a list
field_cells = [{'Terms': authors_terms, 'FieldType': authors_field_type},
               {'Terms': abstracts_terms, 'FieldType': abstracts_field_type}]

# Loop through the field cells
for field_cell in field_cells:
    for m_Trm in range(len(field_cell['Terms'])):
        # Field number string
        field_num += 1
        FNS = str(field_num)
        FieldStr = field_cell['Terms'][m_Trm]
        FieldStr = FieldStr.replace(",", "%2C+")
        FieldStr = FieldStr.replace(" ", "+")
        FieldStr = FieldStr.replace('"', "%22")
        txt_str += (
            f'terms-{FNS}-operator=OR&terms-{FNS}-term={FieldStr}&'
            f'terms-{FNS}-field={field_cell["FieldType"]}&'
        )

txt_str += 'classification-physics_archives=all&classification-include_cross_list=include&date-filter_by=all_dates&date-year=&date-from_date=&date-to_date=&date-date_type=submitted_date&abstracts=show&size=200&order=-announced_date_first'

# Write the TxtStr to a text file
with open('ArxivSearchUrl.txt', 'w') as file:
    file.write(txt_str)
