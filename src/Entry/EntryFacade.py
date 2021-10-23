import os
try:
    from Entry import EntryIF
    from Entry import File
    from Entry import Directory
    from Entry import Link
    from Entry import Device

except ModuleNotFoundError:
    from .Entry import EntryIF
    from .Entry import File
    from .Entry import Directory
    from .Entry import Link
    from .Entry import Device


class EntryFacade:

    class UnknownEntry(Exception):
        pass

    @classmethod
    def make(cls, path: str, content: tuple, reflect=False) -> EntryIF:
        entry: EntryIF
        if os.path.isfile(path):
            entry = cls._make_file(path)
        elif os.path.isdir(path):
            entry = cls._make_directory(path)
        elif os.path.islink(path):
            entry = cls._make_link(path)
        elif os.path.ismount(path):
            entry = cls._make_device(path)
        else:
            raise cls.UnknownEntry("Selected unknown entry.")

        if reflect and entry is not None:
            entry.reflect()
        return entry

    @staticmethod
    def make_file(path) -> File:
        return File(path)

    @staticmethod
    def make_directory(path) -> Directory:
        pass

    @staticmethod
    def make_link(path) -> Link:
        pass

    @staticmethod
    def _make_device(path) -> Device:
        pass
