from plyer import notification

def notify_low_stock(material_name, current_stock, threshold):
    title = "تنبيه انخفاض المخزون"
    message = f"المادة {material_name} وصلت إلى {current_stock} وهي أقل من الحد المسموح به {threshold}."
    notification.notify(title=title, message=message, app_name="MarbleGraniteApp")


