# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fingerprint.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='fingerprint.proto',
  package='fingerprint',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11\x66ingerprint.proto\x12\x0b\x66ingerprint\".\n\x0ePreEnrolledFMD\x12\x1c\n\x14\x62\x61se64PreEnrolledFMD\x18\x01 \x01(\t\"(\n\x0b\x45nrolledFMD\x12\x19\n\x11\x62\x61se64EnrolledFMD\x18\x01 \x01(\t\"G\n\x11\x45nrollmentRequest\x12\x32\n\rfmdCandidates\x18\x01 \x03(\x0b\x32\x1b.fingerprint.PreEnrolledFMD\"v\n\x13VerificationRequest\x12.\n\ttargetFMD\x18\x01 \x01(\x0b\x32\x1b.fingerprint.PreEnrolledFMD\x12/\n\rfmdCandidates\x18\x02 \x03(\x0b\x32\x18.fingerprint.EnrolledFMD\"%\n\x14VerificationResponse\x12\r\n\x05match\x18\x01 \x01(\x08\"-\n\x16\x43heckDuplicateResponse\x12\x13\n\x0bisDuplicate\x18\x01 \x01(\x08\x32\x93\x02\n\x0b\x46ingerPrint\x12O\n\x11\x45nrollFingerprint\x12\x1e.fingerprint.EnrollmentRequest\x1a\x18.fingerprint.EnrolledFMD\"\x00\x12Z\n\x11VerifyFingerprint\x12 .fingerprint.VerificationRequest\x1a!.fingerprint.VerificationResponse\"\x00\x12W\n\x0e\x43heckDuplicate\x12 .fingerprint.VerificationRequest\x1a#.fingerprint.CheckDuplicateResponseb\x06proto3'
)




_PREENROLLEDFMD = _descriptor.Descriptor(
  name='PreEnrolledFMD',
  full_name='fingerprint.PreEnrolledFMD',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='base64PreEnrolledFMD', full_name='fingerprint.PreEnrolledFMD.base64PreEnrolledFMD', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=80,
)


_ENROLLEDFMD = _descriptor.Descriptor(
  name='EnrolledFMD',
  full_name='fingerprint.EnrolledFMD',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='base64EnrolledFMD', full_name='fingerprint.EnrolledFMD.base64EnrolledFMD', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=82,
  serialized_end=122,
)


_ENROLLMENTREQUEST = _descriptor.Descriptor(
  name='EnrollmentRequest',
  full_name='fingerprint.EnrollmentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fmdCandidates', full_name='fingerprint.EnrollmentRequest.fmdCandidates', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=124,
  serialized_end=195,
)


_VERIFICATIONREQUEST = _descriptor.Descriptor(
  name='VerificationRequest',
  full_name='fingerprint.VerificationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='targetFMD', full_name='fingerprint.VerificationRequest.targetFMD', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fmdCandidates', full_name='fingerprint.VerificationRequest.fmdCandidates', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=197,
  serialized_end=315,
)


_VERIFICATIONRESPONSE = _descriptor.Descriptor(
  name='VerificationResponse',
  full_name='fingerprint.VerificationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='match', full_name='fingerprint.VerificationResponse.match', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=317,
  serialized_end=354,
)


_CHECKDUPLICATERESPONSE = _descriptor.Descriptor(
  name='CheckDuplicateResponse',
  full_name='fingerprint.CheckDuplicateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='isDuplicate', full_name='fingerprint.CheckDuplicateResponse.isDuplicate', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=356,
  serialized_end=401,
)

