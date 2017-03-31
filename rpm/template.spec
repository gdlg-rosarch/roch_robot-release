Name:           ros-indigo-roch-control
Version:        1.0.13
Release:        2%{?dist}
Summary:        ROS roch_control package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/roch_control
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-controller-manager
Requires:       ros-indigo-create-node
Requires:       ros-indigo-diff-drive-controller
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-interactive-marker-twist-server
Requires:       ros-indigo-joint-state-controller
Requires:       ros-indigo-joint-trajectory-controller
Requires:       ros-indigo-joy
Requires:       ros-indigo-robot-localization
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-rostopic
Requires:       ros-indigo-teleop-twist-joy
Requires:       ros-indigo-twist-mux
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-joy
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-roslaunch

%description
SawYer roch controller configurations

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Mar 31 2017 Carl <wzhang@softrobtech.com> - 1.0.13-2
- Autogenerated by Bloom

* Thu Mar 30 2017 Carl <wzhang@softrobtech.com> - 1.0.13-1
- Autogenerated by Bloom

* Thu Mar 23 2017 Carl <wzhang@softrobtech.com> - 1.0.13-0
- Autogenerated by Bloom

* Thu Feb 23 2017 Carl <wzhang@softrobtech.com> - 1.0.12-0
- Autogenerated by Bloom

* Tue Feb 07 2017 Carl <wzhang@softrobtech.com> - 1.0.11-0
- Autogenerated by Bloom

* Tue Jan 24 2017 Carl <wzhang@softrobtech.com> - 1.0.10-0
- Autogenerated by Bloom

* Sun Jan 22 2017 Carl <wzhang@softrobtech.com> - 1.0.8-0
- Autogenerated by Bloom

* Sat Jan 21 2017 Carl <wzhang@softrobtech.com> - 1.0.7-0
- Autogenerated by Bloom

* Fri Jan 20 2017 Carl <wzhang@softrobtech.com> - 1.0.6-1
- Autogenerated by Bloom

* Fri Jan 20 2017 Carl <wzhang@softrobtech.com> - 1.0.6-0
- Autogenerated by Bloom

