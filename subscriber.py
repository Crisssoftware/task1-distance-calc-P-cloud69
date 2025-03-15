import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from std_msgs.msg import Float32
import math

class DistanceCalculator(Node):
    def __init__(self):
        super().__init__('node')

       
        self.subscription = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.callback,
            10
        )

       
        self.publisher = self.create_publisher(Float32, '/turtle1/distance', 10)

    def callback(self, msg):
        
        x = msg.x
        y = msg.y

        distance = math.sqrt(x*x + y*y)

        self.get_logger().info(f"Distance from origin: {distance}")

        distance_msg = Float32()
        distance_msg.data = distance
        self.publisher.publish(distance_msg)


def main(args=None):
    rclpy.init(args=args)
    node = DistanceCalculator()

    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == '__main__':
    main()

