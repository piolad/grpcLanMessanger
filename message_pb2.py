# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rmessage.proto\x1a\x1bgoogle/protobuf/empty.proto\"C\n\rSimpleMessage\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\t\"7\n\x0cStateMessage\x12\x16\n\x06status\x18\x01 \x01(\x0e\x32\x06.state\x12\x0f\n\x07message\x18\x02 \x01(\t**\n\x05state\x12\x06\n\x02OK\x10\x00\x12\x0b\n\x07WARNING\x10\x01\x12\x0c\n\x08\x43RITICAL\x10\x02\x32t\n\x0eMessageService\x12,\n\x0bSendMessage\x12\x0e.SimpleMessage\x1a\r.StateMessage\x12\x34\n\x0bHealthCheck\x12\x16.google.protobuf.Empty\x1a\r.StateMessageb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'message_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_STATE']._serialized_start=172
  _globals['_STATE']._serialized_end=214
  _globals['_SIMPLEMESSAGE']._serialized_start=46
  _globals['_SIMPLEMESSAGE']._serialized_end=113
  _globals['_STATEMESSAGE']._serialized_start=115
  _globals['_STATEMESSAGE']._serialized_end=170
  _globals['_MESSAGESERVICE']._serialized_start=216
  _globals['_MESSAGESERVICE']._serialized_end=332
# @@protoc_insertion_point(module_scope)
