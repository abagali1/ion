# Stubs for bleach.sanitizer (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
import sanitizer

ALLOWED_TAGS = ...  # type: Any
ALLOWED_ATTRIBUTES = ...  # type: Any
ALLOWED_STYLES = ...  # type: Any
ALLOWED_PROTOCOLS = ...  # type: Any

class Cleaner:
    tags = ...  # type: Any
    attributes = ...  # type: Any
    styles = ...  # type: Any
    protocols = ...  # type: Any
    strip = ...  # type: Any
    strip_comments = ...  # type: Any
    filters = ...  # type: Any
    parser = ...  # type: Any
    walker = ...  # type: Any
    serializer = ...  # type: Any
    def __init__(self, tags: Any = ..., attributes: Any = ..., styles: Any = ..., protocols: Any = ..., strip: bool = ..., strip_comments: bool = ..., filters: Optional[Any] = ...) -> None: ...
    def clean(self, text): ...

def attribute_filter_factory(attributes): ...

class BleachSanitizerFilter(sanitizer.Filter):
    attr_filter = ...  # type: Any
    strip_disallowed_elements = ...  # type: Any
    strip_html_comments = ...  # type: Any
    def __init__(self, source, attributes: Any = ..., strip_disallowed_elements: bool = ..., strip_html_comments: bool = ..., **kwargs) -> None: ...
    def sanitize_token(self, token): ...
    def allow_token(self, token): ...
    def sanitize_css(self, style): ...
