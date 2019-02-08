%bcond_with	tests
Summary:	Free software implementation of IDNA2008
Summary(pl.UTF-8):	Wolnodostępna implementacja IDNA2008
Name:		libidn2
Version:	2.1.1
Release:	1
License:	LGPL v3+ or GPL v2+ (library), GPL v3+ (utilities)
Group:		Libraries
Source0:	http://ftp.gnu.org/gnu/libidn/%{name}-%{version}.tar.lz
# Source0-md5:	22b61dbab9bd7e2d43c0e49c6c14f795
Patch0:		%{name}-info.patch
Patch1:		%{name}-pl.po-update.patch
URL:		http://www.gnu.org/software/libidn/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake >= 1:1.10
BuildRequires:	gettext-tools >= 0.19.3
BuildRequires:	gtk-doc >= 1.14
BuildRequires:	help2man
BuildRequires:	libtool >= 2:2.0
BuildRequires:	libunistring-devel
BuildRequires:	lzip
BuildRequires:	rpmbuild(macros) >= 1.98
BuildRequires:	tar >= 1:1.22
BuildRequires:	texinfo >= 4.7
Requires(post,postun):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libidn2 is a free software implementation of internationalized domain
names (IDNA2008).

%description -l pl.UTF-8
Libidn2 to wolnodostępna implementacja specyfikacji
umiędzynarodowionych nazw domen (IDNA2008).

%package devel
Summary:	Header files for libidn2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libidn2
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libunistring-devel

%description devel
Header files for libidn2 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libidn2.

%package static
Summary:	Static libidn2 library
Summary(pl.UTF-8):	Statyczna biblioteka libidn2
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libidn2 library.

%description static -l pl.UTF-8
Statyczna biblioteka libidn2.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%{__rm} po/stamp-po

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4 -I unistring/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README.md
%attr(755,root,root) %{_bindir}/idn2
%attr(755,root,root) %{_libdir}/libidn2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libidn2.so.0
%{_mandir}/man1/idn2.1*
%{_infodir}/libidn2.info*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libidn2.so
%{_libdir}/libidn2.la
%{_includedir}/idn2.h
%{_pkgconfigdir}/libidn2.pc
%{_mandir}/man3/idn2_*.3*
%{_gtkdocdir}/libidn2

%files static
%defattr(644,root,root,755)
%{_libdir}/libidn2.a
