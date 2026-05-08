# from moveit_configs_utils import MoveItConfigsBuilder
# from moveit_configs_utils.launches import generate_moveit_rviz_launch


# def generate_launch_description():
#     moveit_config = MoveItConfigsBuilder("basic_scara", package_name="scara_moveit").to_moveit_configs()
#     return generate_moveit_rviz_launch(moveit_config)


from launch import LaunchDescription
from launch_ros.actions import Node
from moveit_configs_utils import MoveItConfigsBuilder
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    moveit_config = (
        MoveItConfigsBuilder("basic_scara", package_name="scara_moveit")
        .to_moveit_configs()
    )

    rviz_config_file = os.path.join(
        get_package_share_directory("scara_moveit"),
        "config",
        "moveit.rviz",
    )

    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        output="screen",
        arguments=["-d", rviz_config_file],
        parameters=[
            moveit_config.robot_description,
            moveit_config.robot_description_semantic,
            moveit_config.robot_description_kinematics,
            moveit_config.planning_pipelines,
            moveit_config.joint_limits,
            {"use_sim_time": True},
        ],
    )

    return LaunchDescription([rviz_node])