# shelves ~ 本棚共有SNS ~

ポートフォリオとして作成したWebサービスのローカル開発用リポジトリ

Webサービスの公開URLは[こちら](http://shelves.yaga.tokyo/)

## 主に使っている技術
- Django
- Vue.js
- bootstrap4
- Docker

## 実装した主な機能
- ユーザーのCRUD(djangoのdefaultパッケージであるAbstractBaseUserを使用)
- 投稿のCRUD(djangoのdefaultパッケージであるgenericを使用)
- GoogleBooksAPIを用いた書籍情報の取得（axiosでAPIから情報を取得）
- おすすめユーザー推薦機能（ピアソン相関係数を用いた簡単なユーザー推薦）
