import zAI
from zAI import zImage

zAI.utils.set_backend_key(key_name='MICROSOFT_AZURE_VISION_API_KEY', key_value='애져API키를 입력하세요.', save=True)
zAI.utils.set_backend_key(key_name='MICROSOFT_AZURE_URL', key_value='japaneast.api.cognitive.microsoft.com', save=True)

# 이미지 지정
image = zImage('./img/test.png')
image.display()

# 이미지 인식
text = image.ocr(backend='Microsoft')
text.display()


