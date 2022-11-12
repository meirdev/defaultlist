from typing import Callable, Iterable, SupportsIndex, TypeVar, overload

T = TypeVar("T")


class DefalutList(list[T]):
    def __init__(self, default_factory: Callable[[], T], /, *args, **kwargs) -> None:
        self.__default_factory = default_factory

        super().__init__(*args, **kwargs)

    def __create_default(self, key: slice | SupportsIndex) -> None:
        if isinstance(key, slice):
            start = key.start or 0
            stop = key.stop or 0

            if start < 0:
                start = abs(start)

            if stop < 0:
                stop = abs(stop)

            if key.start is not None and key.start > 0 and key.stop is None:
                start += 1

            end = max(start, stop)
        else:
            key = int(key)

            if key < 0:
                end = abs(key)
            else:
                end = key + 1

        self.extend(self.__default_factory() for _ in range(len(self), end))

    @overload
    def __getitem__(self, key: SupportsIndex, /) -> T:  # pragma: no cover
        ...

    @overload
    def __getitem__(self, key: slice, /) -> list[T]:  # pragma: no cover
        ...

    def __getitem__(self, key: slice | SupportsIndex, /) -> T | list[T]:
        if isinstance(key, (slice, SupportsIndex)):
            self.__create_default(key)

        return super().__getitem__(key)

    @overload
    def __setitem__(self, key: SupportsIndex, value: T, /) -> None:  # pragma: no cover
        ...

    @overload
    def __setitem__(self, key: slice, value: Iterable[T], /) -> None:  # pragma: no cover
        ...

    def __setitem__(
        self, key: slice | SupportsIndex, value: T | Iterable[T], /
    ) -> None:
        if isinstance(key, (slice, SupportsIndex)):
            self.__create_default(key)

        return super().__setitem__(key, value)  # type: ignore


defaultlist = DefalutList
