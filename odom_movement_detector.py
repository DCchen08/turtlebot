import rospy
import math
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point
from std_msgs.msg import Float_64

class Movedetector(Object):
    def __init__(self):
        self._mved_distance = Float_64()
        self._mved_distance.data = 0.0
        self.get_init_position()
        self.distance_moved_pub = rospy.Publisher('/moved_publiser',Float_64,queue_size=1)
        rospy.Subscriber('/odom',Odometry,self.odom_callback)
    
    def get_init_position(self):
        data_odom = None
        while data_odom is None:
            try:
                data_odom = rospy.wait_for_message('odom',Odometry,timeout = 1)
            except:
                rospy.loginfo("Current is not ready")

        self._current_position = Point()
        self._current_position.x = data_odom.pose.pose.position.x
        self._current_position.y = data_odom.pose.pose.position.y
        self._current_position.z = data_odom.pose.pose.position.z

    def updatedcurrent_position(self, new_position):
        self._current_position.x = new_position.x
        self._current_position.y = new_position.y
        self._current_position.z = new_position.z

    def calculate_distance(self,new_position,old_position):
        x2 = new_position.x
        x1 = old_position.x
        y2 = new_position.y
        y1 = old_position.y
        dist = math.hypot(x2-x1,y2-y1)
        return dist

    def publish_moved_distance(self):
        rospy.spin()



if __name__ == "__main__":
    rospy.init_node('move_detector_node',anonymous = True)
    movement_obj = MovementDetector()
    movement_obj.publish_move_distance()




