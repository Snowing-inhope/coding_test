# -*- coding:utf-8 -*-
from exts import db


class DbOptions():
    # 存储一个对象
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return "success"
        except BaseException as e:
            db.session.rollback()
            return str(e)

    # 存储多个对象
    @classmethod
    def saveAll(cls, arr):
        try:
            db.session.add_all(arr)
            db.session.commit()
            return "success"
        except BaseException as e:
            db.session.rollback()
            return str(e)

    # 删除一个对象
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return "success"
        except BaseException as e:
            db.session.rollback()
            return str(e)

    def insertall(self, arr):
        try:
            db.session.execute(self.__table__.insert(), arr)
            db.session.commit()
            return "success"
        except BaseException as e:
            db.session.rollback()
            return str(e)


class GoodsInfo(db.Model, DbOptions):
    __tablename__ = "goodsinfo"
    __table_args__ = {
        "mysql_charset": "utf8"
    }
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(256), comment="标题")
    seller = db.Column(db.String(256), comment="商家")
    date = db.Column(db.DATETIME, comment="时间")
    price = db.Column(db.Float, comment="价格")
    average_score = db.Column(db.Float, comment="评分")
    reviews = db.Column(db.String(64), comment="评论")
    rankings = db.Column(db.Integer, comment="排名")

    def __init__(self, title, seller, date, price, average_score,
                 reviews, rankings):
        self.title = title
        self.seller = seller
        self.date = date
        self.price = price
        self.average_score = average_score
        self.reviews = reviews
        self.rankings = rankings

    def toDict(self):
        return {"title": self.title, "seller": self.seller, "date": self.date,
                "price": self.price, "average_score": self.average_score,
                "reviews": self.reviews, "rankings": self.rankings}
