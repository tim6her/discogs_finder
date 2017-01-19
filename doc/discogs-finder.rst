Usage: discogs-finder [OPTIONS] [QUERRY]...

FIND Every Release:
===================
    
Find the releases in your collection with an easy
key value search.  The script 'discogs-finder' 
accepts one QUERRY that is specified in form of
a 'key=value' format.  If the value contains 
whitespace, the argument must be contained in 
"quotation marks".

Examples:
---------

::

    $ discogs-tagger --u titm6her name="Keith Jarrett"
    $ discogs-tagger --u titm6her name="ABC Impulse!"
    $ discogs-tagger --u --v titm6her title="An Evening"
    $ discogs-tagger --u titm6her id=3318191

Options:
--------

  --u TEXT  Your discogs user name
  --v       Verbose output dumping the whole json-file
  --p       Pretty output
  --help    Show this message and exit.