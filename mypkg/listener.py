#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Koki Tsutaya
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class PowerListener(Node):
    def __init__(self):
        super().__init__('power_listener')
        self.subscription = self.create_subscription(
            Float32,
            'power',
            self.callback,
            10
        )

    def callback(self, msg):
        self.get_logger().info(f'Estimated Power: {msg.data:.2f} W')


def main(args=None):
    rclpy.init(args=args)
    node = PowerListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

