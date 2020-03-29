# encoding:utf-8

import requests
import base64

'''
face matching
'''

def base64Encode(face_img_path):
  face_img = open(face_img_path, 'rb')
  face_img_read = face_img.read()
  face_img_base64_encode_str = str(base64.b64encode(face_img_read), 'utf-8')

  # print(face_img_base64_encode)
  return '"' + face_img_base64_encode_str + '"'

def matchTwoFace(face_1, face_2):
  request_url = "https://aip.baidubce.com/rest/2.0/face/v3/match"
  # params = "[{\"image\": \"https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=1528147186,891408054&fm=26&gp=0.jpg\", \"image_type\": \"URL\", \"face_type\": \"LIVE\", \"quality_control\": \"LOW\"}, {\"image\": \"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=3934828190,3882777681&fm=26&gp=0.jpg\", \"image_type\": \"URL\", \"face_type\": \"LIVE\", \"quality_control\": \"LOW\"}]"
  # params = "[{\"image\": " + face_1 + ", \"image_type\": \"URL\", \"face_type\": \"LIVE\", \"quality_control\": \"LOW\"}, {\"image\": " + face_2 + ", \"image_type\": \"URL\", \"face_type\": \"LIVE\", \"quality_control\": \"LOW\"}]"
  params = "[{\"image\": " + face_1 + ", \"image_type\": \"BASE64\", \"face_type\": \"LIVE\", \"quality_control\": \"LOW\"}, {\"image\": " + face_2 + ", \"image_type\": \"BASE64\", \"face_type\": \"LIVE\", \"quality_control\": \"LOW\"}]"
  # print(params)
  access_token = '[24.5ae1f2eb5d8faf36f3d0222dd6aabaa3.2592000.1588094551.282335-19152882]'
  request_url = request_url + "?access_token=" + access_token
  headers = {'content-type': 'application/json'}
  response = requests.post(request_url, data=params, headers=headers)

  if response:
    match_score = response.json()['result']['score']
    if match_score > 95: 
      print("matching succeed, match_score:", match_score)
    else:
      print("match failed. match_score:", match_score)
    # print(response.json())


if __name__ == "__main__":
  base_path = './pictures/'
  face1_path = 'huge_1.jpg'
  face2_path = 'huge_2.jpg'
  face1_encode = base64Encode(base_path + face1_path)
  face2_encode = base64Encode(base_path + face2_path)
  matchTwoFace(face1_encode, face2_encode)
  # url1 = '\"https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=1528147186,891408054&fm=26&gp=0.jpg\"'
  # url2 = '\"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=3934828190,3882777681&fm=26&gp=0.jpg\"'
  # matchTwoFace(url1, url2)
