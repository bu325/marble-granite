from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors

from core.rtl import get_rtl_text
from core.utils import format_currency

# Register Amiri font (assuming it\'s in assets/fonts/)
pdfmetrics.registerFont(TTFont("Amiri-Regular", "assets/fonts/Amiri-Regular.ttf"))
pdfmetrics.registerFont(TTFont("Amiri-Bold", "assets/fonts/Amiri-Bold.ttf"))

def generate_invoice_pdf(invoice_data, file_path):
    c = canvas.Canvas(file_path, pagesize=A4)
    width, height = A4

    # Set font for the entire document
    pdfmetrics.setDefaultFont("Amiri-Regular")

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name=\'RTL
        name=\'RTL
        fontName=\'Amiri-Regular
        alignment=4, # TA_RIGHT
        leading=14
    ))
    styles.add(ParagraphStyle(name=\'RTL_Bold
        name=\'RTL_Bold
        fontName=\'Amiri-Bold
        alignment=4, # TA_RIGHT
        leading=14
    ))

    # Company Info (Placeholder)
    c.setFont("Amiri-Bold", 18)
    c.drawString(width - 50 * mm, height - 30 * mm, get_rtl_text("شركة الرخام والجرانيت"))

    # Invoice Title
    c.setFont("Amiri-Bold", 16)
    c.drawString(width - 50 * mm, height - 45 * mm, get_rtl_text("فاتورة بيع"))

    # Client Info
    c.setFont("Amiri-Regular", 12)
    c.drawString(width - 50 * mm, height - 65 * mm, get_rtl_text(f"العميل: {invoice_data["client_name"]}"))
    c.drawString(width - 50 * mm, height - 75 * mm, get_rtl_text(f"التاريخ: {invoice_data["date"]}"))
    c.drawString(width - 50 * mm, height - 85 * mm, get_rtl_text(f"رقم الفاتورة: {invoice_data["invoice_number"]}"))

    # Items Table
    data = [[get_rtl_text("الإجمالي"), get_rtl_text("السعر/م²"), get_rtl_text("المساحة م²"), get_rtl_text("الكمية"), get_rtl_text("المادة")]]
    for item in invoice_data["items"]:
        data.append([
            format_currency(item["total"]),
            format_currency(item["sell_price_m2"]),
            f"{item["area_m2"]:.2f}",
            f"{item["pieces"]}",
            get_rtl_text(item["material_name"])
        ])

    table = Table(data, colWidths=[60*mm, 30*mm, 30*mm, 20*mm, 50*mm])
    table.setStyle(TableStyle([
        (\'BACKGROUND\', (0, 0), (-1, 0), colors.grey),
        (\'TEXTCOLOR\', (0, 0), (-1, 0), colors.whitesmoke),
        (\'ALIGN\', (0, 0), (-1, -1), \'RIGHT\'),
        (\'FONTNAME\', (0, 0), (-1, 0), \'Amiri-Bold\'),
        (\'BOTTOMPADDING\', (0, 0), (-1, 0), 12),
        (\'BACKGROUND\', (0, 1), (-1, -1), colors.beige),
        (\'GRID\', (0,0), (-1,-1), 1, colors.black)
    ]))

    table.wrapOn(c, width, height)
    table.drawOn(c, 30 * mm, height - 120 * mm - len(data) * 10 * mm)

    # Totals
    y_pos = height - 120 * mm - len(data) * 10 * mm - 20 * mm
    c.setFont("Amiri-Regular", 12)
    c.drawString(width - 50 * mm, y_pos, get_rtl_text(f"الإجمالي قبل الخصم: {format_currency(invoice_data["subtotal"])}"))
    y_pos -= 15 * mm
    c.drawString(width - 50 * mm, y_pos, get_rtl_text(f"الخصم: {format_currency(invoice_data["discount_amount"])}"))
    y_pos -= 15 * mm
    c.drawString(width - 50 * mm, y_pos, get_rtl_text(f"الضريبة: {format_currency(invoice_data["tax_amount"])}"))
    y_pos -= 15 * mm
    c.setFont("Amiri-Bold", 14)
    c.drawString(width - 50 * mm, y_pos, get_rtl_text(f"الإجمالي النهائي: {format_currency(invoice_data["total"])}"))

    c.save()


