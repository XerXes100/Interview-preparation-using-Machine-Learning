import requests
import time
# from api_secrets import API_KEY_ASSEMBLYAI
import nlp

API_KEY_ASSEMBLYAI = "6f4af1b5524d4a47bd78908b09d989ec"

upload_endpoint = 'https://api.assemblyai.com/v2/upload'
transcript_endpoint = 'https://api.assemblyai.com/v2/transcript'

headers_auth_only = {'authorization': API_KEY_ASSEMBLYAI}

headers = {
    "authorization": API_KEY_ASSEMBLYAI,
    "content-type": "application/json"
}

CHUNK_SIZE = 5_242_880  # 5MB


def upload(filename):
    def read_file(filename):
        with open(filename, 'rb') as f:
            while True:
                data = f.read(CHUNK_SIZE)
                if not data:
                    break
                yield data

    upload_response = requests.post(upload_endpoint, headers=headers_auth_only, data=read_file(filename))
    return upload_response.json()['upload_url']


def transcribe(audio_url, sentiment_analysis):
    transcript_request = {
        'audio_url': audio_url,
        'sentiment_analysis': sentiment_analysis
    }

    transcript_response = requests.post(transcript_endpoint, json=transcript_request, headers=headers)
    return transcript_response.json()['id']


def poll(transcript_id):
    polling_endpoint = transcript_endpoint + '/' + transcript_id
    polling_response = requests.get(polling_endpoint, headers=headers)
    return polling_response.json()


def get_transcription_result_url(url, sentiment_analysis):
    transcribe_id = transcribe(url, sentiment_analysis)
    while True:
        data = poll(transcribe_id)
        if data['status'] == 'completed':
            return data, None
        elif data['status'] == 'error':
            return data, data['error']

        print("waiting for 30 seconds")
        time.sleep(30)


def save_transcript(url, title, sentiment_analysis=False):
    data, error = get_transcription_result_url(url, sentiment_analysis)
    # print(data['text'])

    if sentiment_analysis:
        # print(data['sentiment_analysis_results'])
        return data['text'], data['sentiment_analysis_results']
    return data['text'], data['sentiment_analysis_results']
    # if data:
    #     filename = title + '.txt'
    #     with open(filename, 'w') as f:
    #         f.write(data['text'])
    #     print('Transcript saved')
    # elif error:
    #     print("Error!!!", error)


# import requests
#
# # from api_02 import *
#
# filename = "output.wav"
# audio_url = upload(filename)
#
#
#
# s, t = save_transcript(audio_url, 'file_title', sentiment_analysis=True)
# print(nlp.entity_analysis(s))
# print(s)
# print(nlp.entity_analysis_q1(s))
# print(t[1])