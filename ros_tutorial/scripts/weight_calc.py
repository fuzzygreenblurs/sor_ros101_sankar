import rospy
from std_msgs.msg import Float64
from ros_tutorial.msg import Weight, Cylinder

density = 0
volume = 0

density_found = False
volume_found = False

def store_density(data):
    global density
    global density_found
    density = data.data
    density_found = True


def store_volume(data):
    global volume
    global volume_found
    volume = data.volume
    volume_found = True

def calculate():
    if density_found and volume_found:
        msg = Weight()
        msg.weight = density * volume
        msg.density = density

        pub.publish(msg)

rospy.init_node("weight_calc")
rospy.Subscriber("/density", Float64, store_density)
rospy.Subscriber("/cylinder", Cylinder, store_volume)

pub = rospy.Publisher("/weight", Weight, queue_size=10)

while not rospy.is_shutdown():
    calculate()
    rospy.sleep(0.1)
