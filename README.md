# mypkg

本リポジトリは、千葉工業大学 未来ロボティクス学科における2025年度「ロボットシステム学」の授業内容（lesson8, lesson9）をもとに作成した、  
ROS2 の基本的な publish / subscribe 通信を学習するための練習用パッケージです。

本パッケージでは、PC の CPU 使用率から推定した消費電力を talker ノードで計算・送信し、  
listener ノードで受信・表示するシステムを構築しています。

## 概要

- **talker ノード**
  - `/proc/stat` から CPU 使用率を取得
  - CPU 使用率をもとに消費電力を推定
  - 推定した消費電力をトピックとして publish

- **listener ノード**
  - talker が送信した消費電力を subscribe
  - 1秒周期で消費電力を画面に表示

- **launch ファイル**
  - talker と listener を同時にに起動可能

### 使い方

### 1. ワークスペースのビルド

```shell
cd ~/ros2_ws
colcon build
source install/setup.bash
```



## テスト環境
- Ubuntu 22.04.5 LTS

## 必要なソフトウェア
- Github Actions
  - テスト済みのpythonバージョン: 3.7 ~ 3.12  

## 著作権・ライセンス・利用しているソフトウェア
- Ubuntu 22.04.5 LTS / Python3 .13 .5
- このソフトウェアパッケージは、3条項BSDの下、再頒布および使用が許可されています。  
- 本[README](https://github.com/Tsutaya113/robosys2025/blob/main/README.md)は、[asnm1208](https://github.com/asnm1208)の[robosys2025](https://github.com/asnm1208/robosys2025/blob/main/README.md)（© 2025 asnm1208）と[tadano0405](https://github.com/tadano0504)の[robosys2025](https://github.com/tadano0504/robosys2025/blob/main/README.md)（© 2025 Tadano Keito）を参考に作られています。
- © 2025 Tsutaya Koki
