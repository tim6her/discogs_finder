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

def found_in_release(data, **querry):
    if type(data) == list:
        sub = (found_in_release(d, **querry) for d in data)
        
    elif type(data) == dict:
        field = querry.keys()[0]
        value = querry[field]
        if unicode(value) in unicode(data.get(field, '')):
            return True
        
        sub = (found_in_release(d, **querry) for d in data.values())
        
    else:
        return False
    
    #print list(sub)
    return any(sub)
        
@click.command(context_settings=dict(
    ignore_unknown_options=True,
))
@click.argument('querry', nargs=-1, type=click.UNPROCESSED)
def finder(querry):
    user = 'tim6her'
    

    p_arg = re.compile(r'(\w+)=([\w\s]+)')
    match = p_arg.match(querry[0])
    if match:
        q = {match.group(1): match.group(2)}
    else:
        raise KeyError('Could not match your querry to value=key')
    
    print 'Searching for ' + str(q)
    data = load_data(user)
    result = (release_string(r) for r in data 
                        if found_in_release(r, **q))
    print '\n'.join(result)
    
if __name__ == '__main__':
    finder()