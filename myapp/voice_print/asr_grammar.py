#!/usr/bin/env python
from requests import post
import consts
import datetime
import hashlib


class SinoVoiceAsrRecogniser(object):
    def __init__(self, file_name):
        self._file_name = file_name
        self._headers = {}

    def recognise(self):
        self.__get_headers()
        response = post(consts.ASR_CLOUD_SERVER, data=self.__read_audio(), headers=self._headers)
        return response.text

    def __get_headers(self):
        self._headers['Content-Type'] = consts.CONTENT_TYPE
        self._headers['charset'] = consts.CHARSET
        self._headers['x-app-key'] = consts.APP_KEY
        self._headers['x-sdk-version'] = consts.SDK_VERSION
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._headers['x-request-date'] = date
        session_key_str = date + consts.DEVELOPER_KEY
        session_key_md5 = hashlib.md5(session_key_str).hexdigest()
        self._headers['x-session-key'] = session_key_md5
        task_config = 'addpunc=no,audioformat=pcm16k16bit,capkey=' + consts.CAP_KEY + \
                      ',grammarid=10421,grammartype=jsgf,mode=grammar,lang=chinese,'
        self._headers['x-task-config'] = task_config
        self._headers['x-udid'] = consts.UD_ID

    def __read_audio(self):
        if self._file_name:
            with open(self._file_name, 'rb') as fp:
                audio_bytes = fp.read()
                return audio_bytes
        return ""


def main():
    recogniser = SinoVoiceAsrRecogniser("E:\\PCM_TEST\\svoice_pri1.wav")
    response = recogniser.recognise()
    print response


if __name__ == '__main__':
    main()
