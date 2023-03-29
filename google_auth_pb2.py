# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google_auth.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
  b'\n\x11google_auth.proto\x12\ngoogleauth\"\xd8\x03\n\x10MigrationPayload'\
  b'\x12\x42\n\x0eotp_parameters\x18\x01 \x03(\x0b\x32*.googleauth.MigrationPayload.OtpParameters'\
  b'\x12\x0f\n\x07version\x18\x02 \x01(\x05\x12\x12\n\nbatch_size\x18\x03 \x01'\
  b'(\x05\x12\x13\n\x0b\x62\x61tch_index\x18\x04 \x01(\x05\x12\x10\n\x08\x62\x61'\
  b'tch_id\x18\x05 \x01(\x05\x1a\xcd\x01\n\rOtpParameters\x12\x0e\n\x06'\
  b'secret\x18\x01 \x01(\x0c\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06'\
  b'issuer\x18\x03 \x01(\t\x12\x39\n\talgorithm\x18\x04 \x01'\
  b'(\x0e\x32&.googleauth.MigrationPayload.Algorithm\x12\x0e\n\x06\x64'\
  b'igits\x18\x05 \x01(\x05\x12\x32\n\x04type\x18\x06 \x01(\x0e\x32$.googleauth.MigrationPayload.OtpType'\
  b'\x12\x0f\n\x07\x63ounter\x18\x07 \x01(\x03\",\n\tAlgorithm\x12\x10\n\x0c\x41'\
  b'LGO_INVALID\x10\x00\x12\r\n\tALGO_SHA1\x10\x01\"6\n\x07OtpType\x12\x0f\n\x0b'\
  b'OTP_INVALID\x10\x00\x12\x0c\n\x08OTP_HOTP\x10\x01\x12\x0c\n\x08OTP_TOTP\x10\x02\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google_auth_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MIGRATIONPAYLOAD._serialized_start=34
  _MIGRATIONPAYLOAD._serialized_end=506
  _MIGRATIONPAYLOAD_OTPPARAMETERS._serialized_start=199
  _MIGRATIONPAYLOAD_OTPPARAMETERS._serialized_end=404
  _MIGRATIONPAYLOAD_ALGORITHM._serialized_start=406
  _MIGRATIONPAYLOAD_ALGORITHM._serialized_end=450
  _MIGRATIONPAYLOAD_OTPTYPE._serialized_start=452
  _MIGRATIONPAYLOAD_OTPTYPE._serialized_end=506
# @@protoc_insertion_point(module_scope)
