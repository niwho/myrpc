# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: FangJing.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='FangJing.proto',
  package='',
  serialized_pb='\n\x0e\x46\x61ngJing.proto\"\xbe\x01\n\x08\x46\x61ngJing\x12\n\n\x02ip\x18\t \x02(\t\x12\x17\n\x0f\x63pu_logic_cores\x18\x06 \x02(\x02\x12\x15\n\rcpu_userd_per\x18\x01 \x02(\x02\x12\x11\n\tmem_total\x18\x08 \x02(\x04\x12\x15\n\rmem_userd_per\x18\x02 \x02(\x02\x12\x0e\n\x06net_up\x18\x03 \x02(\x02\x12\x10\n\x08net_down\x18\x04 \x02(\x02\x12\x13\n\x0b\x64isk_totoal\x18\x07 \x02(\x04\x12\x15\n\rdisk_used_per\x18\x05 \x02(\x02')




_FANGJING = _descriptor.Descriptor(
  name='FangJing',
  full_name='FangJing',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip', full_name='FangJing.ip', index=0,
      number=9, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cpu_logic_cores', full_name='FangJing.cpu_logic_cores', index=1,
      number=6, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cpu_userd_per', full_name='FangJing.cpu_userd_per', index=2,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mem_total', full_name='FangJing.mem_total', index=3,
      number=8, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mem_userd_per', full_name='FangJing.mem_userd_per', index=4,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='net_up', full_name='FangJing.net_up', index=5,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='net_down', full_name='FangJing.net_down', index=6,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='disk_totoal', full_name='FangJing.disk_totoal', index=7,
      number=7, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='disk_used_per', full_name='FangJing.disk_used_per', index=8,
      number=5, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=19,
  serialized_end=209,
)

DESCRIPTOR.message_types_by_name['FangJing'] = _FANGJING

class FangJing(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FANGJING

  # @@protoc_insertion_point(class_scope:FangJing)


# @@protoc_insertion_point(module_scope)
