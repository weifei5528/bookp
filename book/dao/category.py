from book.models.category import Category as CategoryModel
from book.dao.common import Common
from book.util.common import Common as CommonUtil
from book.dao.book import Book as BookDao


class Category(Common):
    def get_rand_categories(self, num=3):
        list = self.get_all_id()
        slice_list = CommonUtil.get_rand_slice(list, 3)
        return slice_list

    # 获取所有没有子类的分类
    def get_all_id(self):
        all_ids = CategoryModel.objects.filter(status="1").values('id')
        list = []
        for value in all_ids:
            son_id = self.is_son(value['id'])
            if son_id is not None:
                list.append(son_id)
        return list

    # 获取没有子类的分类
    def is_son(self, id):
        all = CategoryModel.objects.filter(pid=id, status=1).values('id')
        if len(all) == 0:
            return id
        else:
            return None

    def get_menu(self):
        parents = CategoryModel.objects.filter(status=1, pid=0).all()
        for key, item in enumerate(parents):
            sons = self.get_sons(item.id)
            parents[key].sons = sons
        return parents

    def get_sons(self, pid):
        return CategoryModel.objects.filter(pid=pid, status=1).all()

    def get_random_category_books(self):
        category_ids = self.get_rand_categories(3)
        if len(category_ids) == 0:
            return None
        category_list = CategoryModel.objects.filter(id__in=category_ids, status=1).all()
        print(category_list)
        for key, item in enumerate(category_list):
            books = BookDao.get_recommend_books(item.id)
            category_list[key].info_list = books

        return category_list
