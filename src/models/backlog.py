from sqlalchemy import Column, String, DateTime, Uuid
from datetime import datetime
from typing import Union

import uuid

from src .config.sqlachemy import db


class Backlog(db.Model):
    __tablename__ = 'Pendencia'

    id = Column("pk_pendencia", Uuid, primary_key=True, default=uuid.uuid4)
    author = Column(String(140))
    title = Column(String(140), unique=True)
    equipment = Column(String(140))
    description = Column(String(280))
    status = Column(String(140))
    insert_date = Column(DateTime, default=datetime.now())

    def __init__(
            self,
            author: str,
            title: str,
            equipment: str,
            description: str,
            status: str,
            insert_date: Union[DateTime, None] = None
            ):
        """
        Cria um pendencia

        Arguments:
            autor: autor do pendencia.
            titulo: titulo da pendência
            equipamento: mostra qual o equipamento a pendencia está se referindo
            descricao: descricao esperado para a pendencia
            status: status que a pendência se encontra
            data_insercao: data de quando o pendencia foi inserido à base
        """
        print("dentro da model da pendencia")

        self.author = author
        self.title = title
        self.equipment = equipment
        self.description = description
        self.status = status

        # se não for informada, será o data exata da inserção no banco
        if insert_date:
            self.insert_date = insert_date
