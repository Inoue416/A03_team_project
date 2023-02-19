# Docker使い方（usecase）

# 前提（準備）
- ### Dockerのインストール（Docker for desktop）
これに関しては、ネットで調べたら、沢山情報があるはず。<br>
[日本版のドキュメント（多分公式？）](https://docs.docker.jp/docker-for-windows/install.html)<br>
加えて、自分がWindowsユーザなので、自分ではMacについては教えられない気がする<br>
- ### Docker-composeのインストール
これもネットで調べれば、大丈夫なはず。<br>
[日本版のドキュメント（多分公式？）](https://docs.docker.jp/compose/install.html)<br>
[公式ドキュメント](https://docs.docker.com/compose/install/)

# 基本的なUsecase
- ## コンテナを起動する。（デフォルトでrunserverするようになっている）
```bash
docker-compose up
```
### しっかり起動しているか確認方法
- [127.0.0.0:8000](127.0.0.0:8000)にアクセスしてDjangoのページが表示されればOK
#### 注意点
- しっかり、docker-compose.ymlを配置してあるフォルダーで実行してね
- もし、それでも動かない場合は下記のコマンドを使って、dockerとdocker-composeがインストールできてるか確認してみて！
```bash
docker --version
or
docker-compose version
```
- ## コンテナを止める
```bash
Ctrl + C
or
docker-compose down
```
※基本的にCtrl+Cを使う。（バックグランドでコンテナを実行して場合は下を使うかも）


- ## コマンドを実行
```bash
docker-compose run --rm app sh -c "<command>"
```
### よく使うコマンド一覧
```bash
docker-compose run --rm app sh -c "python manage.py makemigrations"
```
```bash
docker-compose run --rm app sh -c "python manage.py migrate"
```
```bash
docker-compose run --rm app sh -c "pyhton manage.py test"
```