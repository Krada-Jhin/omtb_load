################################################################################
# Set minimum required version of cmake, project name and compile options
################################################################################
cmake_minimum_required(VERSION 2.8.3)
project(omtb_control)

add_compile_options(-std=c++11)
################################################################################
# Find catkin packages and libraries for catkin and system dependencies
################################################################################
find_package(catkin REQUIRED COMPONENTS
  rospy
  roscpp
  std_msgs
  geometry_msgs
  nav_msgs
  moveit_msgs
  trajectory_msgs
  open_manipulator_msgs
  ar_track_alvar_msgs
  moveit_core
  moveit_ros_planning
  moveit_ros_planning_interface
  smach
  smach_ros
)

################################################################################
# Setup for python modules and scripts
################################################################################
catkin_python_setup()

################################################################################
# Declare ROS messages, services and actions
################################################################################

################################################################################
# Declare ROS dynamic reconfigure parameters
################################################################################

################################################################################
# Declare catkin specific configuration to be passed to dependent projects
################################################################################
catkin_package(
  INCLUDE_DIRS include
  CATKIN_DEPENDS rospy roscpp std_msgs geometry_msgs nav_msgs moveit_msgs trajectory_msgs open_manipulator_msgs ar_track_alvar_msgs moveit_core moveit_ros_planning moveit_ros_planning_interface smach smach_ros
)

################################################################################
# Build
################################################################################
include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)

add_executable(moveit_bridge src/moveit_bridge.cpp)
add_dependencies(moveit_bridge ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(moveit_bridge ${catkin_LIBRARIES})

add_executable(gazebo_bridge src/gazebo_bridge.cpp)
add_dependencies(gazebo_bridge ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(gazebo_bridge ${catkin_LIBRARIES})

add_executable(gripper_server src/gripper_server.cpp)
add_dependencies(gripper_server ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(gripper_server ${catkin_LIBRARIES})
################################################################################
# Install
################################################################################
catkin_install_python(PROGRAMS
  nodes/tb3_teleop_key.py
  nodes/automove_room1.py
<<<<<<< HEAD
  nodes/automove_room1_v=.py
=======
>>>>>>> 966386af94ecff44a331ccb2bc4c3d65238025a4
  nodes/automove_room2.py
  nodes/pick_and_place_robot1.py
  nodes/pick_and_place_robot2.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY launch nodes
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

################################################################################
# Test
################################################################################
