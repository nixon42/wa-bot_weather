from .weather import WeatherData
from .config import RAIN_THRESOLD


def gen_text(data: list[WeatherData]) -> str:
    shower_at = []
    for i, d in enumerate(data):
        if d.precipitation > RAIN_THRESOLD:
            shower_at.append(
                f'==> *{d.precipitation:.2f} mm*({d.precipitation_probability}%) @ *{i:02d}.00 WIB*')
    str_shower = '[🌧️] Hujan \n' + '\n'.join(shower_at)
    return str_shower
