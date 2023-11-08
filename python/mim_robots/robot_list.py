## This file contains all the robots in MiM
from dataclasses import dataclass
import importlib.resources

@dataclass
class RobotInfo:
    name : str
    description : str
    urdf_path : str
    mesh_dir : str
    xml_path : str
    fixed_base : bool

with importlib.resources.path(__package__, "robot_list.py") as p:
    package_path = p.parent.absolute()


resources_path = str(package_path) + '/robots/'
mesh_dir = resources_path

# # TODO: MOVE THESE TO A YAML FILE
# mim_robots = ["iiwa", "iiwa_ft_sensor_shell", "iiwa_ft_sensor_ball", "iiwa_gripper", "teststand", "trifinger0", "trifinger1", "trifinger2"]


MiM_Robots = {

    "teststand" : RobotInfo(
                    "teststand",
                    "2 Degree of Freedom Hopper", \
                    resources_path + "teststand/urdf/teststand.urdf", \
                    resources_path + "teststand", \
                    resources_path + "teststand/xml/teststand.xml", \
                    True),
    "iiwa" : RobotInfo(
                    "iiwa", 
                    "Kuka IIWA LBR robot - 7 DoF", \
                    resources_path + "kuka/urdf/iiwa.urdf", \
                    resources_path + "kuka", \
                    resources_path + "kuka/xml/iiwa.xml", \
                    True),
    "iiwa_ft_sensor_shell" : RobotInfo(
                    "iiwa_ft_sensor_shell", 
                    "Kuka IIWA LBR robot - 7 DoF with the force torque sensor shell at the tip", \
                    resources_path + "kuka/urdf/iiwa_ft_sensor_shell.urdf", \
                    resources_path + "kuka", \
                    resources_path + "kuka/xml/iiwa_ft_sensor_shell.xml", \
                    True),
    "iiwa_ft_sensor_ball" : RobotInfo(
                    "iiwa_ft_sensor_ball", 
                    "Kuka IIWA LBR robot - 7 DoF with the force torque sensor shell at the tip with a ball", \
                    resources_path + "kuka/urdf/iiwa_ft_sensor_ball.urdf", \
                    resources_path + "kuka", \
                    resources_path + "kuka/xml/iiwa_ft_sensor_ball.xml", \
                    True),
    "iiwa_gripper" : RobotInfo(
                    "iiwa_gripper", 
                    "Kuka IIWA LBR robot - 7 DoF with gripper", \
                    resources_path + "kuka/urdf/iiwa_gripper.urdf", \
                    resources_path + "kuka", \
                    resources_path + "kuka/xml/iiwa_gripper.xml", \
                    True),
    "solo12" : RobotInfo(
                    "solo12",
                    "12 Degree of freedom quadruped robot", \
                    resources_path + "solo12/urdf/solo12.urdf", \
                    resources_path + "solo12", \
                    resources_path + "solo12/xml/solo12.xml", 
                    False),
}



