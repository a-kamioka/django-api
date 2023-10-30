プロジェクト・アプリの作成
$ django-admin startproject project
$ cd project
$ python startapp api

モデルの定義（models.py）

データベース構築（settings.py）

$ python manage.py makemigrations api
$ python manage.py migrate

Serializerの定義

ViewSetの定義

URL pattern定義

API動作確認
$ python manage.py runserver