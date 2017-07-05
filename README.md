# a simple WebScraping Python code

WebScraping is a Python code to illustrate data acquisition using
`selenium` library. For this purpose, one needs often to emulate a
human being while retrieving data from the websites. In this code, we
choose the example of retrieving job data from Glassdoor and perform
some analytics on it.

## test cases

1. run `python -m test/test` to search for a particular job (set to be
  data scientist) in a given city (set to Berlin) and to retrieve
  information about the company, job title and the description. It
  will then save all data in `JSON` format in `data.json`.

2. run `python -m test/test0` to read the data file `data.json` and
   perform analytics on the programming skills needed for a data
   science job. The result is saved as a figure in `output`
   folder:
   ![](output/skills_prog.png)
   
   As we can see `python` and `R` are by far the most popular
   scripting languages of data science. The above statistics are
   obtained by the functions defined in `src/DataCleaning.py`.
   
   Here are some more statistics:
   ![](output/skills_ds.png)
   
