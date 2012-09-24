from rdflib import Parser, StringInputSource, URLInputSource, FileInputSource

class MicrodataParser(Parser) :
	def parse(self, source, graph,
			  vocab_expansion        = False,
			  vocab_cache            = False,
			  rdfOutput              = False) :
		"""
		@param source: one of the input sources that the RDFLib package defined
		@type source: InputSource class instance
		@param graph: target graph for the triples; output graph, in RDFa spec. parlance
		@type graph: RDFLib Graph
		@keyword vocab_expansion: whether the RDFa @vocab attribute should also mean vocabulary expansion (see the RDFa 1.1 spec for further details)
		@type vocab_expansion: Boolean
		@keyword vocab_cache: in case vocab expansion is used, whether the expansion data (i.e., vocabulary) should be cached locally. This requires the ability for the local application to write on the local file system
		@type vocab_chache: Boolean
		@keyword rdfOutput: whether Exceptions should be catched and added, as triples, to the processor graph, or whether they should be raised.
		@type rdfOutput: Boolean
		"""		

                from pyMicrodata import pyMicrodata

                if isinstance(source, StringInputSource) :
                        orig_source = source.getByteStream()
                elif isinstance(source, URLInputSource) :
                        orig_source = source.url
                elif isinstance(source, FileInputSource) :
                        orig_source = source.file.name
                        source.file.close()

                baseURI      = source.getPublicId()
                processor    = pyMicrodata(base = baseURI, vocab_expansion = vocab_expansion, vocab_cache = vocab_cache)
                processor.graph_from_source(orig_source, graph=graph, rdfOutput = rdfOutput)
