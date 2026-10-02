import base64

print("=== File Protection Utility ===")

# Get content from user
content = input("Enter the content to protect: ")

# Protect (encode) the content
encoded = base64.b64encode(content.encode()).decode()

print("\nProtected Content:")
print(encoded)

# Restore (decode) the content
decoded = base64.b64decode(encoded).decode()

print("\nRestored Content:")
print(decoded)
