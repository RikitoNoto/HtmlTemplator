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

    def make_entry(self, path, reflect=False) -> EntryIF:
        entry: EntryIF
        if os.path.isfile(path):
            entry = self._make_file(path)
        elif os.path.isdir(path):
            entry = self._make_directory(path)
        elif os.path.islink(path):
            entry = self._make_link(path)
        elif os.path.ismount(path):
            entry = self._make_device(path)
        else:
            raise self.UnknownEntry("Selected unknown entry.")

        if reflect and entry is not None:
            entry.reflect()
        return entry

    def _make_file(self, path) -> File:
        return File(path)

    def _make_directory(self, path) -> Directory:
        pass

    def _make_link(self, path) -> Link:
        pass

    def _make_device(self, path) -> Device:
        pass
