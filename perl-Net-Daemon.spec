#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	Daemon
Summary:	Net::Daemon - Perl extension for portable daemons
Summary(pl.UTF-8):	Net::Daemon - perlowe rozszerzenie dla przenośnych demonów
Name:		perl-Net-Daemon
Version:	0.41
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2243c25672507ce15e6d66cdd954fba0
URL:		http://search.cpan.org/dist/Net-Daemon/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(Thread)'

%description
Net::Daemon is an abstract base class for implementing portable server
applications in a very simple way. The module is designed for Perl
5.005 and threads, but can work with fork() and Perl 5.004.

%description -l pl.UTF-8
Net::Daemon to abstrakcyjna klasa bazowa do implementowania
przenośnych aplikacji serwerowych w bardzo prosty sposób. Ten moduł
był projektowany dla Perla 5.005 z wątkami, ale może działać także z
funkcją fork() i Perlem 5.004.

%prep
%setup -q -n %{pdir}-%{pnam}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Net/Daemon.pm
%{perl_vendorlib}/Net/Daemon
%{_mandir}/man3/*
