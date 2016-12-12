# Book Catalogue

> My personal book catalogue

## Install

```
pip install -r requirements
```

## Usage

1. Search by the book on http://www.isbnsearch.org
2. Save the book's page in the *raw* directory.
3. Optional: You can save the cover image in the *images* directory or run another script at the end.
4. Generate a CSV file.
5. Download cover images if you skip the step 3.
6. Generate an HTML file contains all books.

```
python generate_csv.py raw
python download_covers.py raw images
python generate_html.py books.csv
```
