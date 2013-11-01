
def get_next_target(s):
    """
    html -> url, end_quote
    """
    start_link = s.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = s.find('"', start_link)
    end_quote = s.find('"', start_quote+1)
    url = s[start_quote+1:end_quote]
    return url, end_quote

def print_all_links(page):
    while page:
        url, endpos = get_nex_target(page)
        if url:
            print(url)
            page = page[endpos:]
        else:
            break

def get_page(page):
    import urllib2
    source = urllib2.urlopen(page)
    return source.read()
