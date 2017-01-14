#!/usr/bin/env python

import click
import json
import urllib2
import re


def load_data(username):
    url = 'https://api.discogs.com/users/%s/collection/folders/0/releases'
    url = url % username
    s_data = urllib2.urlopen(url)

    return json.load(s_data)['releases']

def release_string(d_release):
    release_id = d_release['id']
    basics = d_release.get('basic_information', None)
    if not basics:
        raise KeyError ("Your release %d doesn't contain"
                " the field 'basic_information'" % release_id)
    artists = basics.get('artists', None)
    if len(artists):
        j = artists[0]['join']
        if j == ',':
            j = '%s ' % j
        else:
            j = ' %s ' % j
        arts = j.join((a['name'] for a in artists))
    else:
        arts = None
    
    title = basics.get('title', None)
    
    return u'{arts}: {title} ({release_id})'.format(arts=arts,
                                            title=title,
                                            release_id=release_id)

def found_in_release(data, add=None, **querry):
    add = [] if not add else add
    if type(data) == list:
        sub = (found_in_release(d, add + [unicode(i)], **querry) 
                        for i, d in enumerate(data))
        
    elif type(data) == dict:
        field = querry.keys()[0]
        value = querry[field]
        if unicode(value).lower() in unicode(data.get(field, '')).lower():
            return True, add + [unicode(field)], data[field]
        
        sub = (found_in_release(d, add + [k], **querry)
                        for k, d in data.iteritems())
        
    else:
        return False, add, None
    
    hits = [(f, a, v) for f, a, v in sub if f]

    if len(hits):
        return hits[0]
    else:
        return False, add, None
        
@click.command(context_settings=dict(
    ignore_unknown_options=True,
))
@click.argument('querry', nargs=-1, type=click.UNPROCESSED)
def finder(querry):
    """ FIND Every Release:

Find the releases in your collection with an easy key value search.
    """
    user = 'tim6her'
    

    p_arg = re.compile(r'(\w+)=([\w\s]+)')
    match = p_arg.match(querry[0])
    if match:
        q = {match.group(1): match.group(2)}
    else:
        raise KeyError('Could not match your querry to value=key')
    
    print 'Searching for ' + str(q)
    data = load_data(user)
    
    result = []
    for r in data:
        f, a, v = found_in_release(r, None, **q)
        if f:
            s = '%d)\t%s\n\t%s = %s' % (len(result) + 1,
                                    release_string(r), 
                                    '.'.join(a), v)
            result.append(s)
    print '\n'.join(result)
    
if __name__ == '__main__':
    finder()