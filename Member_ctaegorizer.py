def categorize_members(members):
    categories = []
    for age, handicap in members:
        if age >= 55 and handicap > 7:
            categories.append("Senior")
        else:
            categories.append("Open")
    return categories

# Test case
input_members = [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9],[66,5]]
output_categories = categorize_members(input_members)
print(output_categories)
