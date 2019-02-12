import requests


class GenderDetector:

    def run(self, name):
        result = requests.get('https://api.genderize.io/?name={}'.format(name))
        return result.json()['gender']
