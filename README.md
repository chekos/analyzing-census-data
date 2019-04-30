# Analyzing Census Data with Pandas
## PyCon 2019
***

Materials for my Analyzing Census Data with Pandas workshop for PyCon 2019.

TODO:
- add installation instructions
- add "basics" notebook
    - includes imports (pandas pathlib datetime)
    - directory structure
    - pandas most common commands
        - load data
        - `.info()`, `.shape`, `.head()`
        - `.sum()`, `.max()`, `.min()` and their behavior (series v dataframes)
        - dropping columns
        - dropping rows
            - conditional indexing
            - example of keeping households w/ children (slicing by condition on another col)
        - saving data
- add exercises
    - pandas basics: dataframe / series, data types / nan, 
    - read in data: zipped files, regular files. 
    - subsets: `.loc`, `.iloc`, `df[col]` vs `df[[col]]`
    - indexing: conditions / boolean stuff, `.query()`, dropping columns / rows, `.filter()`, 
    - grouping: aggregating, melting, unstacking, pivot_tables. 
- make mybinder-stable branch

Exercises:
- Project #1: Internet Access by Race/Ethnicity in a certain geography (i.e. X counties, X states, x county in x state)
- Project #2: Employment-to-Population ratio example
- Project #3 (requires good internet): We'll use census-data-downloader or censusdata go get a dataset and find Qs