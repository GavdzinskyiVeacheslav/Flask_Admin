import os
from flask import url_for, Markup
from flask_admin import form
from flask_admin.contrib.sqla import ModelView
from models import Post, User

# 'C:\\Users\\mike\\pythonProject\\NAME_PROJECT'
file_path = os.path.abspath(os.path.dirname(__name__))


def name_gen_image(model, file_data):
    hash_name = f'{model.author}/post_id-{model.id}/{file_data.filename}'
    return hash_name


class PostView(ModelView):
    column_labels = {
        'id': 'ID',
        'author': 'Автор',
        'tag_post': 'Тег поста',
        'title': 'Заголовок',
        'image_post': 'Изображение поста',
        'category': 'Категория',
        'slug': 'Слаг',
        'text': 'Текст',
        'date': 'Дата',
        'user': 'Пользователь',
        'username': 'Имя',
        'tag': 'Тег',
        'tags': 'Теги',
        'name': 'Имя',
    }

    can_create = True
    can_delete = True
    can_edit = True

    column_list = ['id', 'author', Post.title, 'image_post', 'tags']
    column_default_sort = ('title', True)
    column_sortable_list = ('id', 'author', 'title', 'tags')
    column_exclude_list = []
    column_searchable_list = ['title']
    column_filters = ['title', User.username, 'tags']
    column_editable_list = ['title']

    create_modal = True
    edit_modal = True

    form_widget_args = {
        'text': {
            'rows': 5,
            'style': 'width: 100%',
            # 'style': 'color: red',
            'class': ' w-100 border border-danger text-success'
        },

        'image_post': {
            # 'style': 'color: red',
            'class': 'btn btn-primary btn-md'
        }
    }

    form_extra_fields = {
        'image_post': form.ImageUploadField(
            '',
            base_path=os.path.join(file_path, 'blog/static/storage/post_img'),
            url_relative_path='storage/post_img/',
            namegen=name_gen_image,
            allowed_extensions=['jpg'],
            max_size=(1200, 780, True),
            thumbnail_size=(100, 100, True),
        )
    }

    def _list_thumbnail(view, context, model, name):
        if not model.image_post:
            return ''

        url = url_for('static', filename=os.path.join('storage/post_img/', model.image_post))

        if model.image_post.split('.')[-1] in ['jpg', 'jpeg', 'png', 'svg', 'gif']:
            return Markup(f'<img src={url} width="100">')

        # Передача функции _list_thumbnail в поле image_user

    column_formatters = {
        'image_post': _list_thumbnail
    }

    def create_form(self, obj=None):
        return super(PostView, self).create_form(obj)

    def edit_form(self, obj=None):
        return super(PostView, self).edit_form(obj)



















