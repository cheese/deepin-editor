Name:           deepin-editor
Version:        5.9.0.24
Release:        1%{?dist}
Summary:        Simple editor for Linux Deepin
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-editor
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  freeimage-devel
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5SyntaxHighlighting)
BuildRequires:  cmake(DFrameworkdbus)
BuildRequires:  pkgconfig(dtkwidget) >= 2.0.6
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(xcb-aux)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(polkit-qt5-1)
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  desktop-file-utils
BuildRequires:  qt5-linguist
BuildRequires:  gtest-devel
BuildRequires:  gmock-devel
BuildRequires:  qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
Requires:       deepin-notifications
Requires:       deepin-qt5integration
# bundled libraries
Provides:       bundled(libiconv) = 1.16
Provides:       bundled(enca) = 1.19
Provides:       bundled(uchardet) = 0.0.7

%description
%{summary}.

%prep
%autosetup -p1
# force bundled libaries install to 'third/lib/lib'
sed -i 's/lib$/lib -DCMAKE_INSTALL_LIBDIR=lib/' third/uchartdet_install.sh

%build
# force bundled libaries to build with -fPIE
export CFLAGS="%{optflags} -fPIE"
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
