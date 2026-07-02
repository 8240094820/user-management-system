from enum import Enum
# define Enums
class SortOrder(str, Enum):
    ASC = "asc"
    DESC = "desc"

class SortColumn(str, Enum):
    NAME = "Name"
    EMAIL = "Email"
    ROLE = "Role"
    STATUS = "Status"


class DocSortColumn(str, Enum):
    FILE_NAME = "original_file_name"
    EXT = "ext"
    PAGE_NO = "page_no"
    WHO_UPLOADED = "who_uploaded"
    WHEN_UPLOADED = "created_date"


class ChatSortColummn(str, Enum):
    ID = "id"
    DATE = "date"

class DocClassification(str, Enum):
    FILE_NAME = "original_file_name"
    CATEGORY = "category"
    WHO_UPLOADED = "uploaded_by"
    WHEN_UPLOADED = "uploaded_at"
    EXT = "file_extension"


class LocationName(str, Enum):
    CHENNAI = "chennai"
    BANGALORE = "bangalore"
    MUMBAI = "mumbai"
    DELHI = "delhi"