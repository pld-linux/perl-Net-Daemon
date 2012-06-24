#
# Conditional build:
# _with_tests - perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	Daemon
Summary:	Net::Daemon module - Perl extension for portable daemons
Summary(pl):	Modu� Net::Daemon - perlowe rozszerzenie dla przeno�nych demon�w
Name:		perl-Net-Daemon
Version:	0.37
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5: 1f9acb45c6729e3a6ce3cae7697a6bde
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(Thread)'

%description
Net::Daemon is an abstract base class for implementing portable server
applications in a very simple way. The module is designed for Perl
5.005 and threads, but can work with fork() and Perl 5.004.

%description -l pl
Net::Daemon to abstrakcyjna klasa bazowa do implementowania
przeno�nych aplikacji serwerowych w bardzo prosty spos�b. Ten modu�
by� projektowany dla Perla 5.005 z w�tkami, ale mo�e dzia��� tak�e z
funkcj� fork() i Perlem 5.004.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?_with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Net/Daemon.pm
%{perl_vendorlib}/Net/Daemon
%{_mandir}/man3/*
