%include	/usr/lib/rpm/macros.perl
Summary:	Net-Daemon perl module
Summary(pl):	Modu³ perla Net-Daemon
Name:		perl-Net-Daemon
Version:	0.35
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/Net-Daemon-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net-Daemon perl module.

%description -l pl
Modu³ perla Net-Daemon.

%prep
%setup -q -n Net-Daemon-%{version}

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
