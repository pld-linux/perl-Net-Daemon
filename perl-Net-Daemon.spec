%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	Daemon

%define		_noautoreq	'perl(Thread)'

Summary:	Net::Daemon - Perl extension for portable daemons
Name:		perl-Net-Daemon
Version:	0.36
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::Daemon is an abstract base class for implementing portable server
applications in a very simple way. The module is designed for Perl 5.005
and threads, but can work with fork() and Perl 5.004.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Net/Daemon.pm
%{perl_sitelib}/Net/Daemon
%{_mandir}/man3/*
