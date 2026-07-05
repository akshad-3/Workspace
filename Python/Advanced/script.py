import requests
from bs4 import BeautifulSoup


def print_secret_message(doc_url):
    """
    Fetches a published Google Doc containing a table of Unicode
    characters and their (x, y) grid positions, then prints the
    grid so the characters form a graphic of uppercase letters.
    done
    """
    response = requests.get(doc_url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table")
    if table is None:
        print("No table found in the document.")
        return

    rows = table.find_all("tr")

    # Figure out which column is x, which is the character, and which is y
    header_cells = [c.get_text(strip=True).lower() for c in rows[0].find_all(["td", "th"])]
    x_idx = next(i for i, h in enumerate(header_cells) if "x" in h)
    y_idx = next(i for i, h in enumerate(header_cells) if "y" in h)
    char_idx = next(i for i in range(len(header_cells)) if i != x_idx and i != y_idx)

    grid = {}
    max_x = 0
    max_y = 0

    for row in rows[1:]:
        cells = row.find_all("td")
        if len(cells) < 3:
            continue

        x = int(cells[x_idx].get_text(strip=True))
        y = int(cells[y_idx].get_text(strip=True))
        char = cells[char_idx].get_text(strip=True)

        grid[(x, y)] = char
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    # (0,0) is top-left; x grows right, y grows down
    for y in range(max_y + 1):
        line = "".join(grid.get((x, y), " ") for x in range(max_x + 1))
        print(line)


if __name__ == "__main__":
    print_secret_message(
        "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
    )