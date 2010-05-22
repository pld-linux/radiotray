Summary:	Radio Tray is an online radio streaming player
Name:		radiotray
Version:	0.5.1
Release:	2
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/radiotray/%{name}-%{version}.tar.gz
# Source0-md5:	9811f8145108784e8e515b66fdaa6f05
Patch0:		%{name}-no-song-notify.patch
URL:		http://radiotray.sourceforge.net/
BuildRequires:	gettext-devel
BuildRequires:	python-devel
BuildRequires:	python-lxml >= 2.1.5
BuildRequires:	python-pyinotify >= 0.8.6
BuildRequires:	python-pyxdg
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-gstreamer
Requires:	python-libs
Requires:	python-lxml >= 2.1.5
Requires:	python-modules
Requires:	python-pygobject >= 2.18
Requires:	python-pygtk-glade
Requires:	python-pygtk-gtk
Requires:	python-pyinotify >= 0.8.6
Requires:	python-pynotify
Requires:	python-pyxdg
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Radio Tray is an online radio streaming player that runs on a Linux
system tray. Its goal is to have the minimum interface possible,
making it very straightforward to use. Radio Tray is not a full
featured music player, there are plenty of excellent music players
already. However, there was a need for a simple application with
minimal interface just to listen to online radios. And that's the sole
purpose of Radio Tray.

%prep
%setup -q
%patch0 -p1

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS CONTRIBUTORS NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%dir %{py_sitescriptdir}/radiotray
%dir %{py_sitescriptdir}/radiotray/lib
%{py_sitescriptdir}/radiotray/*.py[co]
%{py_sitescriptdir}/radiotray/lib/*.py[co]
%{py_sitescriptdir}/radiotray-*.egg-info
