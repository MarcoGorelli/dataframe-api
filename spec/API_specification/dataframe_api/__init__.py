"""
Function stubs and API documentation for the DataFrame API standard.
"""
from __future__ import annotations

from typing import Mapping, Sequence, Any, Literal

from .column_object import *
from .dataframe_object import DataFrame
from .groupby_object import *
from ._types import DType

__all__ = [
    "__dataframe_api_version__",
    "DataFrame",
    "Column",
    "column_from_sequence",
    "concat",
    "dataframe_from_dict",
    "is_null",
    "null",
    "Int64",
    "Int32",
    "Int16",
    "Int8",
    "UInt64",
    "UInt32",
    "UInt16",
    "UInt8",
    "Float64",
    "Float32",
    "Bool",
    "Datetime",
    "Duration",
    "String",
]


__dataframe_api_version__: str = "YYYY.MM"
"""
String representing the version of the DataFrame API specification to which
the conforming implementation adheres. Set to a concrete value for a stable
implementation of the dataframe API standard.
"""

def concat(dataframes: Sequence[DataFrame]) -> DataFrame:
    """
    Concatenate DataFrames vertically.

    To concatenate horizontally, please use ``insert``.

    Parameters
    ----------
    dataframes : Sequence[DataFrame]
        DataFrames to concatenate.
        Column names, ordering, and dtypes must match.

    Notes
    -----
    The order in which the input DataFrames appear in
    the output is preserved (so long as the DataFrame implementation supports row
    ordering).
    """
    ...

def column_from_sequence(sequence: Sequence[Any], *, dtype: Any) -> Column[Any]:
    """
    Construct Column from sequence of elements.

    Parameters
    ----------
    sequence : Sequence[object]
        Sequence of elements. Each element must be of the specified
        ``dtype``, the corresponding Python builtin scalar type, or
        coercible to that Python scalar type.
    dtype : DType
        Dtype of result. Must be specified.

    Returns
    -------
    Column
    """
    ...

def dataframe_from_dict(data: Mapping[str, Column[Any]]) -> DataFrame:
    """
    Construct DataFrame from map of column names to Columns.

    Parameters
    ----------
    data : Mapping[str, Column]
        Column must be of the corresponding type of the DataFrame.
        For example, it is only supported to build a ``LibraryXDataFrame`` using
        ``LibraryXColumn`` instances.

    Returns
    -------
    DataFrame
    """
    ...

class null:
    """
    A `null` object to represent missing data.

    ``null`` is a scalar, and may be used when constructing a `Column` from a
    Python sequence with `column_from_sequence`. It does not support ``is``,
    ``==`` or ``bool``.

    Raises
    ------
    TypeError
        From ``__eq__`` and from ``__bool__``.

        For ``__eq__``: a missing value must not be compared for equality
        directly. Instead, use `DataFrame.is_null` or `Column.is_null` to check
        for presence of missing values.

        For ``__bool__``: truthiness of a missing value is ambiguous.

    Notes
    -----
    Like for Python scalars, the ``null`` object may be duck typed so it can
    reside on (e.g.) a GPU. Hence, the builtin ``is`` keyword should not be
    used to check if an object *is* the ``null`` object.

    """
    ...

def is_null(value: object, /) -> bool:
    """
    Check if an object is a `null` scalar.

    Parameters
    ----------
    value : object
        Any input type is valid.

    Returns
    -------
    bool
        True if the input is a `null` object from the same library which
        implements the dataframe API standard, False otherwise.

    """

##########
# Dtypes #
##########

class Int64:
    """Integer type with 64 bits of precision."""

class Int32:
    """Integer type with 32 bits of precision."""

class Int16:
    """Integer type with 16 bits of precision."""

class Int8:
    """Integer type with 8 bits of precision."""

class UInt64:
    """Unsigned integer type with 64 bits of precision."""

class UInt32:
    """Unsigned integer type with 32 bits of precision."""

class UInt16:
    """Unsigned integer type with 16 bits of precision."""

class UInt8:
    """Unsigned integer type with 8 bits of precision."""

class Float64:
    """Floating point type with 64 bits of precision."""

class Float32:
    """Floating point type with 32 bits of precision."""

class Bool:
    """Boolean type."""

class Datetime:
    """
    Datetime type.

    Attributes
    ----------
    time_unit : Literal['ms', 'us', 'ns']
        Precision of the datetime type. There is no guarantee that the full
        range of dates available for the specified precision is supported.
    time_zone : str | None
        Time zone of the datetime type. Only IANA time zones are supported.
        `None` indicates time-zone-naive data.
    """
    time_unit: Literal['ms', 'us', 'ns']
    time_zone: str | None  # Only IANA time zones are supported

class Duration:
    """Duration type."""
    time_unit: Literal['ms', 'us', 'ns']

class String:
    """String type."""
