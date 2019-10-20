# Manga-Scraper
Scrape manga chapters from Mangafox and organise it into folders.

- Run the script, chapter count is optional.
- Enter the fanfox.net chapter or page url to start downloading.
- All the pages of the chapter are downloaded and saved to a folder in the same directory.
- Keeps downloading and saving to folders till the chapter limit reached or the series ends (Has a default chapter limit of 1500).
- Uses Selenium and chrome driver.
- Uses Python3.

## Examples:

#### 1.
```
 python manga-download.py
```
Output:
```
Enter the url of the chapter or the page:
https://fanfox.net/manga/gintama/v77/c704
```

This will start download from chapter 1 and run till the end, organising chapters into folders.

#### 2.
```
 python manga-download.py
```
Output:
```
Enter the url of the chapter or the page:
https://fanfox.net/manga/gintama/v77/c704/4.html
```

This will start download from page 4.

#### 3.
```
 python manga-download.py 4
```
Output:
```
Enter the url of the chapter or the page:
https://fanfox.net/manga/gintama/v74/c700
```

This will download 4 chapters starting from the url entered.
