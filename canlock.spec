Summary:	A library for creating and verifying cancel locks
Summary(pl.UTF-8):	Biblioteka do tworzenia i weryfikowania cancel-locków
Name:		canlock
Version:	2b
Release:	3
License:	BSD-like
Group:		Libraries
Source0:	http://mysite.verizon.net/vze4y7p6/cssri/tar/%{name}%{version}.tar.gz
# Source0-md5:	b35e464dfc54dcf1e7459a5ad67cb2f2
URL:		http://albasani.net/wiki/Cancel-Lock
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library for creating and verifying cancel locks (special news
articles headers that prevent cancelling articles by unauthorized
persons).

%description -l pl.UTF-8
Biblioteka do tworzenia i weryfikowania cancel-locków (specjalnych
nagłówków artykułów newsowych zapobiegających usuwaniu artykułów przez
osoby nieuprawnione).

%package devel
Summary:	Header files for canlock library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki canlock
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for canlock library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki canlock.

%package static
Summary:	Static canlock library
Summary(pl.UTF-8):	Statyczna biblioteka canlock
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static canlock library.

%description static -l pl.UTF-8
Statyczna biblioteka canlock.

%prep
%setup -q -n %{name}%{version}

%build
%{__make} libcanlock.a \
	CC="libtool --mode=compile %{__cc}" \
	CFLAGS="%{rpmcflags} -Iinclude"

libtool --mode=link %{__cc} %{rpmldflags} -o libcanlock.la src/*.lo -rpath %{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

libtool --mode=install install libcanlock.la $RPM_BUILD_ROOT%{_libdir}
install include/canlock.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES README doc
%attr(755,root,root) %{_libdir}/libcanlock.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcanlock.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcanlock.so
%{_libdir}/libcanlock.la
%{_includedir}/canlock.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libcanlock.a
