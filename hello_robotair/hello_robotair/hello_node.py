import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class HelloRobotairNode(Node):
    def __init__(self):
        super().__init__('hello_robotair_node')
        self.publisher_ = self.create_publisher(String, 'hello_topic', 10)
        timer_period = 1.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.count = 0

    def timer_callback(self):
        msg = String()
        msg.data = f'Hello world {self.count} from Robotair'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.count += 1


def main(args=None):
    rclpy.init(args=args)
    node = HelloRobotairNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print('Keyboard interrupt received. Shutting down.')
    finally:
        if rclpy.ok():
            node.destroy_node()
            rclpy.shutdown()


if __name__ == '__main__':
    main()
