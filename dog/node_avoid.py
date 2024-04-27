import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import UInt16

SAFE_DISTANCE = 1

class ObstacleAvoidance(Node):
    def __init__(self):
        super().__init__('obstacle_avoidance')
        self.subscription = self.create_subscription(UInt16, 'ultrasonic_distance', self.listener_callback, 10)
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        self.cmd_vel = Twist()

    def listener_callback(self, msg):
        distance = msg.data
        if distance < SAFE_DISTANCE:  # 定义一个安全距离
            # 根据测距值调整机器狗的行动
            speed_x=0.0
            speed_y=1.0
            speed_z=0.0
            self.dog_name = "dogc2"
            self.declare_parameter("speed_x",0.0)
            self.declare_parameter("speed_y",1.0)
            self.declare_parameter("speed_z",0.0)
            self.declare_parameter("dog_name","dogc2")
            self.timer = self.create_timer(0.1,self.timer_callback)
            self.pub = self.create_publisher(Float32, f'/{self.dog_name}/ObstacleAvoidance', 10)



        else:
            # 正常前行
            
        self.publisher.publish()

def main(args=None):
    rclpy.init(args=args)
    obstacle_avoidance = ObstacleAvoidance()
    rclpy.spin(obstacle_avoidance)
    obstacle_avoidance.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()