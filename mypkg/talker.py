#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Koki Tsutaya
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import time

class PowerTalker(Node):
    def __init__(self):
        super().__init__('power_talker')
        self.publisher_ = self.create_publisher(Float32, 'power', 10)

        self.prev_idle, self.prev_total = self.read_cpu_stat()
        self.timer = self.create_timer(1.0, self.timer_callback)

        # ノートPC想定のTDP（適当でOK）
        self.TDP_WATT = 15.0

    def read_cpu_stat(self):
        with open('/proc/stat', 'r') as f:
            cpu = f.readline().split()
            idle = int(cpu[4])
            total = sum(map(int, cpu[1:]))
            return idle, total

    def timer_callback(self):
        idle, total = self.read_cpu_stat()

        idle_diff = idle - self.prev_idle
        total_diff = total - self.prev_total

        cpu_usage = 1.0 - (idle_diff / total_diff)

        power = cpu_usage * self.TDP_WATT

        msg = Float32()
        msg.data = power
        self.publisher_.publish(msg)

        self.prev_idle = idle
        self.prev_total = total


def main(args=None):
    rclpy.init(args=args)
    node = PowerTalker()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

