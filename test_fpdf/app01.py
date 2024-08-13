import time

from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_font("NotoSansSC", fname="../assets/NotoSansSC-VariableFont_wght.ttf")
pdf.set_font("NotoSansSC", "", 15)

pdf.add_page()

pdf.cell(text='dddd')
pdf.write(text='dddd\n')
pdf.write(text='dddd\n')
pdf.write(text='dddd\n')
# pdf.write(text='\n')
pdf.cell(text='dddd')


print(pdf.get_y())

pdf.output(name=f'test{time.time()}.pdf')