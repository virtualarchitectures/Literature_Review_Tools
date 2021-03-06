# Literature Review Tools
This repository contains a series of Jupyter notebooks using Python modules Arcas and Scholarly to assist in the early stages of academic literature review.

## Technical documentation

This repository contains Jupyter notebooks which demonstrate the use of a number of Python modules to assist in the search and evaluation of literature for an academic [literature review](https://www.scribbr.com/dissertation/literature-review/).

#### Arcas Notebook

Arcas is a python module providing programmatic access to metadata from the following journals:

- IEEE (10 calls per minute / 200 calls per day)
- PLOS
- Nature
- Springer
- arXiv

To use this notebook you need to install the Arcas module from the command line using `pip install arcas`.

Arcas GitHub repository: https://github.com/ArcasProject/Arcas
Arcas documentation: http://arcas.readthedocs.io/en/latest/index.html

Currently, the following APIs require you to register for an API key:

- IEEE Xplore: https://developer.ieee.org/member/register
- Springer Open Access API: https://dev.springernature.com/login

The API keys currently have to be added to files within the module source code: https://arcas.readthedocs.io/en/latest/Guides/api_key.html

#### Scholarly Notebook

Scholarly is a python module providing programmatic access to metadata from Google Scholar.

To use this notebook you need to install the Scholarly module from the command line using `pip install scholarly`.

Scholarly github repository: https://github.com/scholarly-python-package/scholarly
Scholarly documentation: https://scholarly.readthedocs.io/en/stable/

**Warning:** Google Scholar can block your IP address when using Scholarly. These temporary bans can last for between 1 and 48 hours. To avoiding issues of this kind it is advised that you use a proxy server. Refer to the Scholarly GitHub page and documentation for further information.

Be aware that the more people that use a specific proxy server to access Google Scholar, the more likely it will be for that server to be blocked when you try to use it. The `FreeProxies()` method has been tested but actually performed less well than using a VPN without a proxy. Similarly TOR exit points can also be flooded by too many users and blocked by Google.

**Error Handling:** If you receive the message `Exception: Cannot fetch the page from Google Scholar` this means that you have been temporarily blocked by Google Scholar. This usually occurs because Google responded to the HTTP request from Scholarly with a CAPTCHA. These aren't currently handled by the library. Current workarounds involve the integration with Selenium which gives users the ability to solve the CAPTCHA: https://github.com/scholarly-python-package/scholarly/issues/131

### Dependencies

- [Jupyter Notebooks](https://jupyter.org/) - Provides a notebook interface for writing and running Python code interactively.

Jupyter Notebooks can either be installed directly, or with the [Anaconda](https://www.anaconda.com/) distribution of Python. 

### Running the notebooks

1. Clone this repository with a GitHub client or click the 'Code' button at thew top of this page to download the zip file. Ensure you extract the zipped files and note the file location.
2. Launch the Jupyter notebook application on your computer.
3. Navigate to the location of the downloaded files using the Jupyter interface.
4. Double click on the desired notebook. Either `Arcas_Literature_Review.ipynb` or `Scholarly_Literature_Review.ipynb`.

## Licence

[MIT License](LICENCE)
