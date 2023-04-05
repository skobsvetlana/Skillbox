import re
from typing import List

text: str = 'А578ВЕ777 ОР233787 К901МН666 К901МZ666 СТ46599 СНИ2929П777 666АМР666'

auto_pattern: str = r'\b[АВЕКМНОРСТУХ]{1}\d{3}[АВЕКМНОРСТУХ]{2}\d{3}\b'
taxi_pattern: str = r'\b[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}\b'

taxi: List[str] = re.findall(pattern=taxi_pattern, string=text)
private_auto: List[str] = re.findall(pattern=auto_pattern, string=text)

print('Список номеров частных автомобилей: {}'.format(private_auto))
print('Список номеров такси: {}'.format(taxi))
