
kwargs={}

# fall back on no plugin-extensions and no dependency handling if setuptools 
# is not installed.
try:
    from setuptools import setup
    kwargs["install_requires"]=['rdflib', 'html5lib']
    kwargs["entry_points"]={
        'rdf.plugins.parser' : [ 'mdata = pyMicrodata.rdflib:MicrodataParser',
                                 'microdata = pyMicrodata.rdflib:MicrodataParser'],
        }

except:
    from distutils.core import setup

setup(name="pyMicrodata",
      description="pyMicrodata Libray",
      version="1.2",
      author="Ivan Herman",
      author_email="ivan@w3.org",
	  maintainer="Ivan Herman",
	  maintainer_email="ivan@w3.org",
      packages=['pyMicrodata'],
      **kwargs
      )

