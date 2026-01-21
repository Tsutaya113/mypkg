#!/bin/bash -xv
# SPDX-FileCopyrightText: 2025 Koki Tsutaya
# SPDX-License-Identifier: BSD-3-Clause

ng () {
    echo "NG"
    exit 1
}

# 作業用ディレクトリ（どこで実行されてもOK）
WORKDIR=$(mktemp -d)
cd "$WORKDIR" || ng

source /opt/ros/humble/setup.bash || ng

# ワークスペース構築
mkdir -p ros2_ws/src || ng
rsync -av "$GITHUB_WORKSPACE/" ros2_ws/src/mypkg > /dev/null

cd ros2_ws || ng
colcon build --packages-select mypkg > /dev/null 2>&1 || ng
source install/setup.bash || ng

# テスト実行
timeout 10 ros2 launch mypkg talk_listen.launch.py \
  > /tmp/mypkg.log 2>&1 || true

grep -q "Estimated Power:" /tmp/mypkg.log || ng

echo "OK"
exit 0


