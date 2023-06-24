from __future__ import annotations

from typing import Any, Literal, Mapping, Sequence, Union, TYPE_CHECKING, NoReturn, TypeVar, Generic


if TYPE_CHECKING:
    from .column_object import Column
    from .groupby_object import GroupBy
    from . import DType, IntDType, FloatDType, Bool, null, Scalar


__all__ = ["DataFrame"]

T = TypeVar("T", bound="DType")


class DataFrame(Generic[T]):
    """
    DataFrame object

    Note that this dataframe object is not meant to be instantiated directly by
    users of the library implementing the dataframe API standard. Rather, use
    constructor functions or an already-created dataframe object retrieved via
    
    **Python operator support**

    All arithmetic operators defined by the Python language, except for
    ``__matmul__``, ``__neg__`` and ``__pos__``, must be supported for
    numerical data types.

    All comparison operators defined by the Python language must be supported
    by the dataframe object for all data types for which those comparisons are
    supported by the builtin scalar types corresponding to a data type.

    In-place operators must not be supported. All operations on the dataframe
    object are out-of-place.

    **Methods and Attributes**

    """
    def __dataframe_namespace__(
        self, /, *, api_version: str | None = None
    ) -> Any:
        """
        Returns an object that has all the dataframe API functions on it.

        Parameters
        ----------
        api_version: Optional[str]
            String representing the version of the dataframe API specification
            to be returned, in ``'YYYY.MM'`` form, for example, ``'2023.04'``.
            If it is ``None``, it should return the namespace corresponding to
            latest version of the dataframe API specification.  If the given
            version is invalid or not implemented for the given module, an
            error should be raised. Default: ``None``.

        Returns
        -------
        namespace: Any
            An object representing the dataframe API namespace. It should have
            every top-level function defined in the specification as an
            attribute. It may contain other public names as well, but it is
            recommended to only include those names that are part of the
            specification.

        """

    @property
    def dataframe(self) -> object:
        """
        Return underlying (not-necessarily-Standard-compliant) DataFrame.

        If a library only implements the Standard, then this can return `self`.
        """
        ...
    
    def shape(self) -> tuple[int, int]:
        """
        Return number of rows and number of columns.
        """

    def groupby(self, keys: Sequence[str], /) -> GroupBy:
        """
        Group the DataFrame by the given columns.

        Parameters
        ----------
        keys : Sequence[str]

        Returns
        -------
        GroupBy

        Raises
        ------
        KeyError
            If any of the requested keys are not present.

        Notes
        -----
        Downstream operations from this function, like aggregations, return
        results for which row order is not guaranteed and is implementation
        defined.
        """
        ...

    def get_column_by_name(self, name: str, /) -> Column[T]:
        """
        Select a column by name.

        Parameters
        ----------
        name : str

        Returns
        -------
        Column

        Raises
        ------
        KeyError
            If the key is not present.
        """
        ...

    def get_columns_by_name(self, names: Sequence[str], /) -> DataFrame[T]:
        """
        Select multiple columns by name.

        Parameters
        ----------
        names : Sequence[str]

        Returns
        -------
        DataFrame

        Raises
        ------
        KeyError
            If the any requested key is not present.
        """
        ...

    def get_rows(self, indices: Column[IntDType]) -> DataFrame[T]:
        """
        Select a subset of rows, similar to `ndarray.take`.

        Parameters
        ----------
        indices : Column[IntDType]
            Positions of rows to select.

        Returns
        -------
        DataFrame
        """
        ...

    def slice_rows(
        self, start: int | None, stop: int | None, step: int | None
    ) -> DataFrame[T]:
        """
        Select a subset of rows corresponding to a slice.

        Parameters
        ----------
        start : int or None
        stop : int or None
        step : int or None

        Returns
        -------
        DataFrame
        """
        ...

    def get_rows_by_mask(self, mask: Column[Bool]) -> DataFrame[T]:
        """
        Select a subset of rows corresponding to a mask.

        Parameters
        ----------
        mask : Column[bool]

        Returns
        -------
        DataFrame

        Notes
        -----
        Some participants preferred a weaker type Arraylike[bool] for mask,
        where 'Arraylike' denotes an object adhering to the Array API standard.
        """
        ...

    def insert(self, loc: int, label: str, value: Column[Any]) -> DataFrame[Any]:
        """
        Insert column into DataFrame at specified location.

        Parameters
        ----------
        loc : int
            Insertion index. Must verify 0 <= loc <= len(columns).
        label : str
            Label of the inserted column.
        value : Column
        """
        ...

    def drop_column(self, label: str) -> DataFrame[T]:
        """
        Drop the specified column.

        Parameters
        ----------
        label : str

        Returns
        -------
        DataFrame

        Raises
        ------
        KeyError
            If the label is not present.
        """
        ...

    def rename_columns(self, mapping: Mapping[str, str]) -> DataFrame[T]:
        """
        Rename columns.

        Parameters
        ----------
        mapping : Mapping[str, str]
            Keys are old column names, values are new column names.

        Returns
        -------
        DataFrame
        """
        ...

    def get_column_names(self) -> Sequence[str]:
        """
        Get column names.

        Returns
        -------
        Sequence[str]
        """
        ...

    def sorted_indices(
        self,
        keys: Sequence[str],
        *,
        ascending: Sequence[bool] | bool = True,
        nulls_position: Literal['first', 'last'] = 'last',
    ) -> Column[IntDType]:
        """
        Return row numbers which would sort according to given columns.

        If you need to sort the DataFrame, you can simply do::

            df.get_rows(df.sorted_indices(keys))

        Parameters
        ----------
        keys : Sequence[str]
            Names of columns to sort by.
        ascending : Sequence[bool] or bool
            If `True`, sort by all keys in ascending order.
            If `False`, sort by all keys in descending order.
            If a sequence, it must be the same length as `keys`,
            and determines the direction with which to use each
            key to sort by.
        nulls_position : ``{'first', 'last'}``
            Whether null values should be placed at the beginning
            or at the end of the result.
            Note that the position of NaNs is unspecified and may
            vary based on the implementation.

        Returns
        -------
        Column[IntDType]
    
        Raises
        ------
        ValueError
            If `keys` and `ascending` are sequences of different lengths.
        """
        ...

    def __eq__(self, other: DataFrame[Any] | Scalar[Any]) -> DataFrame[Bool]:  # type: ignore[override]
        """
        Compare for equality.

        Nulls should follow Kleene Logic.

        Parameters
        ----------
        other : DataFrame or Scalar
            If DataFrame, must have same length and matching columns.
            "Scalar" here is defined implicitly by what scalar types are allowed
            for the operation by the underling dtypes.

        Returns
        -------
        DataFrame
        """
        ...

    def __ne__(self, other: DataFrame[Any] | Scalar[Any]) -> DataFrame[Bool]:  # type: ignore[override]
        """
        Compare for non-equality.

        Nulls should follow Kleene Logic.

        Parameters
        ----------
        other : DataFrame or Scalar
            If DataFrame, must have same length and matching columns.
            "Scalar" here is defined implicitly by what scalar types are allowed
            for the operation by the underling dtypes.

        Returns
        -------
        DataFrame
        """
        ...

    def __ge__(self, other: DataFrame[Any] | Scalar[Any]) -> DataFrame[Bool]:
        """
        Compare for "greater than or equal to" `other`.

        Parameters
        ----------
        other : DataFrame or Scalar
            If DataFrame, must have same length and matching columns.
            "Scalar" here is defined implicitly by what scalar types are allowed
            for the operation by the underling dtypes.

        Returns
        -------
        DataFrame
        """
        ...

    def __gt__(self, other: DataFrame[Any] | Scalar[Any]) -> DataFrame[Bool]:
        """
        Compare for "greater than" `other`.

        Parameters
        ----------
        other : DataFrame or Scalar
            If DataFrame, must have same length and matching columns.
            "Scalar" here is defined implicitly by what scalar types are allowed
            for the operation by the underling dtypes.

        Returns
        -------
        DataFrame
        """
        ...

    def __le__(self, other: DataFrame[Any] | Scalar[Any]) -> DataFrame[Bool]:
        """
        Compare for "less than or equal to" `other`.

        Parameters
        ----------
        other : DataFrame or Scalar
            If DataFrame, must have same length and matching columns.
            "Scalar" here is defined implicitly by what scalar types are allowed
            for the operation by the underling dtypes.

        Returns
        -------
        DataFrame
        """
        ...

    def __lt__(self, other: DataFrame[Any] | Scalar[Any]) -> DataFrame[Bool]:
        """
        Compare for "less than" `other`.

        Parameters
        ----------
        other : DataFrame or Scalar
            If DataFrame, must have same length and matching columns.
            "Scalar" here is defined implicitly by what scalar types are allowed
            for the operation by the underling dtypes.

        Returns
        -------
        DataFrame
        """
        ...

    def __and__(self, other: DataFrame[Bool] | bool) -> DataFrame[Bool]:
        """
        Apply logical 'and' to `other` DataFrame (or scalar) and this dataframe.

        Nulls should follow Kleene Logic.

        Parameters
        ----------
        other : DataFrame[bool] or bool
            If DataFrame, must have same length.

        Returns
        -------
        DataFrame[bool]

        Raises
        ------
        ValueError
            If `self` or `other` is not boolean.
        """

    def __or__(self, other: DataFrame[Bool] | bool) -> DataFrame[Bool]:
        """
        Apply logical 'or' to `other` DataFrame (or scalar) and this DataFrame.

        Nulls should follow Kleene Logic.

        Parameters
        ----------
        other : DataFrame[bool] or bool
            If DataFrame, must have same length.

        Returns
        -------
        DataFrame[bool]

        Raises
        ------
        ValueError
            If `self` or `other` is not boolean.
        """

    def __add__(self, other: DataFrame[Any] | Scalar[Any]) -> DataFrame[Any]:
        """
        Add `other` dataframe or scalar to this dataframe.

        Parameters
        ----------
        other : DataFrame or Scalar
            If DataFrame, must have same length and matching columns.
            "Scalar" here is defined implicitly by what scalar types are allowed
            for the operation by the underling dtypes.

        Returns
        -------
        DataFrame
        """
        ...

    def __sub__(self, other: DataFrame[Any] | Scalar[Any]) -> DataFrame[Any]:
        """
        Subtract `other` dataframe or scalar from this dataframe.

        Parameters
        ----------
        other : DataFrame or Scalar
            If DataFrame, must have same length and matching columns.
            "Scalar" here is defined implicitly by what scalar types are allowed
            for the operation by the underling dtypes.

        Returns
        -------
        DataFrame
        """
        ...

    def __mul__(self, other: DataFrame[Any] | Scalar[Any]) -> DataFrame[Any]:
        """
        Multiply  `other` dataframe or scalar with this dataframe.

        Parameters
        ----------
        other : DataFrame or Scalar
            If DataFrame, must have same length and matching columns.
            "Scalar" here is defined implicitly by what scalar types are allowed
            for the operation by the underling dtypes.

        Returns
        -------
        DataFrame
        """
        ...

    def __truediv__(self, other: DataFrame[Any] | Scalar[Any]) -> DataFrame[Any]:
        """
        Divide  this dataframe by `other` dataframe or scalar. True division, returns floats.

        Parameters
        ----------
        other : DataFrame or Scalar
            If DataFrame, must have same length and matching columns.
            "Scalar" here is defined implicitly by what scalar types are allowed
            for the operation by the underling dtypes.

        Returns
        -------
        DataFrame
        """
        ...

    def __floordiv__(self, other: DataFrame[Any] | Scalar[Any]) -> DataFrame[Any]:
        """
        Floor-divide (returns integers) this dataframe by `other` dataframe or scalar.

        Parameters
        ----------
        other : DataFrame or Scalar
            If DataFrame, must have same length and matching columns.
            "Scalar" here is defined implicitly by what scalar types are allowed
            for the operation by the underling dtypes.

        Returns
        -------
        DataFrame
        """
        ...

    def __pow__(self, other: DataFrame[Any] | Scalar[Any]) -> DataFrame[Any]:
        """
        Raise this dataframe to the power of `other`.

        Parameters
        ----------
        other : DataFrame or Scalar
            If DataFrame, must have same length and matching columns.
            "Scalar" here is defined implicitly by what scalar types are allowed
            for the operation by the underling dtypes.

        Returns
        -------
        DataFrame
        """
        ...

    def __mod__(self, other: DataFrame[Any] | Scalar[Any]) -> DataFrame[Any]:
        """
        Return modulus of this dataframe by `other` (`%` operator).

        Parameters
        ----------
        other : DataFrame or Scalar
            If DataFrame, must have same length and matching columns.
            "Scalar" here is defined implicitly by what scalar types are allowed
            for the operation by the underling dtypes.

        Returns
        -------
        DataFrame
        """
        ...

    def __divmod__(self, other: DataFrame[Any] | Scalar[Any]) -> tuple[DataFrame[Any], DataFrame[Any]]:
        """
        Return quotient and remainder of integer division. See `divmod` builtin function.

        Parameters
        ----------
        other : DataFrame or Scalar
            If DataFrame, must have same length and matching columns.
            "Scalar" here is defined implicitly by what scalar types are allowed
            for the operation by the underling dtypes.

        Returns
        -------
        A tuple of two DataFrame's
        """
        ...

    def __invert__(self: DataFrame[Bool]) -> DataFrame[Bool]:
        """
        Invert truthiness of (boolean) elements.

        Raises
        ------
        ValueError
            If any of the DataFrame's columns is not boolean.
        """
        ...

    def __iter__(self) -> NoReturn:
        """
        Iterate over elements.

        This is intentionally "poisoned" to discourage inefficient code patterns.

        Raises
        ------
        NotImplementedError
        """
        raise NotImplementedError("'__iter__' is intentionally not implemented.")

    def any(self, *, skip_nulls: bool = True) -> DataFrame[Bool]:
        """
        Reduction returns a 1-row DataFrame.

        Raises
        ------
        ValueError
            If any of the DataFrame's columns is not boolean.
        """
        ...

    def all(self, *, skip_nulls: bool = True) -> DataFrame[Bool]:
        """
        Reduction returns a 1-row DataFrame.

        Raises
        ------
        ValueError
            If any of the DataFrame's columns is not boolean.
        """
        ...
    
    def any_rowwise(self, *, skip_nulls: bool = True) -> Column[Bool]:
        """
        Reduction returns a Column.

        Differs from ``DataFrame.any`` and that the reduction happens
        for each row, rather than for each column.

        Raises
        ------
        ValueError
            If any of the DataFrame's columns is not boolean.
        """
        ...

    def all_rowwise(self, *, skip_nulls: bool = True) -> Column[Bool]:
        """
        Reduction returns a Column.

        Differs from ``DataFrame.all`` and that the reduction happens
        for each row, rather than for each column.

        Raises
        ------
        ValueError
            If any of the DataFrame's columns is not boolean.
        """
        ...

    def min(self, *, skip_nulls: bool = True) -> DataFrame[T]:
        """
        Reduction returns a 1-row DataFrame.
        """
        ...

    def max(self, *, skip_nulls: bool = True) -> DataFrame[T]:
        """
        Reduction returns a 1-row DataFrame.
        """
        ...

    def sum(self, *, skip_nulls: bool = True) -> DataFrame[Any]:
        """
        Reduction returns a 1-row DataFrame.
        """
        ...

    def prod(self, *, skip_nulls: bool = True) -> DataFrame[Any]:
        """
        Reduction returns a 1-row DataFrame.
        """
        ...

    def median(self, *, skip_nulls: bool = True) -> DataFrame[Any]:
        """
        Reduction returns a 1-row DataFrame.
        """
        ...

    def mean(self, *, skip_nulls: bool = True) -> DataFrame[Any]:
        """
        Reduction returns a 1-row DataFrame.
        """
        ...

    def std(self, *, skip_nulls: bool = True) -> DataFrame[Any]:
        """
        Reduction returns a 1-row DataFrame.
        """
        ...

    def var(self, *, skip_nulls: bool = True) -> DataFrame[Any]:
        """
        Reduction returns a 1-row DataFrame.
        """
        ...

    def is_null(self) -> DataFrame[Bool]:
        """
        Check for 'missing' or 'null' entries.

        Returns
        -------
        DataFrame

        See also
        --------
        is_nan

        Notes
        -----
        Does *not* include NaN-like entries.
        May optionally include 'NaT' values (if present in an implementation),
        but note that the Standard makes no guarantees about them.
        """
        ...

    def is_nan(self) -> DataFrame[Bool]:
        """
        Check for nan entries.

        Returns
        -------
        DataFrame

        See also
        --------
        is_null

        Notes
        -----
        This only checks for 'NaN'.
        Does *not* include 'missing' or 'null' entries.
        In particular, does not check for `np.timedelta64('NaT')`.
        """
        ...

    def fill_nan(self, value: float | 'null', /) -> DataFrame[T]:
        """
        Fill ``nan`` values with the given fill value.

        The fill operation will apply to all columns with a floating-point
        dtype. Other columns remain unchanged.

        Parameters
        ----------
        value : float or `null`
            Value used to replace any ``nan`` in the column with. Must be
            of the Python scalar type matching the dtype of the column (or
            be `null`).

        """
        ...