_ENROLLMENTREQUEST.fields_by_name['fmdCandidates'].message_type = _PREENROLLEDFMD
_VERIFICATIONREQUEST.fields_by_name['targetFMD'].message_type = _PREENROLLEDFMD
_VERIFICATIONREQUEST.fields_by_name['fmdCandidates'].message_type = _ENROLLEDFMD
DESCRIPTOR.message_types_by_name['PreEnrolledFMD'] = _PREENROLLEDFMD
DESCRIPTOR.message_types_by_name['EnrolledFMD'] = _ENROLLEDFMD
DESCRIPTOR.message_types_by_name['EnrollmentRequest'] = _ENROLLMENTREQUEST
DESCRIPTOR.message_types_by_name['VerificationRequest'] = _VERIFICATIONREQUEST
DESCRIPTOR.message_types_by_name['VerificationResponse'] = _VERIFICATIONRESPONSE
DESCRIPTOR.message_types_by_name['CheckDuplicateResponse'] = _CHECKDUPLICATERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PreEnrolledFMD = _reflection.GeneratedProtocolMessageType('PreEnrolledFMD', (_message.Message,), {
  'DESCRIPTOR' : _PREENROLLEDFMD,
  '__module__' : 'fingerprint_pb2'
  # @@protoc_insertion_point(class_scope:fingerprint.PreEnrolledFMD)
  })
_sym_db.RegisterMessage(PreEnrolledFMD)

EnrolledFMD = _reflection.GeneratedProtocolMessageType('EnrolledFMD', (_message.Message,), {
  'DESCRIPTOR' : _ENROLLEDFMD,
  '__module__' : 'fingerprint_pb2'
  # @@protoc_insertion_point(class_scope:fingerprint.EnrolledFMD)
  })
_sym_db.RegisterMessage(EnrolledFMD)

EnrollmentRequest = _reflection.GeneratedProtocolMessageType('EnrollmentRequest', (_message.Message,), {
  'DESCRIPTOR' : _ENROLLMENTREQUEST,
  '__module__' : 'fingerprint_pb2'
  # @@protoc_insertion_point(class_scope:fingerprint.EnrollmentRequest)
  })
_sym_db.RegisterMessage(EnrollmentRequest)

VerificationRequest = _reflection.GeneratedProtocolMessageType('VerificationRequest', (_message.Message,), {
  'DESCRIPTOR' : _VERIFICATIONREQUEST,
  '__module__' : 'fingerprint_pb2'
  # @@protoc_insertion_point(class_scope:fingerprint.VerificationRequest)
  })
_sym_db.RegisterMessage(VerificationRequest)

VerificationResponse = _reflection.GeneratedProtocolMessageType('VerificationResponse', (_message.Message,), {
  'DESCRIPTOR' : _VERIFICATIONRESPONSE,
  '__module__' : 'fingerprint_pb2'
  # @@protoc_insertion_point(class_scope:fingerprint.VerificationResponse)
  })
_sym_db.RegisterMessage(VerificationResponse)

CheckDuplicateResponse = _reflection.GeneratedProtocolMessageType('CheckDuplicateResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHECKDUPLICATERESPONSE,
  '__module__' : 'fingerprint_pb2'
  # @@protoc_insertion_point(class_scope:fingerprint.CheckDuplicateResponse)
  })
_sym_db.RegisterMessage(CheckDuplicateResponse)



_FINGERPRINT = _descriptor.ServiceDescriptor(
  name='FingerPrint',
  full_name='fingerprint.FingerPrint',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=404,
  serialized_end=679,
  methods=[
  _descriptor.MethodDescriptor(
    name='EnrollFingerprint',
    full_name='fingerprint.FingerPrint.EnrollFingerprint',
    index=0,
    containing_service=None,
    input_type=_ENROLLMENTREQUEST,
    output_type=_ENROLLEDFMD,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='VerifyFingerprint',
    full_name='fingerprint.FingerPrint.VerifyFingerprint',
    index=1,
    containing_service=None,
    input_type=_VERIFICATIONREQUEST,
    output_type=_VERIFICATIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CheckDuplicate',
    full_name='fingerprint.FingerPrint.CheckDuplicate',
    index=2,
    containing_service=None,
    input_type=_VERIFICATIONREQUEST,
    output_type=_CHECKDUPLICATERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_FINGERPRINT)

DESCRIPTOR.services_by_name['FingerPrint'] = _FINGERPRINT

# @@protoc_insertion_point(module_scope)
