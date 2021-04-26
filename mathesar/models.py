from django.db import models

from mathesar.database.base import create_mathesar_engine
from db import tables

engine = create_mathesar_engine()


class DatabaseObject(models.Model):
    name = models.CharField(max_length=63)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}"


class Schema(DatabaseObject):
    database = models.CharField(max_length=128)


class Table(DatabaseObject):
    schema = models.ForeignKey('Schema', on_delete=models.CASCADE, related_name='tables')

    @property
    def _sa_table(self):
        return tables.reflect_table(self.name, self.schema.name, engine)

    @property
    def sa_columns(self):
        return self._sa_table.columns

    @property
    def sa_all_records(self):
        query = tables.get_query(self._sa_table, engine)
        return query.all()
