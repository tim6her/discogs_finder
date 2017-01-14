# discogs_finder
**FIND** **E**very **R**elease in your collection

This is a small commandline tool that fetches your discogs collection and performs a deep key value search.

    $ discogs-finder name=Chick
    Searching for {'name': 'Chick'}
    1)	Herbie Hancock & Chick Corea: An Evening With Herbie Hancock & Chick Corea In Concert 1978 (530041)
    	basic_information.artists.1.name = Chick Corea
    2)	Chick Corea & Friedrich Gulda: The Meeting (2210545)
    	basic_information.artists.0.name = Chick Corea
    3)	Wolfgang Amadeus Mozart, Chick Corea, Friedrich Gulda, Concertgebouworkest, Nikolaus Harnoncourt: Double Concerto / Compositions (4764105)
    	basic_information.artists.1.name = Chick Corea

For help on usage run `python finder.py --help`.