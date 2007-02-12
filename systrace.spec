Summary:	Interactive Policy Generation for System Calls
Summary(pl.UTF-8):   Interaktywne generowanie polityki dla wywołań systemowych
Name:		systrace
Version:	1.6d
Release:	1
License:	BSD-like
Group:		Applications
Source0:	http://www.citi.umich.edu/u/provos/systrace/%{name}-%{version}.tar.gz
# Source0-md5:	91f2287a22e22ae1585c33c1f26b74dd
URL:		http://www.citi.umich.edu/u/provos/systrace/
BuildRequires:	libevent-devel
ExclusiveArch:	%{ix86}
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
sed -i -e 's#/usr/X11R6/bin/xsystrace#%{_bindir}/xsystrace#g' systrace.h

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/systrace
%{_mandir}/man1/systrace.1*
