# Have You Tried Turning It Off? — one funny line a hopeless tech support
# agent gives a desperate customer. Writes the entry text to
# /output/entry.txt with no trailing newline, so the file holds exactly
# the line itself.

TEXT = "I rebooted the router, the laptop, and the printer — then I rebooted my career by applying for a job at the company that makes the router, because at least it listens."

if __name__ == "__main__":
    # Gate: the sealed scorer requires UTF-8 text of 1 to 199 characters.
    assert 1 <= len(TEXT) <= 199, "entry must be 1-199 characters"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
