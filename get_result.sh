#!/bin/bash

curl -i -k 'https://aip.baidubce.com/rest/2.0/face/v3/match?access_token=24.5ae1f2eb5d8faf36f3d0222dd6aabaa3.2592000.1588094551.282335-19152882' --data '[{"image": "https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=1528147186,891408054&fm=26&gp=0.jpg", "image_type": "URL", "face_type": "LIVE", "quality_control": "LOW"},
 {"image": "https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=3934828190,3882777681&fm=26&gp=0.jpg", "image_type": "URL", "face_type": "LIVE", "quality_control": "LOW"}]' -H 'Content-Type:application/json; charset=UTF-8'
