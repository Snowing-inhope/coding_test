# -*- coding:utf-8 -*-
from datetime import datetime, date
from urllib.request import urlopen
import re
from bs4 import BeautifulSoup
from flask import Blueprint, render_template, request, redirect, url_for, json
from app.models import GoodsInfo

goodInfo = Blueprint("app", __name__)


@goodInfo.route("/")
def toIndex():
    urlstr = url_for("app.index", _external=True)
    print(urlstr)
    return redirect(urlstr)


@goodInfo.route('/index/')
def index():
    return render_template("index.html")


@goodInfo.route('/goodinfo/', methods=['GET', 'POST'])
def goodinfo():
    # url获取
    good_id = request.args.get('id')
    url = 'https://www.amazon.cn/dp/' + good_id + '/'
    # 爬取解析
    html = urlopen(url, timeout=20).read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    item_list = soup.select("#productTitle")
    data_list = []
    for i in range(len(item_list)):
        title = soup.select("#productTitle")[i].get_text().strip()
        date = datetime.now()
        price01 = soup.select("#soldByThirdParty")[i].get_text().strip()
        price = eval(re.findall(r'￥(.*..*)', price01)[0])
        seller_list = re.findall(r'由(.*)销售', price01)
        seller = (re.findall(r'由(.*)销售', price01)[0]
                  if seller_list else '亚马逊')
        score_list = soup.select("#acrPopover")
        average_score = soup.select(
            "#acrPopover")[i].get_text().split(' ')[1] \
            if score_list else None
        review_list = soup.select("#acrCustomerReviewText")
        reviews = soup.select(
            "#acrCustomerReviewText")[i].get_text().split(' ')[0] \
            if review_list else None
        rankings = i + 1
        item = [title, seller, date, price, average_score, reviews, rankings]
        data_list.append(item)

        goods = GoodsInfo(title, seller, date, price, average_score,
                          reviews, rankings)
        goods.save()

    return json.dumps({"goodinfo": data_list}, cls=ComplexEncoder)


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)
