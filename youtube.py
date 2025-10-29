import re
import sys

def main():
    html = input("HTML: ")
    print(parse(html))

def parse(s):
    match = re.search(r'src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"', s)
    if match:
        video_id = match.group(1) 
        return f"https://youtu.be/{video_id}"
    return None

main()
