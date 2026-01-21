# mypkg

本リポジトリは、千葉工業大学 未来ロボティクス学科における2025年度「ロボットシステム学」の授業内容（lesson8, lesson9）をもとに作成した、ROS2 の基本的な publish / subscribe 通信を学習するための練習用パッケージです。

本パッケージでは、PC の CPU 使用率から推定した消費電力を talker ノードで計算・送信するシステムを構築しています。

## 消費電力量チェッカー
![test](https://github.com/Tsutaya113/mypkg/actions/workflows/test.yml/badge.svg)  
本パッケージは、PC の CPU 使用率をもとに消費電力を推定し、
その推定結果を ROS 2 のトピックとして配信することを目的としています。

- **talker ノード**
  - `/proc/stat` から CPU 使用率を取得
  - CPU 使用率をもとに消費電力を推定
  - 推定した消費電力をトピックとして publish

- **launch ファイル**
  - talker と listener を同時にに起動可能

### 使い方

### 1. ワークスペースのビルド

```shell
$ cd ~/ros2_ws/src
$ git clone https://github.com/yagikai2112/mypkg.git
$ cd ~/ros2_ws
$ colcon build
$ source install/setup.bash
```

### 2-1. ノードを個別に起動する場合

### ターミナル①（talker）
```shell
ros2 run mypkg talker
```

※ talker は publish のみを行い、画面出力は行いません。

### ターミナル②（listener）
```shell
ros2 run mypkg listener
```

実行すると以下のように消費電力が表示されます。
```shell
[INFO] [power_listener]: Estimated Power: 6.32 W
[INFO] [power_listener]: Estimated Power: 10.85 W
```

### 2-2. ノードを個別に起動する場合
```shell
ros2 launch mypkg power.launch.py
```

- talker と listener が同時に起動し、listener 側にのみ消費電力が表示されます。

## 推定方法について
以下の計算方法で推定  
CPU使用率 (%) × CPUのTDP（例: 15W）＝ 推定消費電力(W)

## テスト環境
- Ubuntu 22.04 LTS
- ROS2 Humble
- Python 3.10

## 著作権・ライセンス
- このソフトウェアパッケージは、3条項BSDの下、再頒布および使用が許可されています。  
- © 2025 Tsutaya Koki
