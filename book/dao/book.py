from book.models.books import Books as BookModel
from book.dao.common import Common


class Book(Common):
    # 获取指定分类的推荐的图书
    def get_recommend_books(self, cat_id):
        all = BookModel.objects.filter(status=1, cat_id=cat_id).all()[:10]
        print(all)
        return all

