Summary:	The Typesafe Signal Framework for C++
Name:		libsigc++
Version:	0.8.6
Release:	1
License:	LGPL
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Vendor:		Karl E. Nelson <kenelson@ece.ucdavis.edu>
Source0:	ftp://ftp.ece.ucdavis.edu/pub/kenelson/libsigc++/%name-%version.tar.gz
URL:		http://www.ece.ucdavis.edu/~kenelson/libsigc++/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library implements a full callback system for use in widget libraries,
abstract interfaces, and general programming. Originally part of the Gtk--
widget set, %name is now a seperate library to provide for more general use. It
is the most complete library of its kind with the ablity to connect an abstract
callback to a class method, function, or function object. It contains adaptor
classes for connection of dissimilar callbacks and has an ease of use unmatched
by other C++ callback libraries.

%package devel
Summary:	development tools for the Typesafe Signal Framework for C++ 
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	m4
Requires:	%{name} = %{version}

%description devel
Development tools for the Typesafe Signal Framework for C++.

%package static
Summary:	Static Typesafe Signal Framework for C++ libraries
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static Typesafe Signal Framework for C++ libraries.

%prep
%setup -q

%build
LDFLAGS="-s"
CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions"
export LDFLAGS CXXFLAGS
%configure

make

%install
rm -rf $RPM_BUILD_ROOT
make install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf AUTHORS README IDEAS NEWS ChangeLog TODO doc/*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz doc/*
%attr(755,root,root) %{_bindir}/sigc-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/sigc++
%{_libdir}/sigc++
%{_aclocaldir}/*

%files static
%attr(644,root,root) %{_libdir}/lib*.a
