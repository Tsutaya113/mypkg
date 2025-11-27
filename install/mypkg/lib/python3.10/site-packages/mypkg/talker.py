import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Int16, "countup", 10)
n = 0
def cb():          #20行目で定期実行されるコールバック関数
    global n       #関数を抜けてもnがリセットされないようにしている
    msg = Int16()  #メッセージの「オブジェクト」
    msg.data = n   #msgオブジェクトの持つdataにnを結び付け
    pub.publish(msg)        #pubの持つpublishでメッセージ送信
    n += 1

def main():
    node.create_timer(0.5, cb)  #タイマー設定
    rclpy.spin(node)
