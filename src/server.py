from route_pb2 import *
from route_pb2_grpc import add_VCGatewayServicer_to_server, VCGatewayServicer

from concurrent import futures
import grpc
import librosa
import numpy as np
import time


class RouteVCServicer(VCGatewayServicer):
    """
    APIメソッドの実装
    """

    def VoiceChange(self, request_iterator, context):
        audio_byte_array = request_iterator.audio_content
        indata = np.frombuffer(audio_byte_array, dtype=np.float32)
        indata = indata.reshape(indata.shape[0], 1)
        # NOTE: VC処理をここで行う
        outdata = indata
        return VCResponse(
            audio_content=outdata.tobytes(),
            timestamp='sampletimestamp'
        )


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_VCGatewayServicer_to_server(RouteVCServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('Run server.')
    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        print('Stop server.')
        server.stop(0)


if __name__ == '__main__':
    main()
