import fitz
import requests

def papago_api(id, secret, sen):
    request_url = "https://openapi.naver.com/v1/papago/n2mt"
    headers = {"X-Naver-Client-Id": id, "X-Naver-Client-Secret": secret}
    params = {"source": "en", "target": "ko", "text": sen}
    response = requests.post(request_url, headers=headers, data=params)
    result = response.json()

    return  result["message"]["result"]["translatedText"]

if __name__ == "__main__":

    doc = fitz.open("./test.pdf")
    to_text = ""
    for i in doc:
        to_text = to_text + i.getText()

    file = open("./to_text.txt", 'wb')
    file.write(to_text.encode("UTF-8"))
    file.close()

    # 수정한 파일을 다시 불러옵니다.
    file = open("./to_text.txt", 'rb')
    lines = file.readlines()
    file.close()

    last_list = list()
    temp = ""

    for i in lines:
        i = i.decode("UTF-8")
        i = i.replace("\n", " ")

        if len(temp + i) > 5000:
            last_list.append(temp)
            temp = ""
        else:
            temp = temp + i

    for i in range(0,len(last_list)):
        try:
            file = open("./translated_text_{}.txt".format(i), 'w')
            sen = papago_api("발급받은 클라이언트ID 입력", "발급받은 Secret코드 입력", last_list[i])
            file.write(sen+"\n")
            file.close()
        except Exception as e:
            print(e)
            file.close()
