
import urllib.request
from bs4 import BeautifulSoup


def decode_secret_message(doc_url):
    request = urllib.request.Request(
        doc_url,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    with urllib.request.urlopen(request) as response:
        html = response.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table")

    if table is None:
        print("Could not find a table in the document.")
        return

    characters = {}
    largest_x = 0
    largest_y = 0
    for row in table.find_all("tr")[1:]:
        cells = [
            cell.get_text(strip=True)
            for cell in row.find_all(["td", "th"])
        ]

        if len(cells) < 3:
            continue

        try:
            x = int(cells[0])
            character = cells[1] if cells[1] else " "
            y = int(cells[2])

            characters[(x, y)] = character

            largest_x = max(largest_x, x)
            largest_y = max(largest_y, y)

        except ValueError:
            continue

    for y in range(largest_y, -1, -1):
        line = ""

        for x in range(largest_x + 1):
            line += characters.get((x, y), " ")

        print(line)

decode_secret_message("https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub")

