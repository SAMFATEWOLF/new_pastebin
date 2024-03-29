from .models import *

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'FAQ', 'url_name': 'faq'},

]


class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs

        user_menu = menu.copy()
        # if not self.request.user.is_authenticated:
        #     user_menu.pop(1)

        context['menu'] = user_menu
        return context
