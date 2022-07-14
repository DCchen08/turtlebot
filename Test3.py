import sys, rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
PI = 3.1415926535897

theta = 0

def pose_callback(pose_msg):
    rospy.loginfo("x: %.2f, y: %.2f" % (pose_msg.x, pose_msg.y))

def move():
    msg.linear.x = FORWARD_SPEED_IN_MPS
    t0 = rospy.Time.now().to_sec()
    current_distance = 0
    # Move turtle as wanted distance
    while current_distance < DISTANCE_IN_METERS:
        pub.publish(msg)
        # Get current time.
        t1 = rospy.Time.now().to_sec()
        # Calc how much distance our turtle moved.
        current_distance = FORWARD_SPEED_IN_MPS * (t1 - t0)
    msg.linear.x = 0

def turn():
    current_angle = 0
    angular_speed = ROUND_SPEED * 2 * PI / 360
    relative_angle = 45 * 2 * PI / 360
    t0 = rospy.Time.now().to_sec()
    msg.angular.z = abs(angular_speed)
    while current_angle < relative_angle:
        pub.publish(msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = angular_speed * (t1 - t0)

if __name__ == "__main__":
    robot_name = sys.argv[1]
    FORWARD_SPEED_IN_MPS = 0.5
    DISTANCE_IN_METERS = 1
    ROUND_SPEED = 5

    # Initialize the node
    rospy.init_node("move_turtle")
    # A publisher for the movement data
    pub = rospy.Publisher(robot_name+"/cmd_vel", Twist, queue_size=10)
    # A listener for pose
    sub = rospy.Subscriber(robot_name+"/pose", Pose, pose_callback, None, 10)

    # The default constructor will set all commands to 0
    msg = Twist()
    pose = Pose()
    # Loop at 10Hz, publishing movement commands until we shut down
    rate = rospy.Rate(10)
    # Drive forward at a given speed.  The robot points up the x-axis.
    move()
    # Turn counter-clockwise at a given speed.
    turn()