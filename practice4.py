import re

text = """
Contact us at support@example.com or sales@company.org
Call +91-9876543210 or 080-22334455
Visit https://www.python.org or http://example.net
"""

print("========================")
match = re.search(r'\b\w+@[\w.-]+\.\w+\b', text)
if match:
    print("Found email:", match.group())  
    print("Start index:", match.start())
    print("End index:", match.end())
    print("Span:", match.span())

print("\n==========================")
m = re.match(r'Contact', text)
print("Match at start:", m.group() if m else "No match")

print("\n==========================")
emails = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)
print("All emails:", emails)

print("\n============================")
for i, m in enumerate(re.finditer(r'\b\+?\d[\d-]+\b', text), start=1):
    print(f"Phone {i}: {m.group()} at position {m.span()}")

print("\n=============================")
parts = re.split(r'\s+', "This is a test string")
print("Split words:", parts)

print("\n================================")
clean_text = re.sub(r'\+91-', '', text)  
print("After removing +91-:")
print(clean_text)

print("\n===================================")
pattern = r'(\w+)@([\w.]+)' 
for m in re.finditer(pattern, text):
    print("Full email:", m.group(0))
    print("Username:", m.group(1))
    print("Domain:", m.group(2))
    print("All groups:", m.groups())
    print("---")
