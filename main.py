import os
import requests
from logger import logger

path = 'main.log'

class SuperHero:
  
    base_url = 'https://akabab.github.io/superhero-api/api'
    
    @logger(path)
    def _get_data(self):
        uri = '/all.json'
        request_url = self.base_url + uri
        headers = {'Content_Type': 'application/json'}
        response = requests.get(request_url, headers = headers)
        data = response.json()
     
        list_heroes=[]
        for hero in data:
            list_heroes.append({'id': hero['id'],
                                'name': hero['name'],
                                'intelligence':  hero['powerstats']['intelligence']})
        return list_heroes

    @logger(path)
    def find_id_hero_by_name(self, name_hero):
        list_heroes = self._get_data()
        for hero in list_heroes:
            if hero['name'] == name_hero:
                id_hero = hero['id']
                break
        return id_hero
    
    @logger(path)
    def add_intalligence_by_name(self, name_hero):
        list_heroes = self._get_data()
        for hero in list_heroes:
            if hero['name'] == name_hero:
                intelligence = hero['intelligence']
                break
        return intelligence

class Heroes:

    @logger(path)
    def __init__(self, id_hero, name, intelligence=0):
        self.id = id_hero
        self.name = name
        self.intelligence = intelligence

    @logger(path)
    def __lt__(self, other):
        if not isinstance(other, Heroes):
            print(f'Ошибка. {other} не относится к классу Heroes')
        else:
            return self.intelligence < other.intelligence
    
    @logger(path)
    def __str__(self):
        res = f'{self.name} id({self.id}): intelligence = {self.intelligence} '
        return res

if __name__ == '__main__':
    
    if os.path.exists(path):
        os.remove(path)

    sh = SuperHero()
    
    hulk = Heroes(sh.find_id_hero_by_name('Hulk'),'Hulk', sh.add_intalligence_by_name('Hulk'))
    thanos = Heroes(sh.find_id_hero_by_name('Thanos'),'Thanos', sh.add_intalligence_by_name('Thanos'))
    captain_america= Heroes(sh.find_id_hero_by_name('Captain America'),'Captain America', sh.add_intalligence_by_name('Captain America'))
    
    list_heroes = [hulk, thanos, captain_america]
    print(f'Сравниваем:\n{hulk}\n{thanos}\n{captain_america}')
    print('---'*10)
    print(f'Самый сильный: {max(list_heroes)}')