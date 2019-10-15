from django.test import TestCase
from LoveAndShare import settings
# Create your tests here.
import qiniu
from qiniu import Auth, put_file, etag


def qntoken(file_data):
    access_key = settings.QINIU_ACCESS_KEY
    secret_key = settings.QINIU_SECRET_KEY
    q = qiniu.Auth(access_key, secret_key)
    bucket = settings.QINIU_BUCKET_NAME
    token = q.upload_token(bucket)
    ret, info = put_file(token, None, file_data)
    print("ret",ret['key'])
    print("ret",ret)
    print("info",info)
    assert ret['key'] == key
    assert ret['hash'] == etag(localfile)

    if info.status_code == 200:
        # 表示上传成功, 返回文件名
        return ret.get("key")
    else:
        # 上传失败
        raise Exception("上传七牛失败")


s="./../../media/img/top.jpg"

qntoken(s)

