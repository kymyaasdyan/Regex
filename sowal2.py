import re
from datetime import datetime
#import jdatetime 
def convert_gregorian_to_jalali(date_str):
    date_formats = [
        "%d-%m-%Y",
        "%d-%m-%y",
        "%d/%m/%Y",
        "%d/%m/%y",
        "%d/%m/%Y"
    ]
    for date_format in date_formats:
        try:
            date_obj = datetime.strptime(date_str, date_format)
            jalali_date = jdatetime.date.fromgregorian(date=date_obj)
            return jalali_date.strftime('%Y/%m/%d')
        except ValueError:
            pass

    raise ValueError("Date format not recognized")

def find_and_convert_dates(text):
    date_pattern = re.compile(r'\b(\d{1,2}[-/]\d{1,2}[-/]\d{2,4})\b')
    matches = date_pattern.findall(text)
    
    converted_dates = {}
    for match in matches:
        try:
            converted_dates[match] = convert_gregorian_to_jalali(match)
        except ValueError:
            converted_dates[match] = "Invalid Date Format"
    
    return converted_dates
text = """
11-07-2024
9-7-2024
9/7/204
9/7/24
"""
converted_dates = find_and_convert_dates(text)
for original, converted in converted_dates.items():
    print(f"{original} -> {converted}")