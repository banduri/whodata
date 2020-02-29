source
==

All data is mostly manual extracted from PDFs hosted at https://www.who.int/emergencies/diseases/novel-coronavirus-2019/situation-reports

pdf
==
for simple access to the pdfs they are also stored in the pdf-subdir

dataextraction
==
The pdfs do not provide a datascience friendly way to access the strucked data. There is no json or csv provied by the WHO.

The raw text data is extracted by making a screenshot and sending it through the OCR-software tesseract.

``bash
tesseract foo.png foo.png -l eng --psm 4
``
the option '--psm 4' means '4 = Assume a single column of text of variable sizes.'

after that some manual cleanup is done

about data
==

without_china.ndjson provides the cleaned data from the reports. without_china_enrich.ndjson enriches the data with some precalculations done by enrich_data.py. enrich_data.py can only deal with json-data conversion is needed

**loc**: Location (string / label)

**cumultative_confirmed_cases**: all cases (not active infections) reported to the WHO. (includes daily change and all cases that resulted in death) (integer)

**daily_confirmed_cases**: change from the prev. day - new cases (integer)

**cumultative_deaths**: all reported deaths of cases (includes daily change) (integer)

**daily_deaths**: change from the prev. day (integer)

**data**: date of the report. (format: yyyy-MM-dd 00:00:00) 

**active_confirmed_infections**: active infections; cases without those cases that resulted in death (integer)

**rate_cases**: daily_confirmed_cases / cumultative_confirmed_cases (float 0 <= x <= 1)

**change_rate_cases**: changes from the prev report. daily_confirmed_cases / (cumultative_confirmed_cases - daily_confirmed_cases ) (float x >= 0)

**change_rate_deaths**: changes from the prev report. daily_deaths / ( cumultative_deaths - daily_deaths ) (float range x >= 0)

**rate_mortality**: likelyhood of death (cumultative_deaths / cumultative_confirmed_cases) (float: 0 <= x <= 1)

**rate_deaths**: daily_deaths / cumultative_deaths (float 0 <= x <= 1)
