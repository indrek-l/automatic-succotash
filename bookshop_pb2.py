# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bookshop.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x62ookshop.proto\"\x14\n\x12\x43reateChainRequest\"\x15\n\x13\x43reateChainResponse\"S\n\x18\x41\x64\x64ProcessToChainRequest\x12\x0f\n\x07process\x18\x01 \x01(\t\x12\x13\n\x0bpredecessor\x18\x02 \x01(\t\x12\x11\n\tsuccessor\x18\x03 \x01(\t\"\x1b\n\x19\x41\x64\x64ProcessToChainResponse\"\x12\n\x10ListChainRequest\"\x13\n\x11ListChainResponse\"=\n\x0cWriteRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x02\"\x0f\n\rWriteResponse\"-\n\x0bReadRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\x02\"0\n\x0cReadResponse\x12\r\n\x05value\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\x02\"/\n\x16\x43reateProcessesRequest\x12\x15\n\rnum_processes\x18\x01 \x01(\x05\"\x19\n\x17\x43reateProcessesResponse\"\x18\n\x16GetProcessNamesRequest\"0\n\x17GetProcessNamesResponse\x12\x15\n\rprocess_names\x18\x01 \x03(\t\"\x12\n\x10ListBooksRequest\"\x13\n\x11ListBooksResponse\"\x13\n\x11SetTimeoutRequest\"\x14\n\x12SetTimeoutResponse\"\x13\n\x11\x44\x61taStatusRequest\"\x14\n\x12\x44\x61taStatusResponse\"\x13\n\x11RemoveHeadRequest\"\x14\n\x12RemoveHeadResponse\"\x14\n\x12RestoreHeadRequest\"\x15\n\x13RestoreHeadResponse2\xd5\x05\n\x08\x42ookshop\x12;\n\x0c\x63reate_chain\x12\x13.CreateChainRequest\x1a\x14.CreateChainResponse\"\x00\x12O\n\x14\x61\x64\x64_process_to_chain\x12\x19.AddProcessToChainRequest\x1a\x1a.AddProcessToChainResponse\"\x00\x12\x35\n\nlist_chain\x12\x11.ListChainRequest\x1a\x12.ListChainResponse\"\x00\x12(\n\x05write\x12\r.WriteRequest\x1a\x0e.WriteResponse\"\x00\x12%\n\x04read\x12\x0c.ReadRequest\x1a\r.ReadResponse\"\x00\x12G\n\x10\x63reate_processes\x12\x17.CreateProcessesRequest\x1a\x18.CreateProcessesResponse\"\x00\x12H\n\x11get_process_names\x12\x17.GetProcessNamesRequest\x1a\x18.GetProcessNamesResponse\"\x00\x12\x35\n\nlist_books\x12\x11.ListBooksRequest\x1a\x12.ListBooksResponse\"\x00\x12\x38\n\x0bset_timeout\x12\x12.SetTimeoutRequest\x1a\x13.SetTimeoutResponse\"\x00\x12\x38\n\x0b\x64\x61ta_status\x12\x12.DataStatusRequest\x1a\x13.DataStatusResponse\"\x00\x12\x38\n\x0bremove_head\x12\x12.RemoveHeadRequest\x1a\x13.RemoveHeadResponse\"\x00\x12;\n\x0crestore_head\x12\x13.RestoreHeadRequest\x1a\x14.RestoreHeadResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bookshop_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CREATECHAINREQUEST._serialized_start=18
  _CREATECHAINREQUEST._serialized_end=38
  _CREATECHAINRESPONSE._serialized_start=40
  _CREATECHAINRESPONSE._serialized_end=61
  _ADDPROCESSTOCHAINREQUEST._serialized_start=63
  _ADDPROCESSTOCHAINREQUEST._serialized_end=146
  _ADDPROCESSTOCHAINRESPONSE._serialized_start=148
  _ADDPROCESSTOCHAINRESPONSE._serialized_end=175
  _LISTCHAINREQUEST._serialized_start=177
  _LISTCHAINREQUEST._serialized_end=195
  _LISTCHAINRESPONSE._serialized_start=197
  _LISTCHAINRESPONSE._serialized_end=216
  _WRITEREQUEST._serialized_start=218
  _WRITEREQUEST._serialized_end=279
  _WRITERESPONSE._serialized_start=281
  _WRITERESPONSE._serialized_end=296
  _READREQUEST._serialized_start=298
  _READREQUEST._serialized_end=343
  _READRESPONSE._serialized_start=345
  _READRESPONSE._serialized_end=393
  _CREATEPROCESSESREQUEST._serialized_start=395
  _CREATEPROCESSESREQUEST._serialized_end=442
  _CREATEPROCESSESRESPONSE._serialized_start=444
  _CREATEPROCESSESRESPONSE._serialized_end=469
  _GETPROCESSNAMESREQUEST._serialized_start=471
  _GETPROCESSNAMESREQUEST._serialized_end=495
  _GETPROCESSNAMESRESPONSE._serialized_start=497
  _GETPROCESSNAMESRESPONSE._serialized_end=545
  _LISTBOOKSREQUEST._serialized_start=547
  _LISTBOOKSREQUEST._serialized_end=565
  _LISTBOOKSRESPONSE._serialized_start=567
  _LISTBOOKSRESPONSE._serialized_end=586
  _SETTIMEOUTREQUEST._serialized_start=588
  _SETTIMEOUTREQUEST._serialized_end=607
  _SETTIMEOUTRESPONSE._serialized_start=609
  _SETTIMEOUTRESPONSE._serialized_end=629
  _DATASTATUSREQUEST._serialized_start=631
  _DATASTATUSREQUEST._serialized_end=650
  _DATASTATUSRESPONSE._serialized_start=652
  _DATASTATUSRESPONSE._serialized_end=672
  _REMOVEHEADREQUEST._serialized_start=674
  _REMOVEHEADREQUEST._serialized_end=693
  _REMOVEHEADRESPONSE._serialized_start=695
  _REMOVEHEADRESPONSE._serialized_end=715
  _RESTOREHEADREQUEST._serialized_start=717
  _RESTOREHEADREQUEST._serialized_end=737
  _RESTOREHEADRESPONSE._serialized_start=739
  _RESTOREHEADRESPONSE._serialized_end=760
  _BOOKSHOP._serialized_start=763
  _BOOKSHOP._serialized_end=1488
# @@protoc_insertion_point(module_scope)
