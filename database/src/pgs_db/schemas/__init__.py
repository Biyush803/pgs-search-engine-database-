"""Public Pydantic schemas provided by the pgs-db package."""

from .base import ReadSchema, SchemaBase
from .crawl import (
    CrawledDocumentCreate,
    CrawledDocumentRead,
    CrawledDocumentUpdate,
    CrawlRunCreate,
    CrawlRunRead,
    CrawlRunUpdate,
    StoredFileCreate,
    StoredFileRead,
    StoredFileUpdate,
)
from .domain import DomainCreate, DomainRead, DomainUpdate
from .geography import (
    DistrictCreate,
    DistrictRead,
    DistrictUpdate,
    LocalBodyCreate,
    LocalBodyRead,
    LocalBodyUpdate,
    ProvinceCreate,
    ProvinceRead,
    ProvinceUpdate,
)

__all__ = [
    "CrawledDocumentCreate",
    "CrawledDocumentRead",
    "CrawledDocumentUpdate",
    "CrawlRunCreate",
    "CrawlRunRead",
    "CrawlRunUpdate",
    "DistrictCreate",
    "DistrictRead",
    "DistrictUpdate",
    "DomainCreate",
    "DomainRead",
    "DomainUpdate",
    "LocalBodyCreate",
    "LocalBodyRead",
    "LocalBodyUpdate",
    "ProvinceCreate",
    "ProvinceRead",
    "ProvinceUpdate",
    "ReadSchema",
    "SchemaBase",
    "StoredFileCreate",
    "StoredFileRead",
    "StoredFileUpdate",
]