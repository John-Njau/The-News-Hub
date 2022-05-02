class Articles:
    def __init__(self,image,description, time, url, title, author):
        self.image = image
        self.description = description
        self.time = time
        self.url = url
        self.title = title
        self.author = author
        
class Sources:
    def __init__(self, id, name, description, url, country, language, category):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.country = country
        self.language = language
        self.category = category
        
