# coding: utf-8
from coreapi.codecs import CoreJSONCodec, HTMLCodec, PlainTextCodec, PythonCodec
from coreapi.document import Array, Document, Link, Object, Error, required
from coreapi.document import dotted_path_to_list
from coreapi.exceptions import ParseError, TransportError, ErrorMessage
from coreapi.sessions import DefaultSession


__version__ = '1.1.0'
__all__ = [
    'CoreJSONCodec', 'HTMLCodec', 'PlainTextCodec', 'PythonCodec',
    'negotiate_encoder', 'negotiate_decoder',
    'Array', 'Document', 'Link', 'Object', 'Error', 'required',
    'dotted_path_to_list',
    'ParseError', 'NotAcceptable', 'TransportError', 'ErrorMessage',
    'HTTPTransport',
    'load', 'dump', 'get'
]


def negotiate_encoder(accept=None):
    session = DefaultSession()
    return session.negotiate_encoder(accept)


def negotiate_decoder(content_type=None):
    session = DefaultSession()
    return session.negotiate_decoder(content_type)


def get(url):
    session = DefaultSession()
    return session.transition(url, 'get')


def load(bytestring, content_type=None):
    session = DefaultSession()
    codec = session.negotiate_decoder(content_type)
    return codec.load(bytestring)


def dump(document, accept=None, **kwargs):
    session = DefaultSession()
    codec = session.negotiate_encoder(accept)
    content = codec.dump(document, **kwargs)
    return codec.media_type, content
