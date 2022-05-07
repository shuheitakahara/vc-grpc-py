from route_pb2 import *
from route_pb2_grpc import VCGatewayStub

import grpc
import numpy as np
import sounddevice as sd
import time


def callback(indata, outdata, frames, time, status):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = VCGatewayStub(channel)
        response = stub.VoiceChange(VCRequest(
            config=VCConfig(
                api_key='testapikey',
            ),
            audio_content=indata.tobytes(),
        ))
        resdata = np.frombuffer(response.audio_content, dtype=np.float32)
        resdata = resdata.reshape(resdata.shape[0], 1)
        outdata[:] = resdata


def main():
    try:
        with sd.Stream(channels=1, callback=callback, latency=0.1, samplerate=48000):
            input()
    except KeyboardInterrupt:
        exit(1)


if __name__ == '__main__':
    main()
