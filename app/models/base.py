from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer
from fastapi import HTTPException, status

from typing import List, TypeVar, Type


T = TypeVar("T", bound="Base")
EntityMeta = declarative_base()


class Base(EntityMeta):
    __abstract__ = True

    id = Column(
        Integer,
        primary_key=True,
        unique=True,
    )

    def pre_add(self, item: dict) -> None:
        """Function before create"""
        pass

    def pre_update(self, item: dict) -> None:
        """Function before update"""
        pass

    def pre_delete(self) -> None:
        """Function before delete"""
        pass

    @classmethod
    def get_all(
        cls: Type[T],
        db: Session,
        size: int = -1,
        page: int = 0,
        order: str = None,
    ) -> List[T]:
        query = db.query(cls)

        if size > 0:
            query = query.limit(size)
        if page > 0:
            query = query.offset((page - 1) * size)

        if order is not None:
            query.order_by(getattr(cls, order))

        items = query.all()

        return items

    @classmethod
    def get(cls: Type[T], db: Session, id: str) -> T:
        item = db.query(cls).get(id)
        if item is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"{cls.__name__} not found",
            )
        return item

    @classmethod
    def create(cls: Type[T], db: Session, json: dict) -> T:
        try:
            new_item = cls(**json)
            new_item.pre_add(json)
            db.add(new_item)
            db.commit()
            db.refresh(new_item)
            return new_item
        except IntegrityError as ex:
            db.rollback()
            raise ex
        except Exception as ex:
            raise ex

    @classmethod
    def delete(cls: Type[T], db: Session, id: str) -> dict:
        item = cls.get(db, id)

        try:
            item.pre_delete()
            db.delete(item)
            db.commit()
            return {"detail": f"{cls.__name__} deleted"}
        except IntegrityError as ex:
            db.rollback()
            raise ex
        except Exception as ex:
            raise ex

    @classmethod
    def update(cls, db: Session, id: str, json: dict) -> dict:
        item = cls.get(db, id)

        try:
            item.pre_update(json)
            for key, value in json.items():
                setattr(item, key, value)
            db.commit()
            return item
        except IntegrityError as ex:
            db.rollback()
            raise ex
        except Exception as ex:
            raise ex

    @classmethod
    def bulk(cls: Type[T], db: Session, json: List[dict]) -> List[T]:
        try:
            items = []
            for item in json:
                new_item = cls(**item)
                new_item.pre_add(item)
                items.append(new_item)

            db.add_all(items)
            db.commit()
            return items
        except IntegrityError as ex:
            db.rollback()
            raise ex
        except Exception as ex:
            raise ex

    @classmethod
    def filter_first(cls: Type[T], db: Session, *filters) -> T:
        item = db.query(cls).filter(*filters).first()

        return item

    @classmethod
    def filter_all(cls: Type[T], db: Session, *filters) -> List[T]:
        items = db.query(cls).filter(*filters).all()

        return items
