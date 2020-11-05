def parse_top_stories(cmpt, ctype='top_stories'):
    """Parse a "Top Stories" component

    These components contain links to news articles and often feature an image.
    Sometimes the subcomponents are stacked vertically, and sometimes they are
    stacked horizontally and feature a larger image, resembling the video 
    component.
    
    Args:
        cmpt (bs4 object): A "Top Stories" component
    
    Returns:
        list : list of parsed subcomponent dictionaries
    """
    subs = cmpt.find_all('g-inner-card')
    if subs:
        return [parse_top_story(sub, ctype, sub_rank) for sub_rank, sub in enumerate(subs)]
    else:
        subs = cmpt.find('div', {'class':'qmv19b'}).children
        return [parse_top_story(sub, ctype, sub_rank) for sub_rank, sub in enumerate(subs)]


def parse_top_story(sub, ctype, sub_rank=0):
    """Parse "Top Stories" component
    
    Args:
        sub (bs4 object): A "Top Stories" subcomponent
    
    Returns:
        dict: A parsed subresult
    """
    parsed = {'type':ctype, 'sub_rank':sub_rank}
    a = sub.find('a')
    parsed['title'] = a.text if a else None
    parsed['url'] = a['href'] if a else None

    cite = sub.find('cite')
    parsed['cite'] = cite.text if cite else None

    timestamp = sub.find('span', {'class':['f', 'uaCsqe']})
    parsed['timestamp'] = timestamp.text if timestamp else None

    # Extract component specific details
    details = {}
    details['img_url'] = get_img_url(sub)
    details['orient'] = 'v' if sub.find('span', {'class':'uaCsqe'}) else 'h'
    details['live_stamp'] = True if sub.find('span', {'class':'EugGe'}) else False
    parsed['details'] = details
    
    return parsed

def get_img_url(soup):
    """Extract image source"""    
    img = soup.find('img')
    if img and 'data-src' in img.attrs:
        return img.attrs['data-src']
