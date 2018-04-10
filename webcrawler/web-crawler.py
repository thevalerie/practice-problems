# Implement a Web Crawler

# Implement a function, `crawl(url)`, that crawls all web pages (i.e., URLs)
# reachable from `url`. The return result should map each web page to
# the list of links on that web page.

# Assume you have a helper function, `get_links(url)`, that returns the
# list of links on a web page.  For example,
# `get_links('http://foo.com')` might return: `['http://foo.com/bar', 'http://baz.com']`.

# ## Complete example

# Consider a *very small* network with three web pages, http://foo.com,
# http://foo.com/bar, and http://baz.com.

# http://foo.com:
# ```
# <html>
#   <body>
#     Foo.com links:
#     <a href="http://foo.com/bar">http://foo.com/bar</a>
#     <a href="http://baz.com">http://baz.com</a>
#   </body>
# </html>
# ```

# http://foo.com/bar:
# ```
# <html>
#   <body>
#     <a href="http://foo.com">Go back to the main page.</a>
#   </body>
# </html>
# ```

# http://baz.com:
# ```
# <html>
#   <body>
#     Welcome to baz.com
#   </body>
# </html>
# ```

# `crawl('http://foo.com')` should return this result:
# ```json
# {
#   "http://foo.com": [
#     "http://foo.com/bar",
#     "http://baz.com"
#   ],
#   "http://foo.com/bar": [
#     "http://foo.com"
#   ],
#   "http://baz.com": []
# }
# ```

def get_links(url):
    """Takes a URL and returns a list of URLs that are linked from that URL"""

    if url == 'http://foo.com':
        return ['http://foo.com/bar', 'http://baz.com']
    elif url == 'http://foo.com/bar':
        return ['http://foo.com']
    else:
        return []


def crawl(url):
    """Takes a URL and returns a JSON object with each URL as the key and the list of linked URLs as values"""

    stack = [url]
    all_links = {}

    while stack:
        current = stack.pop()
        if current in all_links:
            continue
        linked_urls = get_links(current)
        # add the url and the list of links on that URL as a key: value pair to my dictionary
        all_links[current] = linked_urls
        # add all linked URLs to the stack
        if linked_urls:
            stack.extend(linked_urls)

    return all_links


