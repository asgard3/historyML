import abc

class Button(object):
    __metaclass__ = abc.ABCMeta

    html = ""
    def get_html(self, html):
        return self.html
