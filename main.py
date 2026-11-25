# Have You Tried Turning It Off? — one funny line a hopeless tech support
# agent gives a desperate customer. Writes the entry text to
# /output/entry.txt with no trailing newline, so the file holds exactly
# the line itself.

TEXT = "Please unplug the router, count to ten, and plug it back in. I'll do the same with my headset, my keyboard, and my career — let's see which one of us reconnects first."

if __name__ == "__main__":
    # Gate: the sealed scorer requires UTF-8 text of 1 to 199 characters.
    assert 1 <= len(TEXT) <= 199, "entry must be 1-199 characters"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
