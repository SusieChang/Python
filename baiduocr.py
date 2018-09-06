from aip import AipOcr

APP_ID = '11730410'
API_KEY = 'Teuyu8PygKTn8KEdUqLTTvh1'
SECRET_KEY = 'rIqEyFe6TkFTKrt7Isa9rvsG9vzTELCT '
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('example.jpg')

""" 调用通用文字识别（高精度版） """
client.basicAccurate(image);

""" 如果有可选参数 """
options = {}
options["detect_direction"] = "true"
options["probability"] = "true"

""" 带参数调用通用文字识别（高精度版） """
client.basicAccurate(image, options)