# 掛け算を鍛えるROSパッケージ

2021年度のロボットシステム学で作成したROSのパッケージです。表示される掛け算の答えを入力すると正解か不正解かを判別してくれます。レベルは３つあり、それぞれ選択できます。


___


## 環境

- 本体 : Raspberry Pi 4 

- OS  :  ubuntu 20.04 

___

## 実装内容

このROSパッケージはロボットシステム学第10回の講義内に作成したパッケージ[mypkg](https://github.com/ryuichiueda/robosys2020/blob/master/md/ros.md)を参考に作成しています。
- ノードを起動しスタートすると掛け算が表示されます。その掛け算の答えが正解か不正解かを判別します。
- 間違った答えを入力すると正しい答えを表示します。
- Lv1 (1桁×1桁) Lv2 (2桁×1桁) Lv3 (2桁×2桁)の３つのレベルがあります。
___
## 環境
### ワークスペース
以下のロボットシステム第10回の資料を参考にワークスペースを構築しています。

https://github.com/ryuichiueda/robosys2020/blob/master/md/ros.md

___
## インストール
パッケージを使用するために以下のコマンドを実行してください。
```
$ git clone 
$ cd robotsystem2021_devicedriver/myled
$ make  
$ sudo insmod myled.ko  
$ sudo chmod 666 /dev/myled0  
```
2.目的の動作をさせるために以下のように入力してください。
#### 点灯と消灯の間隔が短くなりながら点滅

```
$ echo 0 > /dev/myled0
```

#### 一定のリズムで点滅

```
$ echo 1 > /dev/myled0
```

#### モールス信号で「こんにちは」

```
$ echo 2 > /dev/myled0
```
___

## 終了するとき
終了する場合は以下のコマンドを実行してください。

```
$ sudo rmmod myled
$ make clean
```
___

## デモ動画

下のリンクよりデモ動画を見れます。

https://youtu.be/-5IIXfJk4Gs
___

## ライセンス

[GNU General Public License v3.0]
