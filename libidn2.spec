Summary:	Free software implementation of IDNA2008
Summary(pl.UTF-8):	Wolnodostępna implementacja IDNA2008
Name:		libidn2
Version:	0.6
Release:	1
License:	GPL v3+
Group:		Libraries
Source0:	http://alpha.gnu.org/gnu/libidn/%{name}-%{version}.tar.gz
# Source0-md5:	81b0852b25d9d5b10166c3325fb6f026
Patch0:		%{name}-info.patch
URL:		http://www.gnu.org/software/libidn/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake >= 1:1.10
BuildRequires:	gtk-doc >= 1.1
BuildRequires:	help2man
BuildRequires:	libtool >= 2:2.0
BuildRequires:	rpmbuild(macros) >= 1.98
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

%build
%{__libtoolize}
%{__aclocal} -I m4 -I gl/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# too common names
for f in lookup register ; do
	mv -f $RPM_BUILD_ROOT%{_bindir}/$f $RPM_BUILD_ROOT%{_bindir}/idn2-${f}
done

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/idn2
%attr(755,root,root) %{_bindir}/idn2-lookup
%attr(755,root,root) %{_bindir}/idn2-register
%attr(755,root,root) %{_libdir}/libidn2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libidn2.so.0
%{_mandir}/man1/idn2.1*
%{_infodir}/libidn2.info*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libidn2.so
%{_libdir}/libidn2.la
%{_includedir}/idn2.h
%{_mandir}/man3/idn2_*.3*
%{_gtkdocdir}/libidn2

%files static
%defattr(644,root,root,755)
%{_libdir}/libidn2.a
