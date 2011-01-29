Summary:	MPD client library
Summary(pl.UTF-8):	Biblioteka kliencka MPD
Name:		libmpdclient
Version:	2.4
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	http://downloads.sourceforge.net/musicpd/%{name}-%{version}.tar.gz
# Source0-md5:	efa6964c44fa7f01481a1f8365c1f6cb
URL:		http://www.musicpd.org/doc/libmpdclient/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	doxygen
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

%prep
%setup -q

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/doc

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README COPYING AUTHORS NEWS
%attr(755,root,root) %{_libdir}/libmpdclient.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmpdclient.so.?

%files devel
%defattr(644,root,root,755)
%doc doc/api/html
%attr(755,root,root) %{_libdir}/libmpdclient.so
%{_libdir}/libmpdclient.la
%{_includedir}/mpd
%{_pkgconfigdir}/libmpdclient.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libmpdclient.a
