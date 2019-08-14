# Nursing-home-lookup-tool
NJAM lookup tool for nursing homes in New Jersey.

### What this is
The data workflow, result and front-end Flask application to create the nursing home lookup tool. There are two things here: a Jupyter notebook that feeds from several data sources and the data it creates, and the Flask application that takes that data and visualizes it on the front end.

### Data sources and workflow

The two main data sources are:
- The CMS [cost report data](https://www.cms.gov/Research-Statistics-Data-and-Systems/Downloadable-Public-Use-Files/Cost-Reports/SkilledNursingFaciilty-2010-form.html) for Skilled Nursing Facilites, currently only complete for 2017. This is used for _only_ the staffing rank and staffing hours for each type of nurse in the tool. I used this because I believe it's more accurate than the self-reported staffing hours for the nursing homes in the Nursing Home Compare data.
- The CMS Nursing Home Compare data, updated on a rolling basis: https://data.medicare.gov/data/nursing-home-compare. This is used for the overall rating, the staffing rating, the Quality measures and the inspection information.

Those two are parsed and merged using the NPI / Federal Provider Number in the Jupyter notebook and spits out a CSV and JSON for the front-end tool.

## Front-end tool
The Flask application is based heavily on the NICAR [first news app](https://first-news-app.readthedocs.io/en/latest/) tutorial using Flask. The big difference is that I threw in a datatables lookup table on the homepage, and there's an additional bit of script in the detail pages to calculate the bar charts and create the dropdown menu. Main components are:

- app.py: Creates the structure of the application that feeds the data into each page.
- templates for index.html and detail.html: index.html is the homepage of the tool with a Leaflet map and Datatables searchable table for the nursing homes. Datatables was not compatible with the rest of the app, so it's fed by a JSON with a basic version of the data. detail.html is what shows up for each individual nursing home.
- static: The folder that contains the data itself, the CSS for the tool and any and all files (images, fonts, etc.) needed. I used .scss to create the more complex css needed for the detail pages.

Once I finished developing the tool, I used Frozen-Flask as outlined in the above tutorial to create all of the static pages. However, I had to change a handful of links to the static css files and the hyperlinks to the detail pages.
