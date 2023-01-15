from typing import TypeVar, Generic, Sequence, Optional

from fastapi import Query
from pydantic.generics import GenericModel

T = TypeVar('T')


def page_params(
    page: int = Query(1, ge=1, description="Page number"),
    size: int = Query(20, ge=1, le=100, description="Page size")
):
    return {'page': page, 'size': size}


class Page(GenericModel, Generic[T]):
    page: int = Query(description="Page number")
    size: int = Query(description="Page size")
    total: Optional[int] = Query(None)
    items: Sequence[T]

    @classmethod
    def create(
        cls,
        items: Sequence[T],
        params,
        total: Optional[int] = None,
    ) -> 'Page[T]':
        return cls(
            total=total,
            items=list(items),
            page=params['page'],
            size=params['size'],
        )
