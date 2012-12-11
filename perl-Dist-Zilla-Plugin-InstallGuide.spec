%define upstream_name    Dist-Zilla-Plugin-InstallGuide
%define upstream_version 1.101461

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Build an INSTALL file
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Dist::Zilla::File::InMemory)
BuildRequires:	perl(Dist::Zilla::Role::FileGatherer)
BuildRequires:	perl(Dist::Zilla::Role::TextTemplate)
BuildRequires:	perl(English)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Moose::Autobox)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::More) >= 0.940.0

BuildArch:	noarch

%description
This plugin adds a very simple _INSTALL_ file to the distribution, telling
the user how to install this distribution.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.yml META.json README
%{_mandir}/man3/*
%{perl_vendorlib}/*

