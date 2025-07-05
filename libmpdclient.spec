#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	MPD client library
Summary(pl.UTF-8):	Biblioteka kliencka MPD
Name:		libmpdclient
Version:	2.22
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	https://www.musicpd.org/download/libmpdclient/2/%{name}-%{version}.tar.xz
# Source0-md5:	3c9ddd62e1c97f5530733acf6b7bde9f
URL:		http://www.musicpd.org/doc/libmpdclient/
BuildRequires:	doxygen
BuildRequires:	meson >= 0.56.0
BuildRequires:	ninja
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library for Music Player Daemon client development.

%description -l pl.UTF-8
Biblioteka do tworzenia klientów demona MPD (Music Player Daemon).

%package devel
Summary:	Header files for the MPD client library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki klienckiej MPD
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	vala-libmpdclient < 2.22

%description devel
Header files for MPD client library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki klienckiej MPD.

%package static
Summary:	Static MPD client library
Summary(pl.UTF-8):	Statyczna biblioteka kliencka MPD
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static MPD client library.

%description static -l pl.UTF-8
Statyczna biblioteka kliencka MPD.

%prep
%setup -q

%build
%meson \
	%{!?with_static_libs:--default-library=shared} \
	-Ddocumentation=true

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

rm -rf $RPM_BUILD_ROOT%{_docdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSES NEWS README.rst
%attr(755,root,root) %{_libdir}/libmpdclient.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libmpdclient.so.2

%files devel
%defattr(644,root,root,755)
%doc build/doc/html
%attr(755,root,root) %{_libdir}/libmpdclient.so
%{_includedir}/mpd
%{_pkgconfigdir}/libmpdclient.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libmpdclient.a
%endif
