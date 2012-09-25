
kwargs={}

# fall back on no plugin-extensions and no dependency handling if setuptools 
# is not installed.
try:
    from setuptools import setup
    kwargs["install_requires"]=["rdflib>3", "html5lib"]
    kwargs["entry_points"]={
        "rdf.plugins.parser" : [ "mdata = pyMicrodata.rdflib:MicrodataParser",
                                 "microdata = pyMicrodata.rdflib:MicrodataParser"],
        }

    # several details or simply a more complete serialization depends on pyRdfa
    # Although the basic RDF conversion works without this, some serializations
    # may not be available and the vocabulary expansion mechanism would not
    # work either. 
    kwargs["extras_requires"]={ "Rdfa" : ["pyRdfa>3"] }

except:
    from distutils.core import setup

setup(name="pyMicrodata",
      description="pyMicrodata Libray",
      version="1.2",
      author="Ivan Herman",
      author_email="ivan@w3.org",
	  maintainer="Ivan Herman",
	  maintainer_email="ivan@w3.org",
      packages=["pyMicrodata"],
      **kwargs
      )

