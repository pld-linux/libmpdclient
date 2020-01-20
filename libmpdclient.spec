Summary:	MPD client library
Summary(pl.UTF-8):	Biblioteka kliencka MPD
Name:		libmpdclient
Version:	2.18
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	http://www.musicpd.org/download/libmpdclient/2/%{name}-%{version}.tar.xz
# Source0-md5:	3f9f4c684ec4b60d6610dc33808af1c9
URL:		http://www.musicpd.org/doc/libmpdclient/
BuildRequires:	doxygen
BuildRequires:	meson > 0.38.1
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.727
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

%package -n vala-libmpdclient
Summary:	libmpdclient API for Vala language
Summary(pl.UTF-8):	API libmpdclient dla języka Vala
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n vala-libmpdclient
libmpdclient API for Vala language.

%description -n vala-libmpdclient -l pl.UTF-8
API libmpdclient dla języka Vala.

%prep
%setup -q

%build
%meson build \
	-Ddocumentation=true

%meson_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install -C build

rm -rf $RPM_BUILD_ROOT%{_docdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.rst COPYING AUTHORS NEWS
%attr(755,root,root) %{_libdir}/libmpdclient.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libmpdclient.so.2

%files devel
%defattr(644,root,root,755)
%doc build/doc/html
%attr(755,root,root) %{_libdir}/libmpdclient.so
%{_includedir}/mpd
%{_pkgconfigdir}/libmpdclient.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libmpdclient.a

%files -n vala-libmpdclient
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/libmpdclient.vapi
