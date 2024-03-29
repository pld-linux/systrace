Summary:	Interactive Policy Generation for System Calls
Summary(pl.UTF-8):	Interaktywne generowanie polityki dla wywołań systemowych
Name:		systrace
Version:	1.6g
Release:	1
License:	BSD-like
Group:		Applications
Source0:	http://www.provos.org/uploads/%{name}-%{version}.tar.gz
# Source0-md5:	c4c0af2127af33e1b53c7aa07a970c5a
Patch0:		%{name}-newsysc.patch
URL:		http://www.provos.org/index.php?/categories/2-Systrace
BuildRequires:	libevent-devel
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Systrace enforces system call policies for applications by
constraining the application's access to the system. The policy is
generated interactively. Operations not covered by the policy raise an
alarm, allowing an user to refine the currently configured policy.

%description -l pl.UTF-8
systrace wymusza polityki wywołań systemowych dla aplikacji poprzez
ograniczanie dostępu aplikacji do systemu. Polityka jest generowana
interaktywnie. Operacje nie pokryte przez politykę podnoszą alarm,
pozwalając użytkownikowi na zmodyfikowanie aktualnie skonfigurowanej
polityki.

%prep
%setup -q
%patch0 -p1
sed -i -e 's#/usr/X11R6/bin/xsystrace#%{_bindir}/xsystrace#g' systrace.h

%build
%configure
echo -e "all:\ninstall:" > regress/Makefile
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/systrace
%{_mandir}/man1/systrace.1*
