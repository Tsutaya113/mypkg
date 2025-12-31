#!/bin/bash
# SPDX-FileCopyrightText: 2025 Koki Tsutaya
# SPDX-License-Identifier: BSD-3-Clause

# ワークスペース指定（引数があればそれを使用）
workspace=${1:-"$HOME/ros2_ws"}

cd "$workspace" || exit 1

# パッケージをビルド
colcon build --packages-select mypkg > /dev/null 2>&1 || exit 1

# ROS 2 環境読み込み
source /opt/ros/humble/setup.bash > /dev/null 2>&1
source install/setup.bash > /dev/null 2>&1

# launch を 10 秒間実行してログ取得
timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log 2>&1

# Estimated Power の出力があるか確認
if ! grep -q "Estimated Power:" /tmp/mypkg.log; then
    echo "error"
    exit 1
fi

# 正常終了メッセージ
echo "OK"
exit 0

