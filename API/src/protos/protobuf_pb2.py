# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: src/protos/protobuf.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19src/protos/protobuf.proto\"P\n\x07Message\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x11\n\trecipient\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\x12\x11\n\ttimestamp\x18\x04 \x01(\x03\"\x18\n\x07IsValid\x12\r\n\x05valid\x18\x01 \x01(\x08\"\x07\n\x05\x45mpty2P\n\x07Service\x12$\n\x0ePrepareMessage\x12\x08.Message\x1a\x08.IsValid\x12\x1f\n\x0bSendMessage\x12\x08.Message\x1a\x06.Emptyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'src.protos.protobuf_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_MESSAGE']._serialized_start=29
  _globals['_MESSAGE']._serialized_end=109
  _globals['_ISVALID']._serialized_start=111
  _globals['_ISVALID']._serialized_end=135
  _globals['_EMPTY']._serialized_start=137
  _globals['_EMPTY']._serialized_end=144
  _globals['_SERVICE']._serialized_start=146
  _globals['_SERVICE']._serialized_end=226
# @@protoc_insertion_point(module_scope)