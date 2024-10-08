from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)


def footer_creator(pdf, text):
    pdf.set_y(-15)
    pdf.set_font(family='Times', style='B', size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, txt=text, align='R')


df = pd.read_csv(r'C:\Users\Elara\Documents\Projects\python_study\60-days-learning-python\day-24\topics.csv')

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1)
    pdf.line(10, 21, 200, 21)

    footer_creator(pdf, row['Topic'])

    y_position = 21
    for j in range(0, 27):
        pdf.line(10, y_position, 200, y_position)
        y_position += 10

    for i in range(row['Pages'] - 1):
        pdf.add_page()
        y_position = 21
        for j in range(0, 27):
            pdf.line(10, y_position, 200, y_position)
            y_position += 10
        footer_creator(pdf, row['Topic'])

# pdf.add_page()
#
# pdf.set_font(family='Times', style='B', size=12)
# pdf.cell(w=0, h=12, txt='Another one!', align='L', ln=1, border=1)

pdf.output('output.pdf')
