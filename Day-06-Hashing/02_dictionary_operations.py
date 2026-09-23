marks = {
    "DSA": 120,
    "fla": 34
}

# Insert
marks["maths"] = 90
marks["english"] = 85

print(marks)

# Delete
del marks["fla"]

print(marks)

# Search / Access
print(marks["DSA"])

# Update
marks["DSA"] = 98

print(marks["DSA"])

# Check if key exists
if "english" in marks:
    print("It exists")
