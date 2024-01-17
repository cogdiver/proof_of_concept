

def print_box(title, rows):
    """
    Prints a box with a title and multiple rows of content.

    The box is dynamically sized based on the length of the title and the content
    of the rows. It ensures that the box is wide enough to contain the longest
    string either in the title or any of the rows, with a padding of 4 characters
    for aesthetics.

    Parameters:
    - title (str): The title of the box. It is centered at the top of the box.
    - rows (list of str): A list of strings, each representing a row of content 
      within the box. These rows are left-aligned inside the box.

    The function first calculates the maximum width needed for the box, which is
    the length of the longest string (either the title or any row) plus 4 characters
    for padding. It then prints the top border of the box, followed by the title
    centered within the box, and then each row of content, left-justified. Finally,
    it prints the bottom border of the box.
    """
    width = max(len(title), *[len(r) for r in rows]) + 4

    print("\n+ " + "-"*width + " +")
    print(f"| {title.center(width)} |")
    print("+ " + "-"*width + " +")

    for r in rows:
        print(f"| {r.ljust(width)} |")

    print("+ " + "-"*width + " +")
