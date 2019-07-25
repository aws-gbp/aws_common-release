Name:           ros-melodic-aws-common
Version:        2.1.0
Release:        1%{?dist}
Summary:        ROS aws_common package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://wiki.ros.org/aws_common
Source0:        %{name}-%{version}.tar.gz

Requires:       curl
Requires:       libcurl-devel
Requires:       libuuid-devel
Requires:       openssl-devel
Requires:       zlib-devel
BuildRequires:  cmake
BuildRequires:  curl
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
BuildRequires:  libcurl-devel
BuildRequires:  libuuid-devel
BuildRequires:  openssl-devel
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-ros-environment
BuildRequires:  zlib-devel

%description
Common AWS SDK utilities, intended for use by ROS packages using the AWS SDK

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Wed Jul 24 2019 AWS RoboMaker <ros-contributions@amazon.com> - 2.1.0-1
- Autogenerated by Bloom

* Thu Mar 21 2019 AWS RoboMaker <ros-contributions@amazon.com> - 2.0.0-2
- Autogenerated by Bloom

* Wed Mar 20 2019 AWS RoboMaker <ros-contributions@amazon.com> - 2.0.0-1
- Autogenerated by Bloom

