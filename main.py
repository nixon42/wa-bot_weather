from utils import weather, plot
from utils.util import gen_text
from utils.config import CHAT_ID, GREENAPI_API_KEY, GREENAPI_INSTANCE
from whatsapp_api_client_python import API

weather = weather.get_wheater_data()
plot.plot_to_a_file(weather, 'plot.png')
caption = gen_text(weather)

greenAPI = API.GreenAPI(GREENAPI_INSTANCE, GREENAPI_API_KEY)

response = greenAPI.sending.sendFileByUpload(
    CHAT_ID,
    'plot.png',
    'plot.png',
    caption
)
