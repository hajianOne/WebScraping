# a simple WebScraping Python code

WebScraping is a Python code to illustrate data acquisition using
`selenium` library. For this purpose, one needs often to emulate a
human being while retrieving data from the websites. In this code, we
choose the example of retrieving job data from Glassdoor and perform
some analytics on it.

## test cases

* run `python -m test/test` to search for a particular job (set to be
  data scientist) in a given city (set to Berlin) and to retrieve
  information about the company, job title and the description. It
  will then save all data in `JSON` format in `data.json`.
