with open ("read file with syntax.txt", "r") as f:
    data=f.read()
print(data)

with open ("read file with syntax.txt", "a") as f:
    s=f.write("\nthis is append line")
print(s)

# No need to close file with syntax