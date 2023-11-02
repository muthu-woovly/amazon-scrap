import gspread
from oauth2client.service_account import ServiceAccountCredentials


# Authenticate with Google Sheets
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    "enroll-influencer-fcc70126bf60.json"
)
client = gspread.authorize(credentials)
# Open the Google Sheet
test_write_url = "https://docs.google.com/spreadsheets/d/1gxPk0wtlLTHmB0B7xwI53DrHCdvkK67Ml7jCxqetR8Y/edit#gid=0"

sheet = client.open_by_url(test_write_url)

# try:
#     sheet = client.open('clearWishlist')
# except gspread.SpreadsheetNotFound as e:
#     print(f"Spreadsheet not found: {e}")


worksheet = sheet.get_worksheet(0)  # Assuming you want to use the first sheet
data = [
    # ['name', 'age', 'city'],
    ["John Doe", 2023, "oslo"],
    # Add more rows as needed
]

actual_data = {
    "url": "https://www.amazon.in/mCaffeine-Caffeinating-Breathable-Lightweight-Ultra-Comfortable/dp/B09BD5CY2G/",
    "title": "mcaffeine Caffeinating Sleeping Eye Mask, Breathable, Lightweight & Ultra-Comfortable, Gender Neutral & Travel Friendly, Made Of Pure Mulberry Silk",
    "actualPrice": "₹399",
    "discountedPrice": "349",
    "ratings": "3.7",
    "soldBy": "Visit the mcaffeine Store",
    "ratings_count": "196 ratings",
}
worksheet.rows_auto_resize(1, worksheet.row_count)

data = [list(actual_data.keys()), list(actual_data.values())]
print(worksheet.row_count)
if worksheet.row_count >= 2:
    data = [list(actual_data.values())]
# worksheet.clear()
# Write data
worksheet.append_rows(data)
# Define the object (row) you want to insert
# new_row = {'name':'John Doe', 'age':30,'city':'New York'}
# # worksheet.insert_row(new_row,1)
# # Write headers if needed (only once)
# if worksheet.row_values(1) == []:
#     headers = list(new_row.keys())
#     worksheet.insert_row(headers, 1)

# # Write data
# values = list(new_row.values())
# worksheet.insert_row(values, worksheet.row_count + 1)
