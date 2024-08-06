import webbrowser

search = input('Write a term here:').replace(' ', '+')

webbrowser.open(f"https://www.google.com/search?q={search}")
