from __future__ import annotations

from typing import TYPE_CHECKING, Any, Callable

if TYPE_CHECKING:
    from dataframe_api.typing import SupportsDataFrameAPI

some_array_function: Callable[[Any], Any]


def main(df_raw: SupportsDataFrameAPI) -> SupportsDataFrameAPI:
    df = df_raw.__dataframe_consortium_standard__(api_version="2023-11.beta").persist()
    ns = df.__dataframe_namespace__()
    df = df.select(
        *[
            col_name
            for col_name in df.column_names
            if isinstance(df.col(col_name).dtype, ns.Int64)
        ],
    )
    arr = df.to_array(ns.Int64())
    arr = some_array_function(arr)
    df = ns.dataframe_from_2d_array(
        arr,
        schema={"a": df.col("a").dtype, "b": ns.Float64()},
    )
    return df.dataframe
