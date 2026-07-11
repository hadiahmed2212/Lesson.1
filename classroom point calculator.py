year_1=34
year_2=16
year_3=37
year_4=29
year_5=42
total_points = year_1 + year_2 + year_3 + year_4 + year_5
average_points = total_points / 5
total_stars = 160
stars_per_box = 15

full_boxes = total_stars // stars_per_box
leftover_stars = total_stars % stars_per_box

print("Full boxes:", full_boxes)
print("Leftover stars:", leftover_stars)
