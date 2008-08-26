Summary:	Interactive Policy Generation for System Calls
Summary(pl.UTF-8):	Interaktywne generowanie polityki dla wywołań systemowych
Name:		systrace
Version:	1.6e
Release:	2
License:	BSD-like
Group:		Applications
Source0:	http://www.citi.umich.edu/u/provos/systrace/%{name}-%{version}.tar.gz
# Source0-md5:	4fd65a51c97612822b658dd8eba79833
Patch0:		%{name}-newsysc.patch
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
