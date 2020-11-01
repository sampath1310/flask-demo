class ISBNDO(dict):
    def __init__(self, title, subtitle, description, published_date):
        self['title'] = title
        self['subtitle'] = subtitle
        self['description'] = description
        self['published_date'] = published_date

    @property
    def title(self):
        return self['title']

    @title.setter
    def title(self, title):
        self['title'] = title

    @property
    def subtitle(self):
        return self['subtitle']

    @subtitle.setter
    def subtitle(self, subtitle):
        self['subtitle'] = subtitle

    @property
    def description(self):
        return self['description']

    @description.setter
    def description(self, description):
        self['description'] = description

    @property
    def published_date(self):
        return self['published_date']

    @published_date.setter
    def published_date(self, published_date):
        self['published_date'] = published_date
