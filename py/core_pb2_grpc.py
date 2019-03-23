# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import cartesi_base_pb2 as cartesi__base__pb2


class MachineStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Run = channel.unary_unary(
        '/CartesiCore.Machine/Run',
        request_serializer=cartesi__base__pb2.RunRequest.SerializeToString,
        response_deserializer=cartesi__base__pb2.RunResponse.FromString,
        )
    self.Machine = channel.unary_unary(
        '/CartesiCore.Machine/Machine',
        request_serializer=cartesi__base__pb2.MachineRequest.SerializeToString,
        response_deserializer=cartesi__base__pb2.Void.FromString,
        )
    self.Snapshot = channel.unary_unary(
        '/CartesiCore.Machine/Snapshot',
        request_serializer=cartesi__base__pb2.Void.SerializeToString,
        response_deserializer=cartesi__base__pb2.Void.FromString,
        )
    self.Rollback = channel.unary_unary(
        '/CartesiCore.Machine/Rollback',
        request_serializer=cartesi__base__pb2.Void.SerializeToString,
        response_deserializer=cartesi__base__pb2.Void.FromString,
        )
    self.Shutdown = channel.unary_unary(
        '/CartesiCore.Machine/Shutdown',
        request_serializer=cartesi__base__pb2.Void.SerializeToString,
        response_deserializer=cartesi__base__pb2.Void.FromString,
        )
    self.Inc = channel.unary_unary(
        '/CartesiCore.Machine/Inc',
        request_serializer=cartesi__base__pb2.Void.SerializeToString,
        response_deserializer=cartesi__base__pb2.Void.FromString,
        )
    self.Print = channel.unary_unary(
        '/CartesiCore.Machine/Print',
        request_serializer=cartesi__base__pb2.Void.SerializeToString,
        response_deserializer=cartesi__base__pb2.Void.FromString,
        )
    self.Step = channel.unary_unary(
        '/CartesiCore.Machine/Step',
        request_serializer=cartesi__base__pb2.Void.SerializeToString,
        response_deserializer=cartesi__base__pb2.AccessLog.FromString,
        )
    self.GetRootHash = channel.unary_unary(
        '/CartesiCore.Machine/GetRootHash',
        request_serializer=cartesi__base__pb2.Void.SerializeToString,
        response_deserializer=cartesi__base__pb2.Hash.FromString,
        )


class MachineServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Run(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Machine(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Snapshot(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Rollback(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Shutdown(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Inc(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Print(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Step(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetRootHash(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MachineServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Run': grpc.unary_unary_rpc_method_handler(
          servicer.Run,
          request_deserializer=cartesi__base__pb2.RunRequest.FromString,
          response_serializer=cartesi__base__pb2.RunResponse.SerializeToString,
      ),
      'Machine': grpc.unary_unary_rpc_method_handler(
          servicer.Machine,
          request_deserializer=cartesi__base__pb2.MachineRequest.FromString,
          response_serializer=cartesi__base__pb2.Void.SerializeToString,
      ),
      'Snapshot': grpc.unary_unary_rpc_method_handler(
          servicer.Snapshot,
          request_deserializer=cartesi__base__pb2.Void.FromString,
          response_serializer=cartesi__base__pb2.Void.SerializeToString,
      ),
      'Rollback': grpc.unary_unary_rpc_method_handler(
          servicer.Rollback,
          request_deserializer=cartesi__base__pb2.Void.FromString,
          response_serializer=cartesi__base__pb2.Void.SerializeToString,
      ),
      'Shutdown': grpc.unary_unary_rpc_method_handler(
          servicer.Shutdown,
          request_deserializer=cartesi__base__pb2.Void.FromString,
          response_serializer=cartesi__base__pb2.Void.SerializeToString,
      ),
      'Inc': grpc.unary_unary_rpc_method_handler(
          servicer.Inc,
          request_deserializer=cartesi__base__pb2.Void.FromString,
          response_serializer=cartesi__base__pb2.Void.SerializeToString,
      ),
      'Print': grpc.unary_unary_rpc_method_handler(
          servicer.Print,
          request_deserializer=cartesi__base__pb2.Void.FromString,
          response_serializer=cartesi__base__pb2.Void.SerializeToString,
      ),
      'Step': grpc.unary_unary_rpc_method_handler(
          servicer.Step,
          request_deserializer=cartesi__base__pb2.Void.FromString,
          response_serializer=cartesi__base__pb2.AccessLog.SerializeToString,
      ),
      'GetRootHash': grpc.unary_unary_rpc_method_handler(
          servicer.GetRootHash,
          request_deserializer=cartesi__base__pb2.Void.FromString,
          response_serializer=cartesi__base__pb2.Hash.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'CartesiCore.Machine', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
