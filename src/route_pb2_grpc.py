# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from src import route_pb2 as src_dot_route__pb2


class VCGatewayStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StreamingVC = channel.stream_stream(
                '/VCGateway/StreamingVC',
                request_serializer=src_dot_route__pb2.StreamingVCRequest.SerializeToString,
                response_deserializer=src_dot_route__pb2.StreamingVCResponse.FromString,
                )


class VCGatewayServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StreamingVC(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_VCGatewayServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StreamingVC': grpc.stream_stream_rpc_method_handler(
                    servicer.StreamingVC,
                    request_deserializer=src_dot_route__pb2.StreamingVCRequest.FromString,
                    response_serializer=src_dot_route__pb2.StreamingVCResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'VCGateway', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class VCGateway(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def StreamingVC(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/VCGateway/StreamingVC',
            src_dot_route__pb2.StreamingVCRequest.SerializeToString,
            src_dot_route__pb2.StreamingVCResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
