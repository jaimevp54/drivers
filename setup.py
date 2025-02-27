from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="naas-drivers",
    version="0.48.0",
    author="Martin Donadieu",
    author_email="martindonadieu@gmail.com",
    license="BSD",
    description="Drivers made to easy connect to any services",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jupyter-naas/drivers",
    packages=find_packages(exclude=["tests"]),
    extras_require={
        "dev": [
            "pytest>=5,<7",
            "pytest-mock>=3,<4",
            "requests-mock>=1,<2",
            "twine>=3,<4",
            "flake8>=3,<4",
            "black",
            "commitizen>=2,<3",
            "pytest-cov>=2,<3",
        ]
    },
    install_requires=[
        "imap_tools>=0,<1",
        "slackclient>=2,<3",
        "pymsteams>=0,<1",
        "pdfkit>=0,<1",
        "markdown2>=2,<3",
        "newsapi-python>=0,<1",
        "airtable-python-wrapper>=0,<1",
        "notion>0,<1",
        "pyjwt>=1,<3",
        "tensorflow>=2,<3",
        "pysftp>=0,<1",
        "htmlbuilder>=0,<1",
        "vaderSentiment>=3,<4",
        "chardet>=3,<5",
        "Cython>=0,<1",
        "idna>=2,<4",
        "inflection>=0,<1",
        "joblib>=0,<2",
        "more-itertools>=8,<9",
        "numpy>=1,<2",
        "ipython>=7,<8",
        "pandas>=1,<2",
        "pandas-datareader>=0,<1",
        "patsy>=0,<1",
        "pmdarima>=1,<2",
        "python-dateutil>=2,<3",
        "python-dotenv>=0,<1",
        "pytz>=2020,<2022",
        "plotly>=4,<5",
        "kaleido",
        "Quandl>=3,<4",
        "requests>=2,<3",
        "scikit-learn>=0,<1",
        "torch>=1,<2",
        "scipy>=1,<2",
        "six>=1,<2",
        "statsmodels>=0,<1",
        "urllib3>=1,<2",
        "xlrd>=1,<3",
        "pymongo>=3,<4",
        "pysftp>=0,<1",
        "md2pdf>=0,<1",
        "sendgrid>=6,<7",
        "escapism>=1,<2",
        "openpyxl>=3,<4",
        "google-api-python-client>=1,<2",
        "google-auth-httplib2>=0,<1",
        "google-auth-oauthlib>=0,<1",
        "gspread>=3,<4",
        "oauth2client>=4,<5",
        "geopy>=1,<3",
        "GitPython>=3,<4",
        "cson>=0,<1",
        "opencv-python>=4,<5",
        "pytesseract>=0,<1",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: BSD License",
        "Framework :: Jupyter",
        "Operating System :: OS Independent",
    ],
)
