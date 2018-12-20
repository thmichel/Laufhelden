# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       harbour-laufhelden

# >> macros
# << macros

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    Laufhelden - Sport tracker
Version:    1.1.3
Release:    1
Group:      Qt/Qt
License:    GPL
URL:        http://example.org/
Source0:    %{name}-%{version}.tar.bz2
Source100:  harbour-laufhelden.yaml
Requires:   sailfishsilica-qt5 >= 0.10.9
Requires:   qt5-plugin-geoservices-osm >= 5.2.0
Requires:   qt5-qtlocation >= 5.2.0
Requires:   qt5-qtdeclarative-import-location >= 5.2.0
Requires:   qt5-qtdeclarative-import-positioning >= 5.2.0
Requires:   qt5-qtconnectivity-qtbluetooth >= 5.2.0
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Bluetooth)
BuildRequires:  desktop-file-utils

%description
Laufhelden records your track when you walk, run, cycle or practise any other outdoor activity.

%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qtc_qmake5  \
    VERSION='%{version}-%{release}'

%qtc_make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%{_bindir}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
# >> files
# << files
