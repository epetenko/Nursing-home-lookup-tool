# Nursing-home-lookup-tool
NJAM lookup tool for nursing homes in New Jersey.

### What this is
The data workflow, result and front-end Flask application to create the nursing home lookup tool. There are two things here: a Jupyter notebook that feeds from several data sources and the data it creates, and the Flask application that takes that data and visualizes it on the front end.

### Data sources and workflow

The two main data sources are:
- The CMS cost report data for Skilled Nursing Facilites, currently only complete for 2017: https://www.cms.gov/Research-Statistics-Data-and-Systems/Downloadable-Public-Use-Files/Cost-Reports/SkilledNursingFaciilty-2010-form.html. This is used for _only_ the staffing rank and staffing hours for each type of nurse in the tool.
- The CMS Nursing Home Compare data, updated on a rolling basis: https://data.medicare.gov/data/nursing-home-compare. This is used for the overall rating, the staffing rating, the Quality measures and the inspection information.

Those two are parsed and merged using the NPI / Federal Provider Number in the Jupyter notebook and spits out a CSV and JSON for the front-end tool.

## Front-end tool
The Flask application is based heavily on the NICAR [first news app](https://first-news-app.readthedocs.io/en/latest/) tutorial using Flask. The big difference is that I threw in a datatables lookup table on the homepage, and there's an additional bit of script in the detail pages to calculate the bar charts and create the dropdown menu.
