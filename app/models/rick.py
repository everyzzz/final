import requests


class Rick_Morty:    

    def __init__(self,id, name,status,species,gender, img_url, origin, location, episode):
        self.id= id
        self.name=name
        self.status=status
        self.species = species
        self.gender = gender
        self.img_url=img_url
        self.origin= origin
        self.location=location
        self.episode=episode
    def to_json(self):
        return {
            "id":self.id,
            "name":self.name,
            "status":self.status,
            "species":self.species,
            "gender":self.gender,
            "img_url":self.img_url,
            "origin":self.origin,
            "location":self.location,
            "episode":self.episode
        }    
    
    """  def gravatar(self, size=100, default='identicon', rating='g'):
        return self.img
    """