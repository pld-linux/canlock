Summary:	A library for creating and verifying cancel locks
Summary(pl):	Biblioteka do tworzenia i weryfikowania cancel-locków
Name:		canlock
Version:	2a
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	http://homepage.mac.com/imeowbot/%{name}%{version}.tar.gz
# Source0-md5:	2764d2ea24f97867b095e92339640e11
URL:		http://cssri.meowing.net/
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library for creating and verifying cancel locks (special news
articles headers that prevent cancelling articles by unauthorized
persons).

%description -l pl
Biblioteka do tworzenia i weryfikowania cancel-locków (specjalnych
nag³ówków artyku³ów newsowych zapobiegaj±cych usuwaniu artyku³ów przez
osoby nieuprawnione).

%package devel
Summary:	Header files for canlock library
Summary(pl):	Pliki nag³ówkowe biblioteki canlock
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for canlock library.

%description devel -l pl
Pliki nag³ówkowe biblioteki canlock.

%package static
Summary:	Static canlock library
Summary(pl):	Statyczna biblioteka canlock
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static canlock library.

%description static -l pl
Statyczna biblioteka canlock.

%prep
%setup -q -n %{name}2

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
%doc CHANGES README doc/HOWTO doc/draft*.txt
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/canlock.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
