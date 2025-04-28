
import re

def extract_emails_from_html(html: str) -> list:
    """
    Extracts email addresses from a given HTML string.
    """
    pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    return re.findall(pattern, html)

# --- Demonstration with sample HTML ---
sample_html = """
<p>Contact our team:</p>
<ul>
  <li>info@example.com</li>
  <li>support@domain.org</li>
  <li>team@website.co.uk</li>
</ul>
"""

emails = extract_emails_from_html(sample_html)
print("Extracted emails from sample HTML:", emails)

# --- Code snippet for real website extraction ---
# Uncomment and use the following in your own environment:
#
# import requests
# def extract_emails_from_url(url: str) -> list:
#     response = requests.get(url)
#     return extract_emails_from_html(response.text)
#
# # Example usage:
# real_emails = extract_emails_from_url("https://www.your-website.com")
# print("Extracted emails from website:", real_emails)
