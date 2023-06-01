import pandas as pd
import vobject

# Read the Excel file
file = input("File Name? => ")
excel_file = './input/'+file
df = pd.read_excel(excel_file)

# Create a VCF file
vcf_file = './output/contacts.vcf'

# Iterate through each row in the DataFrame
with open(vcf_file, 'w', encoding='utf-8') as f:
    for _, row in df.iterrows():
        # Extract contact information from each row
        first_name = row['First Name']
        number = str(row['Nomber'])  # Convert to string

        # Add prefix to the first name
        modified_first_name = "000000" + first_name

        # Create a vCard object
        vcard = vobject.vCard()
        vcard.add('fn').value = modified_first_name
        vcard.add('tel').value = "+"+number

        # Write the vCard to the VCF file
        f.write(vcard.serialize())
        f.write('\n\n')  # Add newlines between vCards

print("Conversion completed. VCF file generated.")

